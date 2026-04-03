초등생을 위한 산수 문제 발생기

importrandom
flag = True
whileflag:
x = random.randint(1, 100)
y = random.randint(1, 100)
answer = int(input(f"{x} + {y} = "))
ifanswer == x + y:
print("정답입니다.")
else:
print("틀렸습니다.")
flag = False
