data=[]
student=int(input("Enter number of students :"))
for i in range(1,student+1):
    name=input("Input name :")
    data.append(name)
print("-"*20)
print("Your student data")
for strName in data:
    print(strName)
