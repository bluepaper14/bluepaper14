import feedparser
import os
import html
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
    cleaned = re.sub(r'[\\/*?:"<>|]', '', title)
    return cleaned.replace(' ', '-')

def remove_html_tags(text):
    clean = re.compile('<.*?>')
    return html.unescape(re.sub(clean, '', text)).strip()

def get_thumbnail_url(content):
    match = re.search(r'<img[^>]+src="([^">]+)"', content)
    if match:
        return match.group(1)
    # 기본 이미지 (필요시 변경)
    return "https://velog.velcdn.com/images/velog/profile/9aa07f66-5fcd-41f4-84f2-91d73afcec28/social_image.png"

def update_readme(posts):
    # 파일을 줄 단위로 읽어옵니다
    with open(readme_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    start_index = -1
    end_index = -1

    # 마커의 위치를 찾습니다
    for i, line in enumerate(lines):
        if '' in line:
            start_index = i
        if '' in line:
            end_index = i

    # 마커가 없으면 종료
    if start_index == -1 or end_index == -1:
        print("Error: README.md에 마커 위치를 찾을 수 없습니다.")
        return

    # 새로운 HTML 테이블 내용 생성
    new_content_lines = []
    new_content_lines.append("### 📰 Recent Posts\n")
    new_content_lines.append("<table width='100%'>\n")

    for post in posts[:3]:
        title = post['title']
        local_link = f"./{OUTPUT_DIR}/{clean_filename(title)}.md"
        summary = remove_html_tags(post['description'])[:100] + "..."
        date = post['date'][:10]
        thumbnail = get_thumbnail_url(post['description'])

        row = f"""    <tr>
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
    </tr>\n"""
        new_content_lines.append(row)
    
    new_content_lines.append("</table>\n")

    # 기존 내용 중 마커 앞부분 + 새로운 내용 + 마커 뒷부분 결합
    final_lines = lines[:start_index+1] + new_content_lines + lines[end_index:]

    # 파일 저장
    with open(readme_path, 'w', encoding='utf-8') as file:
        file.writelines(final_lines)

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
