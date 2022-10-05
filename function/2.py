#우선, 점수에 따라 달라지는 성적을 반환하는 함수 getGrade(score)을 정의합니다.
def getGrade(score):
    if score>=90:
        return("A")
    elif score<90 and score>=80:
        return("B")
    elif score<80 and score>=70:
        return("C")
    elif score<70 and score>=60:
        return("D")
    else:
        return("F")
# 사용자로부터 점수를 입력 받습니다.
score=int(input("점수를 입력하세요: "))
# 함수를 불러와서 그 점수에 따른 성적을 얻습니다.
grade=getGrade(score)
# 그리고 그 점수의 성적을 출력합니다.
print("성적은",grade, "입니다")
    
