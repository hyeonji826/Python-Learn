# pyqt5 라이브버리
# 외부 GUI 라이브러리로, 설치를 해야 사용할 수 있다.
# pip install pyqt5
# 외부 GUI 라이브러리 중에서도 지원하는 기능이 강련한
# 라이브러리이다.

import sys
from PyQt5.QtWidgets import QApplication,QWidget

# 기본 앱 만들기
# Qwidget클래스를 상속받아 그 기능을 받아쓴다.
class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    # UI를 초기화하기 위한 메서드 선언
    def initUI(self):
        # 제목 설정
        self.setWindowTitle("pyQt5로 만드는 첫번째 프로그램")

        # 창크기 설정
        self.setGeometry(0,0,200,300)
            
        # 창 나타내기
        self.show()

    if __name__=="__main__":
        app=QApplication(sys.argv)
        # ex = MyApp()
        sys.exit(app.exec_())