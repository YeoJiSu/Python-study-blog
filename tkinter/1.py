#tkinter 모듈을 불러옵니다.
from tkinter import *
#루트 윈도우를 생성합니다.
window= Tk()
#우선 예제처럼 하얀색 바탕의 캔버스를 만듭니다.
canvas= Canvas(window, width=450, height=300, bg="white")
canvas.pack()
 
#각각의 도형, 직선을 생성하는 함수를 만듭니다.
def oval():
    return canvas.create_oval(100,100,300,200)
def rectangle():
    return canvas.create_rectangle(100,100,300,200)
def line():
    return canvas.create_line(100,100,300,200)
#캔버스에 그려진 도형 또는 직선을 모두 삭제하는 함수도 만듭니다.
def clearCanvas():
    return canvas.delete("all")
 
#각각의 버튼을 클릭했을 때 각각의 도형(또는 직선)이 생성되도록 command 매개변수에 각각의 도형(또는 직선)을 생성하는 이벤트를 처리하는 함수를 등록합니다.
#예제에 나와있는 것 처럼 가로 방향의 간격을 띄워줍니다.
b1=Button(window, text="사각형 그리기",command=rectangle).pack(side=LEFT, padx=20)
b2=Button(window, text="타원 그리기",command=oval).pack(side=LEFT, padx=20)
b3=Button(window, text="직선 그리기",command=line).pack(side=LEFT, padx=20)
#마찬가지로, 삭제하기 버튼을 클릭하면 command 매개변수에 '캔버스에 그려진 도형을 모두 삭제하는' clearCanvas 함수를 등록합니다.
b4=Button(window, text="삭제하기",command=clearCanvas).pack(side=LEFT, padx=20)
#화면에 윈도우가 나타나도록 메인 루프에 진입시켜줍니다.
window.mainloop()
