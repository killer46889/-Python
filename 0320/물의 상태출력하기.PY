물의 상태출력하기

##
# 이프로그램은온도에따른물의상태를출력한다.
#
temp = float(input("온도를입력하시오: "))
if temp <= 0:
print("물의상태는얼음입니다.")
eliftemp > 0and temp < 100: # 논리연산자를사용한다.
print("물의상태는액체입니다.")
else:
print("물의상태는기체입니다.")
