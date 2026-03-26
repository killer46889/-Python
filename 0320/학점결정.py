학점결정

# 성적을받아서학점을결정하는프로그램
score가80이상, 90미만인경우
score = int(input("성적을입력하시오: "))
ifscore >= 90:
print("학점A")
elifscore >= 80:
print("학점B")
elifscore >= 70:
print("학점C")
elifscore >= 60:
print("학점D")
else:
print("학점F")