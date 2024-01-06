salary = int(input("Enter your salary :"))
percent = int(input("Enter increase of percentage (%) :"))
net = salary*percent/100
print ("Your receive more salary is {0:,.2f} Baht".format(net))
print ("Your net salary is {0:,.2f} Baht".format(salary+net))
