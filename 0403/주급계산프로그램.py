주급계산프로그램

주단위로봉급을받는알바생이있다고하자. 현재시급과일한시간을입력
하면주급을계산해주는함수weeklyPay(rate, hour)를 만들고이함수를호
출하여주급을출력하는프로그램을작성해보자. 30시간이넘는근무시간
에대해서는시급의1.5배를지급한다고하자. 

defweeklyPay( rate, hour ): 
money = 0
if(hour > 30): 
money = rate*30+ 1.5*rate*(hour-30)
else: 
money = rate*hour
returnmoney
rate = int(input("시급입력:"))
hour = int(input("근무시간입력:"))
print("주급은"+ str(weeklyPay(rate, hour)))


