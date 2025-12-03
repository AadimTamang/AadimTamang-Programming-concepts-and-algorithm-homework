print("Welcome to the Haunted House")

direction = input("Which direction do you want to go? (upstairs or downstairs): ").lower()
if direction == "downstairs" or "downstair":
    print("Game Over! you fell into a pit.")
else:
    choice = input("You see a Door. Do you want to enter the room or stay out (enter/stay): ").lower()
    if choice == "enter":
        print("Game Over! A ghost caught you.")
    else:
        choice2 = input("You meet a ghost, vampire and a warewolf Who do you approach? ").lower()
        if choice2 == "ghost":
            print("Game Over! The ghost scared you to death.")
        elif choice2 == "vampire":
            print("Game Over! The vampire sucked your blood.")
        elif choice2 == "warewolf":
            print("You win!! The warewolf showed you the way out of the house.")
        else:
            print("Game Over! You hesitated too long and got lost in the house.")