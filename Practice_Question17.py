time = int(input("Enter the time period of service in years: "))
bonus = ''

if time > 10:
    bonus= "10%"
elif time >= 6 and time <= 10:
    bonus= "8%"
elif time < 6:
    bonus= "5%"

print("Your bonus percentage is:", bonus)