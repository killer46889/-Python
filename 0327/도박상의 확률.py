도박상의 확률

어떤사람이50달러를가지고라스베가스에서게임을한다고하자. 한번의
게임에1달러를건다고가정하자. 돈을딸확률은0.5이라고가정하자. 한번
라스베가스에가면, 가진돈을다잃거나목표금액인250달러에도달할때
까지게임을계속한다. 어떤사람이라스베가스에100번을갔다면몇번이나
250달러를따서돌아올수있을까?

importrandom
initial_money = 50
goal = 250
wins = 0
for i in range(100) : # 라스베가스에100번간다.
cash = initial_money
whilecash > 0and cash < goal : # 돈이0이거나250불을따면반복중단
number = random.randint(1, 2)
ifnumber == 1: 
cash = cash + 1 # $1을딴다.
else:
cash = cash -1 # $1을잃는다.
ifcash == goal : wins = wins + 1
print("초기금액$%d"% initial_money)
print("목표금액$%d"% goal)
print("100번중에서%d번성공"% wins)
