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
    
    for entry in reversed(feed.entries):
        title = entry.title
        link = entry.link
        published = entry.get('published', datetime.now().strftime("%Y-%m-%d %H:%M"))
        
        # --- [수정] 태그 추출 로직 대폭 강화 ---
        actual_tags = []
        
        # 1) 표준 tags 필드 확인
        if 'tags' in entry:
            for t in entry.tags:
                if hasattr(t, 'term') and t.term:
                    actual_tags.append(t.term)
                elif isinstance(t, dict) and 'term' in t:
                    actual_tags.append(t['term'])
        
        # 2) 만약 위 방법으로 안나오면 category 필드 확인 (RSS 라이브러리에 따라 다름)
        if not actual_tags and 'categories' in entry:
            actual_tags = [c for c in entry.categories if c]

        # 중복 제거 및 공백 정리
        actual_tags = list(set([t.strip() for t in actual_tags if t.strip()]))
        
        # 태그가 없으면 기본값, 있으면 사용자 태그 사용
        tags_str = ", ".join(actual_tags) if actual_tags else "velog, backup"
        # ---------------------------------------

        content_html = entry.description
        h = html2text.HTML2Text()
        h.ignore_links = False
        content_md = h.handle(content_html)

        filename = clean_filename(title) + ".md"
        filepath = os.path.join(BACKUP_DIR, filename)

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
            
            print(f"Commit: {title} (Tags: {tags_str})")
            os.system(f'git add "{filepath}"')
            os.system(f'git commit -m "Update post: {title}"')
            has_updates = True

    if has_updates:
        os.system('git push')
    else:
        print("No updates found.")

if __name__ == "__main__":
    main()
