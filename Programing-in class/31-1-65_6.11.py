qty=int(input("Input Internet User :"))
print("{0:10} {1}".format("Year","Internet Usage"))
for year in range(2560,2568):
    if year==2565:
        print("*"*50)
    print("{0:<10d} {1:,d}".format(year,round(qty)))
    if year==2565:
        print("*"*50)
    qty+= 0.04*qty
