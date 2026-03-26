산술 퀴즈프로그램

##
#이프로그램은산수문제를출제한다.  
#
importrandom
x = random.randint(1, 100)
y = random.randint(1, 100)
answer = int(input(f"{x} + {y} = "))
# 부울변수에결과를저장하고출력한다. 
flag = (answer == (x+y))
print(flag)
