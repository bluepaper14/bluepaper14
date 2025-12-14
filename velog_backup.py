import feedparser
import os
import re
from datetime import datetime
import html2text

# --- 설정 구간 ---
VELOG_ID = "bluepaper14_"  # 벨로그 아이디 (언더바 포함 확인)
RSS_URL = f"https://v2.velog.io/rss/{VELOG_ID}"
BACKUP_DIR = "posts"  # 글이 저장될 폴더 이름

# --- 메인 로직 ---
def clean_filename(title):
    # 파일명으로 쓸 수 없는 문자 제거
    return re.sub(r'[\\/*?:"<>|]', "", title)

def main():
    # 1. RSS 피드 가져오기
    feed = feedparser.parse(RSS_URL)
    
    # 2. 저장할 폴더 생성
    if not os.path.exists(BACKUP_DIR):
        os.makedirs(BACKUP_DIR)

    # 3. Git 설정 (GitHub Actions에서 실행될 때 필요)
    os.system('git config --global user.name "GitHub Action"')
    os.system('git config --global user.email "action@github.com"')

    has_updates = False
    
    # RSS 피드는 최신글이 앞쪽에 있으므로, 과거 순으로 커밋하고 싶다면 뒤집어야 함
    # 하지만 "새로 쓴 글"을 감지하는 것이므로 순서는 크게 상관 없으나,
    # 동시에 여러 글을 썼을 때 순서대로 커밋되게 하기 위해 역순 정렬 추천
    for entry in reversed(feed.entries):
        title = entry.title
        link = entry.link
        # RSS에는 전체 내용이 없을 수도 있지만, Velog는 대개 description에 내용을 포함함
        # html 형식을 마크다운으로 변환
        content_html = entry.description
        h = html2text.HTML2Text()
        h.ignore_links = False
        content_md = h.handle(content_html)

        # 파일명 생성 (제목.md)
        filename = clean_filename(title) + ".md"
        filepath = os.path.join(BACKUP_DIR, filename)

        # 내용 앞에 원본 링크와 제목 추가
        full_content = f"# [{title}]({link})\n\n{content_md}"

        # 파일 변경 감지 로직
        is_new_or_updated = False
        
        # 기존 파일이 없으면 생성
        if not os.path.exists(filepath):
            is_new_or_updated = True
        else:
            # 기존 파일이 있다면 내용을 읽어서 비교 (변경사항이 있을 때만 커밋)
            with open(filepath, 'r', encoding='utf-8') as f:
                old_content = f.read()
            if old_content.strip() != full_content.strip():
                is_new_or_updated = True

        if is_new_or_updated:
            # 파일 쓰기
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(full_content)
            
            # --- 핵심: 게시물 1개당 1 커밋 ---
            print(f"Commit: {title}")
            os.system(f'git add "{filepath}"')
            os.system(f'git commit -m "Update post: {title}"')
            has_updates = True

    # 4. 변경사항이 있다면 GitHub으로 Push
    if has_updates:
        os.system('git push')
    else:
        print("No updates found.")

if __name__ == "__main__":
    main()
