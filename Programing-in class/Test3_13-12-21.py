strID = input("Enter your student ID :")
print ("Your student ID is",strID)
strName = input("Enter your name :")
position = strName.rfind(" ")
print ("Your last name is :",strName[position+1:])
print ("Your first name is :",strName [:position])
