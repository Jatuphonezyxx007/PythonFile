fv = int(input("Enter future value :"))
rate = int(input("Enter interest rate (as %) :"))
year = int(input("Enter number of years :"))
pv =fv/(1+rate/100)**year
print ("Present value: {0:,.2f} Baht".format(pv))
