land=4347826.09
print("{0:20} {1:30}".format("Year","Land Value"))
year=2561
while year<=2566:
    land+=land*0.15
    print("{0:<20} {1:,.2f}".format(year,land))
    year+=1
