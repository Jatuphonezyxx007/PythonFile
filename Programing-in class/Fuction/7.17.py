import lib_total
price=float(input("Enter price :"))
qty=int(input("Enter Quantity :"))
Total=lib_total.TotalPrice(qty,price)
print("Total Price = {0:,.2f} Baht".format(Total))
lib_total.ShowLine(20)
