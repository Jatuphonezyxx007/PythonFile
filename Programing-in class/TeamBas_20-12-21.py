TeamName = input ("Enter name of team :")
lost = int(input("Enter number of games lost :"))
won = int(input ("Enter number of games won :"))
Total = lost+won
PerWon = won*100/Total
print (TeamName,"won",round(PerWon,2),"% of their games.")
