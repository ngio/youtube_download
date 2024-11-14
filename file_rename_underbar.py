# 파이썬 컴파일 경로가 달라서 현재 폴더의 이미지를 호출하지 못할때 작업디렉토리를 변경한다. 
import os
from pathlib import Path
# src 상위 폴더를 실행폴더로 지정하려고 한다.
###real_path = Path(__file__).parent.parent
real_path = Path(__file__).parent
print(real_path)
#작업 디렉토리 변경
os.chdir(real_path) 


def replace_spaces_in_filenames(folder_path):
    # 폴더 내 모든 파일을 반복
    for filename in os.listdir(folder_path):
        # 파일의 전체 경로 생성
        old_file_path = os.path.join(folder_path, filename)

        # 파일 이름에 공백이 있는지, -도 _로 변경 확인
        if ' ' in filename or  '-' in filename:
            # 공백을 언더바로 대체
            new_filename = filename.replace(' ', '_').replace('-', '_')
            new_file_path = os.path.join(folder_path, new_filename)

            
            # 파일이 존재할경우 덮어쓸지, 빠져나갈지 
            if os.path.exists(new_file_path):
                overwrite = input(f"'{new_file_path}' already exists. Overwrite? (y/n): ")
                if overwrite.lower() == 'y':
                    os.remove(new_file_path)
                else:
                    print("Operation canceled.")
                    exit()
            # 파일 이름 변경
            os.rename(old_file_path, new_file_path)
            
            
            print(f"Renamed: '{filename}' -> '{new_filename}'")
        else:
            print(f"No change: '{filename}'")

# 사용 예시
#folder_path = 'path_to_your_folder'  # 여기에 폴더 경로를 입력하세요
#folder_path = 'D:\______통합로그인'  # 여기에 폴더 경로를 입력하세요
#replace_spaces_in_filenames(folder_path)


