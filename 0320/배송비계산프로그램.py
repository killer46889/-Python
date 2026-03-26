배송비계산프로그램

# 사용자로부터상품의가격을입력받는다.  
price = int(input("상품의가격: "))
# 배송비를결정한다. 
if price > 20000:
shipping_cost= 0
else:
shipping_cost= 3000
# 배송비를출력한다. 
print("배송비= ", shipping_cost)