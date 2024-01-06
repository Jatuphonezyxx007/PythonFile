while True:
    try:
        number=int(input("Input number or enter 0 to exit : "))
        if number >0:
            for i in range (1,12+1):
                print(number, "x", i, "=", number*i)
        elif number ==0:
            print("Thank you for your testing")
            break
        else:
            print("Please enter an integer number")
    except:
        print("Please enter an integer number")
