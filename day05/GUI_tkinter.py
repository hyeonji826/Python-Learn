# GUI(Graphic User Interface)
# CLI(Command LIne Interface)와 대응되는 개념으로 
# 버튼, 이미지, 텍스트 박스 등 
# 시작적인 요소를 통해 프로그램과 상호작용하는 것을 말한다.
# 파이썬에는 기본 내장 라이브러리로 
# tkinter라는 GUI 툴킷이 존재한다.
# 기본 내장 라이브러리라 기능이 강력하진 않지만
# GUI 라이브러리의 기본을 익히기에는 충분하다.
import tkinter as tk
from tkinter import messagebox as msg

class GUI_practice():
    def __init__(self,root:tk.Tk=None):
        self.root=root or tk.Tk() # 외부에서 전달받은 root가 비어있다면
        # 내부에서 생성

        # 기타 세팅을 할 메서드
        self.settings()

        # 프로그램 메인 루프 실행
        self.root.mainloop()

    def settings(self):
        # 프로그램의 상단 제목 설정
        self.root.title("처음 만들어보는 GUI 프로그램")

        # 프로그램 창의 크기 설정(가로x세로)
        width,hight=300,200
        self.root.geometry(f"{width}x{hight}")

        # 라벨 위젯 생성
        # tk.Label(윈도우객체,text="라벨에 적을 내용",font=)
        self.labell1=tk.Label(self.root,text="첫번째 라벨")
        self.labell1.pack(pady=10)

        # 텍스트 한 줄을 입력하기 위한
        # Entry 위젯
        self.entry=tk.Entry(self.root, width=20)
        self.entry.pack(pady=5)
        
        # 버튼 위젯 생성
        # command 매개변수는 함수를 전달하는 매개변수로(call back)
        # 소괄호 없이 함수 혹은 메서드의 이름만 전달해야 한다.
        self.submit=tk.Button(self.root,text="전송",command=self.bth_click)
        self.submit.pack(pady=5)

    def bth_click(self):
        # print("버튼 눌림")
        # self.entry에서 값을 가져온다.
        self.data = self.entry.get()
        # 값이 잘 가져와지는지 확인한다.(출력)
        # print(self.data)
        # -> self.data에 담는다.
        # self.labell1에 그 값을 전달한다.
        self.labell1.config(text=self.data)
        pass

if __name__=="__main__":
    obj = GUI_practice()