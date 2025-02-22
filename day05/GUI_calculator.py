import tkinter as tk

class Calc():
    def __init__(self,root:tk.Tk=None):
        self.root=root or tk.Tk()
        self.formula=""
        self.settings()
        
    def settings(self):
        self.root.title("나만의 계산기")
        self.width,self.height=200,250
        self.root.geometry(f"{self.width}x{self.height}")

        # 상단의 계산중, 계산결과를 보여줄 display 위젯 배치
        # display 위젯을 배치할 상단 frame 생성
        self.upper_frame =tk.Frame(self.root)

        # display 위젯 만들기
        # 나중에 높이 키우기 !!
        self.display= tk.Label(self.upper_frame,width=20,font=('Arial',16))
        # self.display.place(height=20)
        self.display.pack()

        # display에 값을 입력하지 못하도록
        # readonly로 설정
        self.display.config(state="active")

        # 상단 프레임 루트 윈도우에 배치
        self.upper_frame.pack()

        # 버튼들이 들어갈 중단 프레임 생성
        self.mid_frame =tk.Frame(self.root)
        self.mid_frame.pack()

        # 기타 항목이 들어갈 하단 프레임 생성
        self.bottom_frame=tk.Frame(self.root)
        self.bottom_frame.pack()

        self.label_test=tk.Label(self.bottom_frame,text="text")
        self.label_test.pack()

        # 숫자와 연산자 버튼 배치
        self.bttns=[
            7, 8,   9,   "/",
            4, 5,   6,   "*",
            1, 2,   3,   "-",
            0,".", "=",  "+"
        ]
        # 그리드의 행과 열을 정하기 위한 변수 선언
        row,col=0,0 # 시작 행렬
        # (반복문)버튼 생성
        for bttn_text in self.bttns:
            # 버튼 위젯 생성
            # lambda를 이용하여 각 버튼마다 텍스트를 다르게 설정
            button= tk.Button(
                self.mid_frame,
                text=str(bttn_text),
                width=5,
                height=2,
                command=lambda x=bttn_text: self.button_click(x)
            )
            # 버튼을 그리드에 배치
            button.grid(row=row,column=col,padx=2,pady=2)
            col += 1
            # 4열까지 배치했으면 다음 행으로 이동
            if col > 3 :
                col=0
                row+=1
    def button_click(self,value):
        # 전달받은 값은 문자열로 처리
        value=str(value)
        # print(value)
        if not self.formula: 
            self.formula=""
        if value != "=":
            # 전달받은 값이 =이 아니라면
            # 전달받은 값을 self.formula에 +로 문자열 연결
            self.formula += value
            # 현재 계산중인 내용을 display에 출력
            self.display.config(text=self.formula)
        else:   # =을 입력받은 경우
            # self.formula의 값을 self.display의 text로 전달
            # eval을 통해 전달받은 계산식(formula)룰 계산한 후
            self.result=eval(self.formula)
            # 그 결과를 display의 text로 설정
            self.display.config(text=self.formula)
            self.formula=str(self.result) # 계산식 초기화


        # 버튼을 눌렀을 때, 모두 같은 함수를 실행
        # 누른 버튼이 무엇인지 전달
        # =을 제외한 나머지 버튼은 버튼의 문자를
        # self.formula 변수에 +로 문자열 연결
        pass

if __name__=="__main__":
    obj=Calc()
    obj.root.mainloop()