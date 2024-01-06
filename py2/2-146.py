promotion = input("Enter your package :")
minute = int(input("Enter your minute :"))
if "A" in promotion:
    start=600
    if minute>600:
        extra=(minute-500)*1.50
    else:
        extra=0
elif "B" in promotion:
    start=300
    if minute>200:
        extra=(minute-200)*4
    else:
        extra=0
else:
    print("Please try agian")
total=start+extra
print("Your package :",promotion)
print("Total current charge :{0:,.2f}".format(total))
