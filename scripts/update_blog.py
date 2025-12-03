import feedparser
import os
import urllib.parse

# 벨로그 RSS 주소
rss_url = 'https://v2.velog.io/rss/bluepaper14'

# 글을 저장할 폴더 이름
save_dir = 'velog-posts'

# 폴더가 없으면 생성
if not os.path.exists(save_dir):
    os.makedirs(save_dir)

# RSS 피드 가져오기
feed = feedparser.parse(rss_url)

# 각 글을 순회하며 파일로 저장
for entry in feed.entries:
    # 파일 이름 정제
    file_name = entry.title
    file_name = file_name.replace('/', '-')
    file_name = file_name.replace('\\', '-')
    file_name = file_name[:200]
    
    file_path = os.path.join(save_dir, f'{file_name}.md')

    # 파일이 이미 존재하지 않을 때만 생성
    if not os.path.exists(file_path):
        with open(file_path, 'w', encoding='utf-8') as f:
            # 1. YAML Front Matter (메타 데이터)
            f.write(f"---\n")
            clean_title = entry.title.replace('"', "'")
            f.write(f'title: "{clean_title}"\n')
            f.write(f'date: {entry.published}\n')
            
            # 태그 처리 (에러 방지)
            tags = []
            if hasattr(entry, 'tags'):
                tags = [t.term for t in entry.tags]
                f.write(f'categories: {tags}\n')
            else:
                f.write(f'categories: []\n')
            
            f.write(f"---\n\n")
            
            # -----------------------------------------------------------
            # 2. [Velog 스타일 헤더 구현] 
            # -----------------------------------------------------------
            
            # (1) 제목 (H1)
            f.write(f"# {entry.title}\n\n") 
            
            # (2) 작성자 및 날짜 처리 (에러 방지 로직 추가)
            author_name = "bluepaper14" # 기본값
            if hasattr(entry, 'author'):
                author_name = entry.author
            
            date_str = entry.published
                
            f.write(f"**{author_name}** · *{date_str}*\n\n")

            # (3) 태그를 '뱃지' 스타일로 변환
            tag_badges = ""
            if tags:
                for tag in tags:
                    safe_tag = urllib.parse.quote(tag)
                    # 회색 뱃지 스타일
                    badge_url = f"https://img.shields.io/badge/{safe_tag}-3E4C59?style=flat-square&logoColor=white"
                    tag_badges += f"![{tag}]({badge_url}) "
            
            f.write(f"{tag_badges}\n\n")
            
            # 구분선
            f.write(f"---\n")
            f.write(f"<br/>\n\n") 
            
            # -----------------------------------------------------------
            
            # 3. 글 본문
            f.write(entry.description)
        
        print(f"New post saved: {file_name}")
