사용자입력검증하기

##
#이프로그램은사용자의입력을검증한다. 
#
print("========================")
print("메뉴1번: 치즈버거")
print("메뉴2번: 치킨버거")
print("메뉴3번: 불고기버거")
print("========================")
selection = int(input("메뉴를선택하세요:"))
ifselection >= 1and selection <= 3:
print("메뉴", selection)
else:
print("잘못입력하셨습니다.")
