num = int(input("Enter the number of rounds to display:"))
i=1
total=0
while i <= num:
    score=int(input("Enter the number:"))
    total+= score
    i+=1
print("The total number is",total)
print("The average number is",total/num)
