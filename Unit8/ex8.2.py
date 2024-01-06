while True :
    try:
        price = float(input("Enter the price of product : "))
        if price == 0:
            break
        qty = int(input("Enter quantity : "))
        total = price * qty
        print("Total price is {0:,.2f} baht".format(total))
    except ValueError as errText1:
        print("Problem : ",errText1)
    except TypeError as errText2:
        print("Problem : ",errText2)
