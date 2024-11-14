# 파이썬 컴파일 경로가 달라서 현재 폴더의 이미지를 호출하지 못할때 작업디렉토리를 변경한다. 
import os
from pathlib import Path
# src 상위 폴더를 실행폴더로 지정하려고 한다.
###real_path = Path(__file__).parent.parent
real_path = Path(__file__).parent
print(real_path)
#작업 디렉토리 변경
os.chdir(real_path) 


#  pip install moviepy
#  Python에서 moviepy 또는 pydub 라이브러리를 사용하여 MP4 파일을 MP3 형식으로 변환할 수 있습니다.
"""https://pypi.org/project/moviepy/
    pip install moviepy
    
    MoviePy(전체 문서)는 비디오 편집을 위한 Python 라이브러리입니다. 
    자르기, 연결, 제목 삽입, 비디오 합성(일명 비선형 편집), 
    비디오 처리 및 사용자 지정 효과 생성. 사용 사례는 갤러리를 참조하세요.
"""

from moviepy.editor import *

# MP4 파일이 있는 폴더 경로 지정
folder_path = './downloads'

# 파일명에 공백이 있으면 _로 변경
import file_rename_underbar as fru

# 폴더내의 파일명 rename
fru.replace_spaces_in_filenames(folder_path)


# 폴더 내의 모든 파일 확인
for filename in os.listdir(folder_path):
    if filename.endswith('.mp4'):
        mp4_path = os.path.join(folder_path, filename)
        mp3_path = os.path.join(folder_path, filename.replace('.mp4', '.mp3'))

        # 동일한 이름의 MP3 파일이 존재하면 건너뛰기
        if os.path.exists(mp3_path):
            print(f"Skipped: {filename} (MP3 already exists)")
            continue
        
        # 비디오에서 오디오 추출 후 MP3로 저장
        video = VideoFileClip(mp4_path)
        video.audio.write_audiofile(mp3_path)
        video.close()  # 명시적으로 close 호출하여 자원 해제

        print(f"Converted: {filename} to MP3")
    else:
        print(f"Converted Not: {filename} to MP3")

