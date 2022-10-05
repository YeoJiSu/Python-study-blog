#우선, 사용자로부터 정수를 입력 받습니다.
asd= input("정수 리스트 입력: ")
#입력 받은 정수를 space를 기준으로 나누어 a 라는 list로 호환합니다.
a=asd.split()
#a 라는 list의 길이를 b라고 둡니다.
b=len(a)
#list 안의 값들의 평균을 계산하는 함수 ave를 정의합니다.
def ave():
    #우선 list 안의 값들의 합계인 sum을 구합니다.
    sum=0
    for i in range(b):
        sum=sum+int(a[i])
    #합계에서 list의 길이를 나누면 평균이 나오므로 이를 반환합니다.
    return sum/b
#함수를 호춣하여 평균을 출력합니다.
print("평균=",ave())
#list 안의 값들의 표준 편차를 계산하는 함수 std를 정의합니다.
def std():
    #list 안의 값들 각각에 평균을 뺀 편차를 제곱해서 이들를 모두 더한 값을 k로 두고, k를 list의 길이로 나오면 분산 var이 나오므로 이를 반환합니다.
    k=0
    for i in range(b):
        k= k + (int(a[i])-ave())**2
    var=k/b
    #표준편차는 분산에 루트를 씌운 값입니다.
    import math
    return math.sqrt(var)
#함수를 호출하여 표준편차를 출력합니다.
print("표준 편차",std())
