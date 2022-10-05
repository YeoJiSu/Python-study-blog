#Rectangle이라는 class를 정의합니다.
class Rectangle:
#사각의 위치 x,y 와 폭 width 와 높이 height를 인스턴스 변수로 둡니다.
    def __init__(self,x,y,width,height):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
    #사각형의 넓이를 반환하는 calcArea()를 정의합니다.
    def calcArea(self):
        return self.width*self.height
    #예시 박스처럼 결과가 나오도록 결과값을 반환합니다.
    def __str__(self):
        return '(%d,%d)%d,%d ' % (self.x,self.y,self.width,self.height)
#위치가 (0,0)이고 크기가 (100,100)인 Rectangle 객체를 생성합니다.
A1=Rectangle(0,0,100,100)
#위치가 (10,10)이고 크기가 (200,200)인 Rectangle 객체를 생성합니다.
A2=Rectangle(10,10,200,200)
# 각 사각형의 위치, 폭과 높이를 출력합니다.
print("box:",A1)
print("box:",A2)
