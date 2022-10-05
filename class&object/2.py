#직원을 나타내는 클래스 Employee를 정의합니다.
class Employee:
    # 전체 직원의 수는 클래스 변수인 empCount에 저장합니다.
    empCount= 0
    # 이름(nmae)과 월급(salary)를 인스턴스 변수로 가지는 생성자를 만듭니다.
    def __init__(self,name, salary):
        self.name=name
        self.salary=salary
        #직원이 생길 때 마다 empCount를 1씩 증가시키게 하여 전체 직원수를 empCount에 저장합니다. 
        Employee.empCount +=1
        
    #현재까지 존재하는 employee의 수를 나타내는 displayCount라는 method를 만듭니다.
    def displayCount(self):
        return Employee.empCount
     
    #해당 employee 객체의 정보를 출력해주는 displayEmployee라는 method를 만듭니다.
    def displayEmployee(self):
        return self.name, self.salary


