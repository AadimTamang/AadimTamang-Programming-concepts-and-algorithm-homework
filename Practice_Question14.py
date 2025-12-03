earth_weight = float(input("Enter your weight on Earth: "))
planet = int(input("Enter the planet number (1-7): "))

if planet == 1:
    weight = earth_weight * 0.38
    print("Your weight on Mercury is:", weight)
elif planet == 2:   
    weight = earth_weight * 0.91
    print("Your weight on Venus is:", weight)
elif planet == 3:   
    weight = earth_weight * 0.38
    print("Your weight on Mars is:", weight)
elif planet == 4:   
    weight = earth_weight * 2.53
    print("Your weight on Jupiter is:", weight)
elif planet == 5:   
    weight = earth_weight * 1.07
    print("Your weight on Saturn is:", weight)
elif planet == 6:   
    weight = earth_weight * 0.89
    print("Your weight on Uranus is:", weight)
elif planet == 7:   
    weight = earth_weight * 1.14
    print("Your weight on Neptune is:", weight)
else:
    print("Invalid planet number entered.")