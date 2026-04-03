이분법

구간[a, b]에서f(a)f(b) < 0이라고 하자. f(a)f(b) < 0이면 함수 f는 반드시 구간
[a,b]에서 근을 가져야한다. 계속해서a와b의중간값m=(a+b)/2을계산하고
, 함수 f(m)의 값을계산한다.
f(a)f(m) < 0이면 근은 [a, m] 사이에 있고, 그렇지 않으면근은[m, b] 구간에
있을것이다

def f(x):
return(x**2-x-1)
defbisection_method(a, b, error):
if f(a)*f(b) > 0:
print("구간에서근을찾을수없습니다.")
else:
while(b -a)/2.0> error: # 오차를계산한다. 
midpoint = (a + b)/2.0 # 중점을계산한다. 
if f(midpoint) == 0:
return(midpoint) 
eliff(a)*f(midpoint) < 0: 
b = midpoint
else:
a = midpoint
return(midpoint)
answer = bisection_method(1, 2, 0.0001)
print("x**2-x-1의근:", answer)



