def CheckScore(Number):
    if Number<50:
        return False
    else:
        return True
score = float(input("Input Score: "))
if CheckScore(score):
    print("Your score is pass")
else:
    print("Your score is fail")
