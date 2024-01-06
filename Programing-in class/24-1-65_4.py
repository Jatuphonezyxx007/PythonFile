listdata = [ ]
n = int(input("Enter a score, or -1 to exit: "))
while n!=-1:
    listdata.append(n)
    n = int(input("Enter a score, or -1 to exit: "))
average = sum(listdata)/len(listdata)
print("number of student is",len(listdata))
print("average number is {0:,.2f}".format(average))
