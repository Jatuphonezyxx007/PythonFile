total=0
for i in range(1,5+1):
    strPromt="Input Number#"+str(i)+":"
    number=eval(input(strPromt))
    total=total+number
print("."*5)
print("Total Score = {0:,.2f}".format(total))
print("Average Score = {0:,.2f}".format(total/i))
