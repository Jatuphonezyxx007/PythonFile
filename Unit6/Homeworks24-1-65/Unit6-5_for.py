land=5000000
print("{0:20} {1:30}".format("Year","Land Value"))
for year in range(2561,2567):
    print("{0:<20} {1:,.2f}".format(year,land))
    land+=0.15*land
