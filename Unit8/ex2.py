while True:
    try:
        number=int(input("Enter an integer number (1-100) : "))
        if number <= 100 and number >= 1:
            print("Thank you for your input an integer number that is {0}.".format(number))
            break
        else:
            print("Please enter an integer number.")
    except:
        print("Please enter an integer number.")
