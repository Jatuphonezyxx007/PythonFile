price=int(input("Input price :"))
if price>100:
    dis=price*10/100
else:
    dis=0

net_pay=price-dis
print("Price:{0:,.2f} Baht".format(price))
print("Discount:{0:,.2f} Baht".format(dis))
print("Net Payment {0:,.2f} Baht".format(net_pay))
