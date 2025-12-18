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

    # 3. Git 설정
    os.system('git config --global user.name "GitHub Action"')
    os.system('git config --global user.email "action@github.com"')

    has_updates = False
    
    # RSS 피드 역순 정렬 (과거순으로 처리)
    for entry in reversed(feed.entries):
        title = entry.title
        link = entry.link
        # 날짜 추출
        published = entry.get('published', datetime.now().strftime("%Y-%m-%d %H:%M"))
        
        # --- 태그 추출 추가 ---
        tags = [tag.term for tag in entry.get('tags', [])]
        tags_str = ", ".join(tags) if tags else "velog, backup"

        # HTML을 마크다운으로 변환
        content_html = entry.description
        h = html2text.HTML2Text()
        h.ignore_links = False
        content_md = h.handle(content_html)

        # 파일명 및 경로 설정
        filename = clean_filename(title) + ".md"
        filepath = os.path.join(BACKUP_DIR, filename)

        # 옵시디언 최적화 YAML Frontmatter 구성
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
        
        # 파일 변경 감지
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
            os.system(f'git commit -m "Update post: {title}"')
            has_updates = True

    # 4. 변경사항 Push
    if has_updates:
        os.system('git push')
    else:
        print("No updates found.")

if __name__ == "__main__":
    main()
