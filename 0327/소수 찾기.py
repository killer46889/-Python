소수 찾기

2부터시작하여50개의소수를 찾는 프로그램

N_PRIMES = 50# 찾아야하는소수의개수
number = 2# 2부터시작한다.
count = 0
whilecount < N_PRIMES :
divisor = 2# 나누는수는2부터시작하여하나씩증가한다.
prime = True
whiledivisor < number :
ifnumber % divisor == 0: # 나누어지면소수가아니다.
prime = False
break;
divisor += 1
ifprime: # 소수이면소수개수를증가하고출력한다.
count += 1
print(number, end=" ")
number += 1# 다음수로간다

