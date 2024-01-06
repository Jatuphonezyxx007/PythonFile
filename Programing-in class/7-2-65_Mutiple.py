def MultipleTable(num):
    for i in range(1,13):
        print("{0} x {1} = {2}".format(num,i,num*i))
number=int(input("Enter a number :"))
MultipleTable(number)
