#time 모듈을 불러옵니다.
import time
#tkinter모듈을 불러옵니다.
from tkinter import *
#루트 윈도우를 생성합니다.
window=Tk()
#캔버스를 생성합니다.
canvas= Canvas(window, width=400, height=300)
canvas.pack()
#예제와 같은 text를 생성하고 이를 id라고 둡니다.
id=canvas.create_text(0,150,text="파이썬 커피샵으로 오세요!")
 
#id가 한번 움질일 때 마다 오른쪽으로 3만큼 가도록 둡니다.
for i in range(400):
    canvas.move(id, 3, 0)
    window.update()
    #약간의 지연시간을 0.03초로 둡니다.
    time.sleep(0.03)
#화면에 윈도우가 나타나도록 메인 루프에 진입시켜줍니다.
window.mainloop()
