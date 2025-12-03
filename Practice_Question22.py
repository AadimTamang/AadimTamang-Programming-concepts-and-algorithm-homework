print("Welcome to the Magic Forest")

direction = input("Which direction do you want to go? (north or south): ").lower()
if direction == "south":
    print("Game Over! You fell into a pit.")
else:
    choice = input("You see a river. Do you want to cross the river or follow the path (swim/follow): ").lower()
    if choice == "swim":
        print("Game Over! You were eaten by a crocodile.")
    else:
        choice2 = input("You meet a fairy, ogre and an elf. Who do you approach? ").lower()
        if choice2 == "ogre":
            print("Game Over! The ogre was hungry.")
        elif choice2 == "fairy":
            print("Game Over! The fairy turned you into a frog.")
        elif choice2 == "elf":
            print("You win!! The elf showed you the way out of the forest.")
        else:
            print("Game Over! You hesitated too long and got lost in the forest.")