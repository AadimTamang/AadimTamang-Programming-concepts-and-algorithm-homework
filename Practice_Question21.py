balance = 50000
pin = 123 
space = '*' * 20

while True:
    entered_pin = int(input("Enter your PIN: "))

    if entered_pin == pin:
        print("PIN accepted.")
        print(space)
        print("1. Withdraw\n2. Check Balance\n3. Exit")
        print(space)
        choice = int(input("Enter your choice (1-3): "))
        if choice == 1:
            amount = int(input("Enter amount to withdraw: "))
            if amount <= balance:
                balance -= amount
                print(f"Your new balance is: {balance}")
                break
            else:
                print("Insufficient balance.")
                break
        elif choice == 2:
            print(f"Your current balance is: {balance}")
            break
        elif choice == 3:
            print("Thank you for visiting")
            break
        else:
            print("Invalid choice.")
            break
    else:
        print("Incorrect PIN. Access denied.")