sub1 = int(input("Enter marks for subject 1: "))
sub2 = int(input("Enter marks for subject 2: "))
sub3 = int(input("Enter marks for subject 3: "))
sub4 = int(input("Enter marks for subject 4: "))

total = sub1 + sub2 + sub3 + sub4
percentage = (total / 400) * 100

if percentage >= 70:
    grade = 'Distinction'
elif percentage >= 60:
    grade = 'First'
elif percentage >= 40: 
    grade = 'Pass'
else:
    grade = "Fail"

print("Total Marks:", total)
print("Percentage:", percentage)
print("Grade:", grade)