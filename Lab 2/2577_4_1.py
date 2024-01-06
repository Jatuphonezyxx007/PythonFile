while True:
    try:
        start=int(input("Enter start number : "))
        stop=int(input("Enter stop number : "))
        if start>stop :
            print("กรุณากรอกตัวเลข Start number ให้น้อยกว่า Stop number")
        else:
            for i in range (start,stop+1):
                print("Loop",i)
            break
    except:
        print("กรุณากรอกเฉพาะตัวเลขเท่านั้น")
