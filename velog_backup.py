import feedparser
import os
import re
from datetime import datetime
import html2text

# --- 설정 구간 ---
VELOG_ID = "bluepaper14_"  # 벨로그 아이디
RSS_URL = f"https://v2.velog.io/rss/{VELOG_ID}"
BACKUP_DIR = "posts"  # 글이 저장될 폴더 이름

def clean_filename(title):
    # 파일명으로 쓸 수 없는 문자 제거
    return re.sub(r'[\\/*?:"<>|]', "", title)

def main():
    # 1. RSS 피드 가져오기
    feed = feedparser.parse(RSS_URL)
    
    # 2. 저장할 폴더 생성
    if not os.path.exists(BACKUP_DIR):
        os.makedirs(BACKUP_DIR)

    # 3. Git 설정 (GitHub Actions 환경용)
    os.system('git config --global user.name "GitHub Action"')
    os.system('git config --global user.email "action@github.com"')

    has_updates = False
    
    # RSS 피드를 역순(과거순)으로 처리하여 커밋 로그를 순서대로 기록
    for entry in reversed(feed.entries):
        title = entry.title
        link = entry.link
        # 발행일 추출
        published = entry.get('published', datetime.now().strftime("%Y-%m-%d %H:%M"))
        
        # --- 태그 추출 로직 보강 ---
        raw_tags = entry.get('tags', [])
        actual_tags = []
        for t in raw_tags:
            # 피드 객체 형태에 따라 term 속성 혹은 키값을 추출
            if hasattr(t, 'term'):
                actual_tags.append(t.term)
            elif isinstance(t, dict) and 'term' in t:
                actual_tags.append(t['term'])
        
        # 태그가 있으면 쉼표로 구분, 없으면 기본값 부여
        tags_str = ", ".join(actual_tags) if actual_tags else "velog, backup"

        # HTML 콘텐츠를 마크다운으로 변환
        content_html = entry.description
        h = html2text.HTML2Text()
        h.ignore_links = False
        content_md = h.handle(content_html)

        # 파일명 및 경로 설정
        filename = clean_filename(title) + ".md"
        filepath = os.path.join(BACKUP_DIR, filename)

        # 옵시디언 YAML Frontmatter 구성 (태그 포함)
        full_content = f"""---
title: "{title}"
date: {published}
url: "{link}"
tags: [{tags_str}]
---

# [{title}]({link})

{content_md}
"""

        is_new_or_updated = False
        
        # 파일 변경 감지: 파일이 없거나 내용이 다르면 업데이트
        if not os.path.exists(filepath):
            is_new_or_updated = True
        else:
            with open(filepath, 'r', encoding='utf-8') as f:
                old_content = f.read()
            if old_content.strip() != full_content.strip():
                is_new_or_updated = True

        if is_new_or_updated:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(full_content)
            
            print(f"Commit: {title}")
            os.system(f'git add "{filepath}"')
            # 파일별로 커밋 생성
            os.system(f'git commit -m "Update post: {title}"')
            has_updates = True

    # 4. 모든 변경사항을 한 번에 Push
    if has_updates:
        os.system('git push')
    else:
        print("No updates found.")

if __name__ == "__main__":
    main()
