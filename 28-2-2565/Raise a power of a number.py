i=0
while True:
    try:
        start=int(input("Enter number start : "))
        if start==0:
            print("Thank you")
            break
        stop=int(input("Enter number stop : "))
        if start>stop :
            print("กรุณากรอกค่าเริ่มต้นไม่เกินค่าที่มากที่สุด")
        for i in range (start,stop+1):
            velue=i**2
            print(i, "ยกกำลัง 2 ได้ {0:,}".format(velue))
    except:
        print("กรุณากรอกเฉพาะตัวเลขเท่านั้น")
    
