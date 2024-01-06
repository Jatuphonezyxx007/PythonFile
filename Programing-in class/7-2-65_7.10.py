def TotalPrice(qty,price):
    sumPrice = qty*price
    return sumPrice

price = float(input("Enter Price :"))
qty = int(input("Enter Quantity :"))
Total=TotalPrice(qty,price)
print("Total Price = {0:,.2f} Baht".format(Total))
