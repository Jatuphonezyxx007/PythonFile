num=20
print("{0:20} {1:30}".format("Celsious","Fahrenheit"))
while num<=50:
    f=(9/5*num)+32
    print("{0:<20} {1:<30}".format(num,f))
    num+=5
