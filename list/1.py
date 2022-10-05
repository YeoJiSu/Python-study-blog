#reverseList() 함수를 정의합니다.
def reverseList():
    #예시 답안을 토대로 정수list를 생성합니다.
    a=[10,20,30,40,50]
    #a 라는 정수 list의 길이를 계산합니다.
    b=len(a)
    #비어있는 리스트 c를 생성하고, append를 이용하여, a라는 list에 있는 값을 '뒤에서부터' 차례대로 추가합니다.
    c=[]
    for i in range(b-1,-1,-1):
        c.append(a[i])
    #c에는 초기의 정수리스트가 역순으로 저장되어있으므로 이를 출력합니다.
    print(c)
#마지막으로, 함수를 호출합니다.
reverseList()
