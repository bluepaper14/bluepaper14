import feedparser
import git
import os
import re

# Velog RSS 주소
RSS_URL = 'https://api.velog.io/rss/@bluepaper14'

# 글이 저장될 폴더
OUTPUT_DIR = 'velog-posts'

# 폴더가 없으면 생성
if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

def clean_filename(title):
    # 파일명에 쓸 수 없는 특수문자 제거 및 공백을 -로 변경
    cleaned = re.sub(r'[\\/*?:"<>|]', '', title)
    return cleaned.replace(' ', '-')

def main():
    feed = feedparser.parse(RSS_URL)
    
    # 글 목록 순회
    for entry in feed.entries:
        title = entry.title
        content = entry.description 
        link = entry.link
        date = entry.published

        filename = clean_filename(title) + '.md'
        file_path = os.path.join(OUTPUT_DIR, filename)

        # 파일이 없을 때만 생성하거나, 덮어쓰기 (원하는 대로 동작)
        # 여기서는 항상 최신 내용으로 덮어쓰도록 함
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(f"# {title}\n\n")
            f.write(f"Parsed from [Velog]({link})\n\n")
            f.write(f"Date: {date}\n\n")
            f.write("---\n\n")
            f.write(content)
            
        print(f"Saved: {filename}")

if __name__ == '__main__':
    main()
