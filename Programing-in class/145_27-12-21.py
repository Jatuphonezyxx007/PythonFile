weight = float(input("INPUT Your weight (kg.) :"))
height = float(input("INPUT Your height (m.) :"))
BMI = weight/height**2
print("Your BMI is {0:.2f}".format(BMI))
if BMI<18.5:
    print("You are underweight.")
elif BMI>18.5 and BMI<25:
    print("You are normal.")
elif BMI>=25 and BMI<30:
    print("You are overweight.")
elif BMI>30:
    print("You are obese.")
