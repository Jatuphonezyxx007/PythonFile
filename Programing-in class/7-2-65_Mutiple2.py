def MultipleTable(num):
    for i in range(1,13):
        print("{0} x {1} = {2}".format(num,i,num*i))
while True:
    number=int(input("Enter a number :"))
    if number == -1:
        print("Thank you for your enjoy.")
        break
    MultipleTable(number)
