import feedparser
import git
import os
import re

# Velog RSS 주소
RSS_URL = 'https://api.velog.io/rss/@bluepaper14'

# 글이 저장될 폴더
OUTPUT_DIR = 'velog-posts'
readme_path = 'README.md'

# 폴더가 없으면 생성
if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

def clean_filename(title):
    # 파일명에 쓸 수 없는 특수문자 제거 및 공백을 -로 변경
    cleaned = re.sub(r'[\\/*?:"<>|]', '', title)
    return cleaned.replace(' ', '-')

def update_readme(posts):
    # README 파일 읽기
    with open(readme_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # 삽입할 내용 생성 (최근 3개, 로컬 파일 링크)
    new_content = ""
    for post in posts[:3]: # 상위 3개만
        filename = clean_filename(post['title']) + '.md'
        # 상대 경로로 링크 걸기 (GitHub 파일 뷰어로 이동됨)
        new_content += f"- [{post['title']}](./{OUTPUT_DIR}/{filename}) <br>\n"

    # 정규식으로 마커 사이의 내용을 교체
    pattern = r'()([\s\S]*?)()'
    replacement = f'\\1\n{new_content}\\3'
    
    updated_content = re.sub(pattern, replacement, content)

    # 변경사항 저장
    with open(readme_path, 'w', encoding='utf-8') as file:
        file.write(updated_content)

def main():
    feed = feedparser.parse(RSS_URL)
    
    posts = []
    
    # 글 목록 순회 (최신글부터)
    for entry in feed.entries:
        title = entry.title
        # RSS description은 HTML 형식이므로 그대로 저장하거나, 필요시 html2text 등으로 변환 가능
        # 여기서는 간단히 HTML 내용을 그대로 md 파일에 저장 (GitHub는 md 안의 HTML도 렌더링 함)
        # 만약 순수 마크다운 변환을 원하면 html2text 라이브러리 추가 필요
        content = entry.description 
        link = entry.link
        date = entry.published

        filename = clean_filename(title) + '.md'
        file_path = os.path.join(OUTPUT_DIR, filename)

        # 파일 생성/업데이트 (헤더 정보를 포함한 MD 파일 생성)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(f"# {title}\n\n")
            f.write(f"Parsed from [Velog]({link})\n\n")
            f.write(f"Date: {date}\n\n")
            f.write("---\n\n")
            f.write(content) # 이미지는 HTML img 태그로 들어가며 Velog 서버 링크 유지됨
        
        posts.append({'title': title, 'path': file_path})

    # README 업데이트
    update_readme(posts)

if __name__ == '__main__':
    main()
