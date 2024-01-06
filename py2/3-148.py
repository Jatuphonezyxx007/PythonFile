str = """\
Regular = R
Express = X
"""
print(str)
service = input("Choose service :")
weight = float(input("Enter the weight of the parcel [g.] :"))
if "R" in service:
    if weight<1000:
        totalpay=weight*0.3
    elif weight>1000:
        totalpay=(1000*3)+(weight-1000)*0.5
elif "X" in service:
    if weight<1000:
        total=weight*0.3
    elif weight>1000:
        total=(1000*3)+(weight-1000)*0.5
    totalpay=total+100
else:
    print("Please try agin")
print("Total Price :{0:,.2f} Baht".format(totalpay))

