age = int(input("Enter your age: "))
gender = input("Enter your gender(m or f): ").strip().lower()

if age >= 18 and age < 30:
    if gender == 'm':
        wage = 700
    else:
        wage = 750
elif age >= 30 and age <= 40:
    if gender == 'm':
        wage = 800
    else:
        wage = 850
else:
    print("Not eligible for the job.")
    wage = None

print("The monthly wage is:", wage)