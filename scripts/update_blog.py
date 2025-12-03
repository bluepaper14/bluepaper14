import feedparser
import git
import os

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
    # 파일 이름에 들어갈 수 없는 문자 제거
    file_name = entry.title
    file_name = file_name.replace('/', '-')
    file_name = file_name.replace('\\', '-')
    # 파일명 길이 제한
    file_name = file_name[:200]
    
    file_path = os.path.join(save_dir, f'{file_name}.md')

    # 파일이 이미 존재하지 않을 때만 생성
    if not os.path.exists(file_path):
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(f"---\n")
            
            clean_title = entry.title.replace('"', "'")
            f.write(f'title: "{clean_title}"\n')
            f.write(f'date: {entry.published}\n')
            
            # [수정] 태그가 있을 때만 가져오기 (에러 방지)
            if hasattr(entry, 'tags'):
                tags = [t.term for t in entry.tags]
                f.write(f'categories: {tags}\n')
            else:
                f.write(f'categories: []\n')

            f.write(f"---\n\n")
            
            # [제목 추가] 마크다운 H1 태그로 제목 크게 출력
            f.write(f"# {entry.title}\n\n") 
            
            # 글 내용
            f.write(entry.description)
        
        print(f"New post saved: {file_name}")
