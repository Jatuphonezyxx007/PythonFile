try:
    price = float(input("Enter the price of product:"))
    qty = int(input("Enter quantity:"))
    total = price * qty
except:
    print("Input Error number")
else:
    print("Total price is {0:,.2f} baht".format(total))
finally:
    print("End of Program")
