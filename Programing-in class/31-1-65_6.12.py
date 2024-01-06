Deposit = float(input("Enter amount deposited:"))
Rate = float(input("Enter annual rate of interate (1-100%):"))
monthlyrate = (Rate/100)/12
print("{0:^6s} {1:>12s}".format("Month","Balance"))
for Quarter in range(3,13,3):
    print("{0:>3} {1:>15,.2f}".format(Quarter, Deposit*(1+monthlyrate)**Quarter))
