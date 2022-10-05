class BankAccount(object):
    #클래스 변수는 interest_rate 입니다.
    interest_rate=0.3
    #인스턴스 변수는 name, number, balance 입니다.
    def __init__(self, name, number, balance):
        self.name=name
        self.number=number
        self.balance=balance
        return
    #잔고를 증가시키는 deposit()메소드를 추가합니다. 추가할 금액을 임의의 수 5 로 지정하여 잔고에 더하도록 합니다.
    def deposit(self,amount=5):
        self.balance += amount
        return self.balance
    #잔고를 감소시키는 withdraw()메소드를 추가합니니다. 뺄 금액을 임의의 수 5로 지정하여 잔고에서 빼도록 합니다.
    def withdraw(self,amount=5):
        self.balance -= amount
        return self.balance

