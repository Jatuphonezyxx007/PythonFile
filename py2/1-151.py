land = eval(input("Enter Land value :"))
fee = land*5/100
if fee<=500:
    vat=500
    print ("Your fee is {0:,.2f} Baht".format(vat))
else:
    if fee>500:
        print ("Your fee is {0:,.2f} Baht".format(fee))
