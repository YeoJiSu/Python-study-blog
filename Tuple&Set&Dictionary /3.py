#우선 table이라는 빈 딕셔너리를 만듭니다.
table= dict()
#while True를 이용하여 입력모드의 이름 입력란에 공백이 생길 때까지 무한반복합니다.
while True:
    name=input("(입력모드)이름을 입력하시오:")
    if name== '':
        break
    else:
        num=input("전화번호를 입력하시오:")
    #입력모드에서 입력받은 이름과 전화번호를 각각 name과 num에 저장하고, 이를 table 딕셔너리에 각각 key와 value로 저장해둡니다.
    table[name] = num
#검색모드 또한 마찬가지로 검색모드의 이름 입력란에 공백이 생길 때까지 무한반복합니다.
while True:
    name= input("(검색모드)이름을 입력하시오:")
    #입력한 이름이 table의 key안에 있다면 그 value를 말하도록 프린트합니다.
    if name in table:
        print( name, "의 전화번호는", table[name], "입니다.")
    elif name=='':
        break
    else:
        print("존재하지 않는 이름입니다.")
