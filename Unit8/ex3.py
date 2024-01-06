while True:
    gpax=[]
    i=1
    while i<=3:
        try:
            gpa=float(input("Input GPA#"+str(i)+ " : "))
            if gpa>0 and gpa<=4:
                gpax.append(gpa)
                i+=1
            else:
                print("Please enter a number between 0.01 - 4.00")
        except:
            print("Please enter a number of GPA")
    total=sum(gpax)
    avg=sum(gpax)/len(gpax)
    print("You GPAX = {0:,.2f}".format(avg))
    break
