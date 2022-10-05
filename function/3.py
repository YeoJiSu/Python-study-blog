#우선, 사용자로부터 두 개의 정수를 입력받습니다.
a=int(input("첫 번째 정수: "))
b=int(input("두 번째 정수: "))
# 유클리드 호제법을 이용하여 최대공약수를 찾는 함수 getGCD를 정의합니다.
def getGCD(a,b):
    if a<b:#먼저, a쪽이 항상 크거나 같도록 해줍니다.
        (a,b)=(b,a)
    while b != 0: # 유클리드 호제법에 의하면 a와 b의 최대공약수는 'b'와 'a를 b로 나눈 나머지'와의 최대공약수와 같기 때문에 나머지가 0이 될 때까지 이 작업을 반복하면 됩니다.
        (a,b)=(b,a%b)
    return a
#최대공약수를 출력합니다.
print(getGCD(a,b))

    