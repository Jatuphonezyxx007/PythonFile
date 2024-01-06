def CelcuVat (number,vat):
    Total_Vat = number*vat/100
    return Total_Vat
Number = int(input("Input Number : "))
Tax = int(input("Input Vat : "))
Total = CelcuVat(Number,Tax)
print("Value Vat = {0:,.2f}".format(Total))

Mark = input("Input (+ for add to Number) or (- for remove from Number) : ")
if "+" in Mark:
    TotalNum = Number+Total
    print("Total Number = {0:,.2f} Baht".format(TotalNum))
elif "-" in Mark:
    TotalNum = Number-Total
    print("Total Number = {0:,.2f} Baht".format(TotalNum))
else:
    print("Sorry, Please try again")
