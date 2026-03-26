BMI 계산하기

##
#
이프로그램은BMI를계산한다. 
#
weight = float(input("몸무게를 kg 단위로 입력하시오: "))
height = float(input("키를 미터 단위로 입력하시오: "))
bmi = (weight / (height**2)) 
print("당신의 BMI=",  bmi)