피자 크기 비교하는 프로그램

20cm 피자2개의면적: 2512.0
30cm 피자1개의면적: 2826.0

defmain() : 
print("20cm 피자2개의면적:", get_area(20)+get_area(20))
print("30cm 피자1개의면적:", get_area(30))
## 원의면적을계산한다.
# @paramradius 원의반지름
# @return 원의면적
#
defget_area(radius) :
ifradius > 0:
area = 3.14*radius**2
else:
area = 0
returnarea
main()