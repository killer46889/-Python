숫자 맞추기 게임

importrandom
tries = 0 # 시도횟수
guess = 0; # 사용자의추측값
answer = random.randint(1, 100) # 1과100사이의난수
print("1부터100 사이의숫자를맞추시오")
whileguess != answer:
guess = int(input("숫자를입력하시오: "))
tries = tries + 1
ifguess < answer:
print("너무낮음!")
elifguess > answer:
print("너무높음!")
ifguess == answer:
print("축하합니다. 시도횟수=", tries)
else:
print("정답은", answer)
