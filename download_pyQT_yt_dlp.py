# 파이썬 컴파일 경로가 달라서 현재 폴더의 이미지를 호출하지 못할때 작업디렉토리를 변경한다. 
import os
from pathlib import Path
# src 상위 폴더를 실행폴더로 지정하려고 한다.
###real_path = Path(__file__).parent.parent
real_path = Path(__file__).parent
print(real_path)
#작업 디렉토리 변경
os.chdir(real_path) 

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel, QScrollArea
import yt_dlp
import threading

class URLInputWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # 윈도우 설정
        self.setWindowTitle("YouTube URL 입력 받기")
        self.setGeometry(300, 300, 500, 300)

        # 레이아웃 설정
        layout = QVBoxLayout()

        # URL 입력 필드 (QLineEdit)
        self.url_input = QLineEdit(self)
        self.url_input.setPlaceholderText("Enter YouTube URL...")
        layout.addWidget(self.url_input)

        # URL 입력 버튼
        self.submit_button = QPushButton("Download", self)
        self.submit_button.clicked.connect(self.onSubmit)
        layout.addWidget(self.submit_button)

        # 다운로드 상태 표시 레이블
        self.result_label = QLabel(self)
        self.result_label.setWordWrap(True)

        # 스크롤 가능한 영역 설정
        scroll_area = QScrollArea(self)
        scroll_area.setWidgetResizable(True)
        scroll_area.setWidget(self.result_label)
        layout.addWidget(scroll_area)

        # 레이아웃 설정
        self.setLayout(layout)

    def onSubmit(self):
        # 입력된 URL 가져오기 및 앞뒤 공백 제거
        url = self.url_input.text().strip()

        if url:
            # 다운로드 상태 레이블 초기화 (첫 번째 제출 시에만 초기화)
            self.result_label.setText("Downloading... Please wait.")
            
            # 다운로드 작업을 별도의 스레드에서 실행
            threading.Thread(target=self.download_video, args=(url,)).start()
        else:
            self.result_label.setText("Please enter a valid URL.")

    def download_video(self, url):
        try:
            # yt-dlp 다운로드 옵션 설정
            ydl_opts = {
                'format': 'best',  # 최고의 품질로 다운로드
                'outtmpl': './downloads/%(title)s.%(ext)s',  # 저장 위치 및 파일명
                'progress_hooks': [self.progress_hook],  # 다운로드 진행 상태 표시 함수
                'logger': MyLogger(self.result_label)  # 사용자 정의 로거를 사용하여 로그 출력
            }

            # yt-dlp 다운로드 실행
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])

            # 다운로드 완료 후 결과 표시 (메시지만 추가)
            self.result_label.setText(self.result_label.text() + "\nDownload complete!")
        except Exception as e:
            # 예외 발생 시 에러 메시지 표시
            self.result_label.setText(f"Error: {str(e)}")

    def progress_hook(self, d):
        if d['status'] == 'downloading':
            # 다운로드 진행 정보 추출
            percent = d['_percent_str']
            speed = d.get('speed', 'Unknown')  # 다운로드 속도 (없을 경우 'Unknown'으로 처리)
            downloaded = d['downloaded_bytes']
            total = d['total_bytes']
            eta = d.get('eta', 'Unknown')  # 예상 남은 시간 (없을 경우 'Unknown'으로 처리)

            # 다운로드된 크기와 총 크기 (MB로 변환)
            downloaded_mb = downloaded / (1024 * 1024)
            total_mb = total / (1024 * 1024)

            # 다운로드 진행 상태를 레이블에 표시
            self.result_label.setText(f"{self.result_label.text()}\nDownloading: {percent} - Speed: {speed} - "
                                      f"Downloaded: {downloaded_mb:.2f} MB / {total_mb:.2f} MB - "
                                      f"ETA: {eta}s")
        elif d['status'] == 'finished':
            # 다운로드가 완료되면 완료 메시지 표시
            self.result_label.setText(f"{self.result_label.text()}\nDownload complete!")

class MyLogger:
    def __init__(self, result_label):
        self.result_label = result_label

    def debug(self, msg):
        self.update_log(msg)

    def info(self, msg):
        self.update_log(msg)

    def warning(self, msg):
        self.update_log(msg)

    def error(self, msg):
        self.update_log(msg)

    def update_log(self, msg):
        current_text = self.result_label.text()
        new_text = current_text + "\n" + msg
        self.result_label.setText(new_text)

# PyQt 애플리케이션 실행
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = URLInputWindow()
    window.show()
    sys.exit(app.exec_())
    




