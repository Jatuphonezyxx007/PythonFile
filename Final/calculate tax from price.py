def SetTax(score,vat):
    return score*vat/100
#end function

number = float(input("Input Number:"))
num_vat = float(input("Input Vat(%) :"))
value_vat = SetTax (number ,num_vat)
strType = input("Input (+ for add to Number) or (- for remove from Number) :")
if strType=="+":
    total_number = number+value_vat
    print("Total Number = {0:,.2f} Baht".format(total_number))
elif strType=="-":
    total_number = number-value_vat
    print("Total Number = {0:,.2}) Baht".format(total_number))
else:
    print("Can not detect your operation")
