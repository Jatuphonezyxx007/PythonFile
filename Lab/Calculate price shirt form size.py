size=input("Input Size :")
startrate=500
if "S" in size:
    qty=int(input("Input Qty :"))
    rate=startrate
    total=rate*qty
    print("Price Rate is {0:,d}".format(rate))
    print("Total Price is {0:,.2f} Baht".format(total)) 
elif "M" in size:
    qty=int(input("Input Qty :"))
    rate=startrate+50
    total=rate*qty
    print("Price Rate is {0:,d}".format(rate))
    print("Total Price is {0:,.2f} Baht".format(total))
elif "L" in size:
    qty=int(input("Input Qty :"))
    rate=startrate+100
    total=rate*qty
    print("Price Rate is {0:,d}".format(rate))
    print("Total Price is {0:,.2f} Baht".format(total))
else:
    print("Please Enter Size only S, M or L")
exit()