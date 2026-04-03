구조화프로그래밍실습

defmenu() :
print("1. 섭씨온도->화씨온도")
print("2. 화씨온도->섭씨온도")
print("3. 종료")
selection = int(input("메뉴를선택하세요: "))
returnselection
defctof(c) :
temp = c*9.0/5.0+ 32
returntemp
def ftoc(f) :
temp = (f-32.0)*5.0/9.0
returntemp
def input_f() :
f = float(input("화씨온도를입력하시오: "))
returnf

