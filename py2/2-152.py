balan = input("Enter balance :")
depo = input("Enter amount deposit :")
if balan.isdigit() and depo.isdigit():
    balance=eval(balan)+eval(depo)
    print("Your balance is {0:,.2f} Baht".format(balance))
else:
    print("Input Error Number")
