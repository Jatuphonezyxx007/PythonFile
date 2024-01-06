while True:
    try:
        def Celculate (price):
            discount=price*8/100
            return discount
        price=float(input("Enter total price : "))
        if price==0:
            mark="-"*3
            print(mark,"End of Program",mark)
            break
        total=Celculate(price)
        print("Your discount is {0:,.2f} Baht".format(total))
    except:
        print("Please enter a number only")

