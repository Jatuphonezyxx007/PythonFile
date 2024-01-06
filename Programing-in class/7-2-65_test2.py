def ShowStars(num):
    for x in range(0,num):
        print("*",end="")
def FaToCel(temp):
    value = (5/9)*(temp-32)
    return value

Fahrenheit = float(input("Enter a Temperature in Fahrenheit :"))
star=int(input("Enter number of star :"))
celsius = FaToCel(Fahrenheit)
ShowStars(star)
print("Celsius = {0:,.2f}".format(celsius))
ShowStars(star)
