def grade():
    score = round(float(input("Input Score :")))
    if score in range(0,101):
        if score >=80:
            g="Your grade = A"
        elif score >=70:
            g="Your grade = B"
        elif score >=60:
            g="Your grade = C"
        elif score >=50:
            g="Your grade = D"
        else:
            g="Your grade = F"
    else:
        g="Sorry, Please try again"
    return g
print(grade())
