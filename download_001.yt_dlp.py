# 파이썬 컴파일 경로가 달라서 현재 폴더의 이미지를 호출하지 못할때 작업디렉토리를 변경한다. 
import os
from pathlib import Path
# src 상위 폴더를 실행폴더로 지정하려고 한다.
###real_path = Path(__file__).parent.parent
real_path = Path(__file__).parent
print(real_path)
#작업 디렉토리 변경
os.chdir(real_path) 

import yt_dlp

def main():
    # 다운로드할 YouTube 비디오의 URL
    #url = 'https://www.youtube.com/watch?v=vjcuQLjSUz4'
    """_summary_
    https://www.youtube.com/watch?v=UFQEttrn6CQ
    https://www.youtube.com/watch?v=bU9nLBUoLJ0 
    https://www.youtube.com/watch?v=SX_ViT4Ra7k
    """
    
    # 사용자로부터 YouTube 비디오 URL 입력받기
    url = input("다운로드할 YouTube 비디오의 URL을 입력하세요: ")

    # 다운로드 옵션 설정
    ydl_opts = {
        'format': 'best',                   # 최고 화질 선택 (audio와 video 포함)
        'outtmpl': './downloads/%(title)s.%(ext)s',  # 다운로드 파일 경로 및 이름 템플릿
    }

    # yt-dlp를 사용하여 다운로드
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    print("Video has been downloaded successfully!")


# 메인 함수 호출
if __name__ == "__main__":
    main()


