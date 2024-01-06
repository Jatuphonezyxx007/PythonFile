def get_grades():
    marks = round(float(input('Your Current Marks: ')))
    if marks in range(0,101):
        if marks >=90:
            return("Your Grade is: A+")
        elif marks >=86:
            return("Your Grade is: A")
        elif marks >=82:
            return("Your Grade is: A-")
        elif marks >=78:
            return("Your Grade is: B+")
        elif marks >=74:
            return("Your Grade is: B")
        elif marks >=70:
            return("Your Grade is: B-")
        elif marks >=66:
            return("Your Grade is: C+")
        elif marks >=62:
            return("Your Grade is: C")
        elif marks >=58:
            return("Your Grade is: C-")
        elif marks >=54:
            return("Your Grade is: D+")
        elif marks >=50:
            return("Your Grade is: D")
        else:
            return("Your Grade is: F")
    else:
        return("sorry, your input is out of range")
print(get_grades())
