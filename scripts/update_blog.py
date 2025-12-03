import feedparser
import os
import urllib.parse # 태그를 URL로 변환하기 위해 추가

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
            
            # 태그 처리
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
            
            # (2) 작성자 및 날짜 (회색 느낌을 낼 수 없으므로 이탤릭체 활용)
            # 날짜 포맷이 길어서 깔끔하게 자름 (예: Mon, 17 Nov 2025...)
            date_str = entry.published
            try:
                # 2025년 11월 17일 형태로 변환은 복잡하므로 RSS 원본 사용하되 깔끔하게 표시
                pass 
            except:
                pass
                
            f.write(f"**{entry.author}** · *{date_str}*\n\n")

            # (3) 태그를 '뱃지' 스타일로 변환 (Velog 태그 느낌)
            # Shields.io 서비스를 이용해 텍스트를 이미지 버튼으로 바꿉니다.
            tag_badges = ""
            if tags:
                for tag in tags:
                    # 태그명 URL 인코딩 (C# -> C%23 등 특수문자 처리)
                    safe_tag = urllib.parse.quote(tag)
                    # 다크 그레이 색상(#3E4C59)의 뱃지 생성
                    badge_url = f"https://img.shields.io/badge/{safe_tag}-3E4C59?style=flat-square&logoColor=white"
                    tag_badges += f"![{tag}]({badge_url}) "
            
            f.write(f"{tag_badges}\n\n")
            
            # 구분선
            f.write(f"---\n")
            f.write(f"<br/>\n\n") # 약간의 여백
            
            # -----------------------------------------------------------
            
            # 3. 글 본문
            f.write(entry.description)
        
        print(f"New post saved: {file_name}")
