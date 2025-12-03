age = int(input("Enter your age: "))
degree = input("Do you have a degree? (yes/no): ").strip().lower()
experience = int(input("Enter your years of experience: "))

if age >= 18:
    if degree == 'yes':
        if experience > 3:
            eligibility = "Highly Eligible."
        elif experience >= 1 and experience <= 3:
            eligibility = "Eligible"
        else:
            eligibility = "Under Review."
    else:
        eligibility = "Degree required."
else:
    eligibility = "Not eligible."

print("Your application status is:", eligibility)
