while True:
    try:
        number=int(input("Enter number 5 - 50 only : "))
        if number >=5 and number<=50:
            for i in range (1,12+1):
                print(number, "x", i, "=", number*i)
        elif number == 0:
            print("Thank you")
            break
        else:
            print("กรุณากรอกเป็นเลขจำนวนเต็ม 5 - 50 เท่านั้น")
    except:
        print("กรุณากรอกเป็นเลขจำนวนเต็ม 5 - 50 เท่านั้น")
