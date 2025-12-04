import feedparser
import os
import re
import html

# Velog RSS 주소
RSS_URL = 'https://api.velog.io/rss/@bluepaper14'

# 글이 저장될 폴더
OUTPUT_DIR = 'velog-posts'
readme_path = 'README.md'

# 폴더가 없으면 생성
if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

def clean_filename(title):
    cleaned = re.sub(r'[\\/*?:"<>|]', '', title)
    return cleaned.replace(' ', '-')

def remove_html_tags(text):
    # HTML 태그 제거 및 엔티티 처리
    clean = re.compile('<.*?>')
    return html.unescape(re.sub(clean, '', text)).strip()

def get_thumbnail_url(content):
    # RSS 내용 중 첫 번째 이미지(img src)를 찾음
    match = re.search(r'<img[^>]+src="([^">]+)"', content)
    if match:
        return match.group(1)
    # 이미지가 없을 경우 기본 이미지 (필요하면 수정하세요)
    return "https://velog.velcdn.com/images/velog/profile/9aa07f66-5fcd-41f4-84f2-91d73afcec28/social_image.png"

def update_readme(posts):
    with open(readme_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # 최근 3개 글을 테이블 형식으로 생성
    new_content = "### 📰 Recent Posts\n"
    new_content += "<table width='100%'>\n"
    
    for post in posts[:3]:
        title = post['title']
        link = post['link'] # 로컬 파일 대신 원본 Velog 링크로 이동하고 싶으면 이 변수 사용
        local_link = f"./{OUTPUT_DIR}/{clean_filename(title)}.md"
        summary = remove_html_tags(post['description'])[:100] + "..." # 100자 요약
        date = post['date'][:10] # 날짜만 자르기 (YYYY-MM-DD)
        thumbnail = get_thumbnail_url(post['description'])

        # HTML 테이블 행 추가 (이미지 | 내용)
        new_content += f"""
    <tr>
        <td width="30%">
            <a href="{local_link}">
                <img src="{thumbnail}" width="100%" style="border-radius:10px;" alt="thumbnail">
            </a>
        </td>
        <td width="70%">
            <b><a href="{local_link}">{title}</a></b><br>
            <span style="font-size:12px; color:gray;">{date}</span><br>
            <span style="font-size:13px;">{summary}</span>
        </td>
    </tr>
        """
    new_content += "</table>\n"

    # 기존 마커 사이의 내용을 교체
    # 주의: 마커까지 포함해서 교체하지 않고, 마커 '사이'만 교체
    pattern = r'()([\s\S]*?)()'
    replacement = f'\\1\n{new_content}\n\\3'
    
    updated_content = re.sub(pattern, replacement, content)

    with open(readme_path, 'w', encoding='utf-8') as file:
        file.write(updated_content)

def main():
    feed = feedparser.parse(RSS_URL)
    posts = []
    
    for entry in feed.entries:
        title = entry.title
        content = entry.description 
        link = entry.link
        date = entry.published

        filename = clean_filename(title) + '.md'
        file_path = os.path.join(OUTPUT_DIR, filename)

        # 로컬 md 파일 저장
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(f"# {title}\n\n")
            f.write(f"Parsed from [Velog]({link})\n\n")
            f.write(f"Date: {date}\n\n")
            f.write("---\n\n")
            f.write(content)
        
        posts.append({
            'title': title, 
            'path': file_path, 
            'description': content, 
            'date': date,
            'link': link
        })

    update_readme(posts)

if __name__ == '__main__':
    main()
