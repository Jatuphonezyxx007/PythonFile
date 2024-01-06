price = float(input("Enter total price :"))
if price>1000 and price<=5000:
    discount=price*5/100
elif price>5000 and price<=10000:
    discount=price*10/100
elif price>10000:
    discount=price*20/100
net=price-discount
print("Discount is {0:,.2f} Baht".format(discount))
print("Net price is {0:,.2f} Baht".format(net))
