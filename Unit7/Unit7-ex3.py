def CelcuVat (number,vat):
    Total_Vat = number*vat/100
    return Total_Vat
Number = int(input("Input Number : "))
Tax = int(input("Input Vat : "))
Total = CelcuVat(Number,Tax)
print("Value Vat = {0:,.2f}".format(Total))
