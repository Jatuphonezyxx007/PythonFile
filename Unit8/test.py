try:
    n = int(input("Enter a score, or -1 to exit: "))
    total=0
    count_loop=0
    while n!=-1:
        total+=n
        n = int(input("Enter a score, or -1 to exit: "))
        count_loop+=1
    average = total/count_loop
    print("number of student is",count_loop)
    print("average number is {0:,.2f}".format(average))
except:
    print("Please Enter a number only")
