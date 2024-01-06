size=input("Input Size :")
startrate=500
if size=="S" or "s":
    qty=int(input("Input Qty :"))
    rate=startrate
    total=rate*qty
elif "M" in size:
    qty=int(input("Input Qty :"))
    rate=startrate+50
    total=rate*qty
elif "L" in size:
    qty=int(input("Input Qty :"))
    rate=startrate+100
    total=rate*qty
else:
    non="Please Enter Size only S, M or L"
print("Price Rate is {0:,d}".format(rate))
print("Total Price is {0:,.2f} Baht".format(total))
