pv = int(input("Enter principle (pv) :"))
rate = int(input("Enter interest rate (as %) :"))
year = int(input("Enter number of years :"))
fv =pv*(1+rate/100)**year
print ("Future value: {0:,.2f} Baht".format(fv))
