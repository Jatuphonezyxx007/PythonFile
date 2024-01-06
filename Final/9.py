while True:
    try:
        num=int(input("Input Number :"))
        if num <=0:
            break
        for i in range (1,6):
            print(num,"x",i,"=",num*i)

    except ValueError:
        print("Please enter an integer number")
