#문자열을 입력 받아 name애 저장합니다.
name=input("문자열을 입력하시오:")
#각 문자를 list2에 담습니다.
list2= list(name)
#list2의 길이를 a라고 둡니다.
a=len(list2)
#문자열을 전화기의 숫자키로 변환하는 함수 adf()를 정의합니다.
def adf():
#우선 빈 리스트 list3를 만듭니다.
    list3=[]
    #사용자로부터 입력받은 문자열에 대해 list2의 0번째 자리부터 차례대로 숫자로 바꾸고 이 숫자를 list3에 하나하나씩 추가합니다.
    for i in range(a):
        if list2[i]in "ABC":
            list3.append("2")
        elif list2[i]in"DEF":
            list3.append("3")
        elif list2[i]in"GHI":
            list3.append("4")
        elif list2[i]in"JKL":
            list3.append("5")
        elif list2[i]in"MNO":
            list3.append("6")
        elif list2[i]in"PQRS":
            list3.append("7")
        elif list2[i]in"TUV":
            list3.append("8")
        elif list2[i]in"WXYZ":
            list3.append("9")
        else:
            list3.append(list2[i])
    #for 문을 이용해 완성된 list3안의 숫자를 출력하도록합니다.
    for i in range(a):
        print(list3[i],end='')
#adf()를 출력합니다.
adf()

