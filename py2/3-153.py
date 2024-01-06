tct = input("Enter type of transaction [D=Deposit] or [W=Withdrawal] :")
if "D" in tct:
    balan = float(input("Enter balance :"))
    depo = float(input("Enter amount deposit :"))
    total=balan+depo
    print("Your balance is {0:,.2f} Baht".format(total))
elif "W" in tct:
    balan = float(input("Enter balance :"))
    withdraw = float(input("Enter amount withdrawal :"))
    total=balan-withdraw
    print("Your balance is {0:,.2f} Baht".format(total))
else:
    print("Input invalid type of transaction.")
