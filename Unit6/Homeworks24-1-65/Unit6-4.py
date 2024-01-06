money=1338000
print("Rental balance = {0:,.2f} Baht".format(money))
print("{0:20} {1:30}".format("YEAR","Balance End of Year"))
year=2561
while year<=2565:
    money-=12*22300
    print("{0:<20} {1:,.2f} {2}".format(year,money,"Baht"))
    year+=1
