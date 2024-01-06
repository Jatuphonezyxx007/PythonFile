def Pay(wage,hours):
    if hours > 30:
        total = (wage*30)+(wage*(hours-30)*2)
    else:
        total = wage*hours
    return total
while True:
    pay_rate = float(input("Enter Pay Rate :"))
    if pay_rate == 0:
        print("End of Program")
        break
    else:
        hourly = float(input("Enter Hours worked :"))
        TotalPay=Pay(pay_rate,hourly)
        print("Earnings: {0:,.2f} Baht".format(TotalPay))
