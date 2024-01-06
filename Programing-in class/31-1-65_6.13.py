while True:
    number=int(input("Input number :"))
    if number==0:
        break
    for i in range(1,12+1):
        print(number," x ",i, "=",i*number)
