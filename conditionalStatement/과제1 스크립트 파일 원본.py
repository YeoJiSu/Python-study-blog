#근무시간을 변수x로 받습니다.
x=int(input("근무시간을 입력하시오: "))
#시간당 임금은 변수 y로 받습니다.
y=int(input("시간당 임금을 입력하시오: "))

#총임금은 변수 z로 받습니다.
#근무시간이 40시간보다 같거나 작으면 시간당 임금은 y로 한결 같으므로 총임금z=x*y가 됩니다.
if x<=40:
    z=x*y
#근무시간이 40시간을 넘어버리면 40시간까지는 시간당 임금이 y이지만 그 이후부터는 시간당 임금이 y*1.5가 되므로 총임금 z=40*y+(x-40)*(y*1.5)가 됩니다.
else:
    z=40*y+(x-40)*(y*1.5)

#마지막에 총임금을 말하도록 프린트합니다.
print("총임금은 ",z)
