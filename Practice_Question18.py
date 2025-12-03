score = int(input("Enter your score: "))

if score >= 90:
    print("Congratulations!")
elif score >= 50 and score < 90:
    print("There is room for improvement.")
else:
    print("retake the exam.")