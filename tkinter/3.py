#tkinter 모듈을 불러옵니다.
from tkinter import *
#루트 윈도우를 생성합니다.
window=Tk()
 
#show라는 버튼을 클릭했을 때 입력 받은 데이터를 출력할 수 있도록 show라는 함수를 생성합니다.
def show():
    print("이름: %s  \n나이: %s  \n국적: %s" % (e1.get(), e2.get(), e3.get()))
 
#이름, 직업, 국적이 적힌 Label을 생성하고 예제와 같이 '0'번 째 열에 세로 방향으로 각각을 생성시킵니다.
Label(window, text="이름").grid(row=0,column=0,pady=5,padx=5,stick=W)
Label(window, text="직업").grid(row=1,column=0,pady=5,padx=5,stick=W)
Label(window, text="국적").grid(row=2,column=0,pady=5,padx=5,stick=W)
 
#command매개변수를 이용하여 버튼을 클릭했을 때 함수가 실행되도록 버튼을 생성하고, grid를 이용해 위치와 간격을 정해줍니다.
b1=Button(window, text="Show", command=show).grid(row=3, column=0,sticky=W, pady=5,padx=5)
#"Quit"버튼을 누르면 프로그램이 종료되도록 합니다.
b2=Button(window, text="Quit",command=window.quit).grid(row=3, column=1, sticky=W, pady=5,padx=3)
 
#예제를 보면 "Quit"이 존재하는 '1'번 째 열과 데이터를 입력받는 열 사이에 간격이 띄워져있으므로 Label을 이용하여 그 사이 간격을 띄워줍니다.
i=0
for i in range(2):
    Label(window, text="   ").grid(row=i,column=2)
    i=i+1
 
#데이터를 입력받을 수 있도록 Entry를 이용하여 생성시켜주고, grid를 이용해 위치와 간격을 정해줍니다.    
e1=Entry(window)
e2=Entry(window)
e3=Entry(window)
e1.grid(row=0, column=3, padx=5)
e2.grid(row=1, column=3, padx=5)
e3.grid(row=2, column=3, padx=5)
#화면에 윈도우가 나타나도록 메인 루프에 진입시켜줍니다.
window.mainloop()
