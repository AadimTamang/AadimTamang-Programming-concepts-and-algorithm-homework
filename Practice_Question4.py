age = int(input("Enter your age: "))
membership_card = input("Do you have a membership card? (yes/no): ").strip().lower()

if age > 12:
    if age >= 12 and age <= 60:
        if membership_card == 'yes':
            amount = 150
        else:
            amount = 200
    else:
        amount = 100
else:
    amount = 0

print("The ticket price is:", amount)