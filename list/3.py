# 우선 지뢰의 List를 '10X10크기의 모양'으로 출력해 낼 함수 printList(a)를 정의합니다. 여기서 a에는 list가 올 것입니다.
def printList(a):
#여기서 i는 행, k는 열을 의미합니다.
    for i in range(len(a)):
        for k in range(len(a[0])):
            print(a[i][k], end=" ")
        print()
# 우선 빈 list인 table을 만듭니다.
table= []
#table을 '0이 10개 들어 있는' list를 10개 가진 list로 만듭니다.
for i in range(10):
    table=table+[[0]*10]

#0부터 1까지의 난수를 발생시켜 table 속 0들을 난수로 바꾸어줍니다.
#i는 행,k는 열을 의미합니다.
for i in range(10):
    for k in range(10):
        from random import *
        b = random()
        table[i][k]=b

#어느 칸이 지뢰일 확률이 0.3이 되려면, 난수가 0.3보다 적은 경우 그 칸을 지뢰로 바꾸면 됩니다.
#i는 행,k는 열을 의미합니다.
for i in range(10):
    for k in range(10):
        if table[i][k]<0.3:
            table[i][k]="#"
        else:
            table[i][k]="."
        
#printList 함수를 호출하여 table을 출력합니다.
printList(table)
