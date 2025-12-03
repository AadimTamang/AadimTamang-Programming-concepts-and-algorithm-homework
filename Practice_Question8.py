current_floor = 5
requested_floor = int(input("Enter the floor number you want to go to: "))

if requested_floor > current_floor:
    print("up")
elif requested_floor < current_floor:
    print("down")
else:
    print("You are already on floor", current_floor)