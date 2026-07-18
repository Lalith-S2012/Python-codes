print("Hello, select your ride:")
print("1. Bike")
print("2. Car")

choice = input("Enter your Choice: ").strip().lower()

if choice == "1" or choice == "bike":
    print("What kind of Bike")
    print("1. Scooty")
    print("2. Scooter")

    choice2 = input("Enter your second Choice: ").strip().lower()
    if choice2 == "1" or choice2 == "scooty":
        print("You Have Selected Scooty")
    else:
        print("You have selected Scooter")

elif choice == "2" or choice == "car":
    print("What type of car? ")
    print("1. Sedan")
    print("2. SUV")

    choice3 = input("Enter your third Choice: ").strip().lower()

    if choice3 == "1" or choice3 == "sedan":
        print("You have selected Sedan")
    elif choice3 == "2" or choice3 == "suv":
        print("You have Chose SUV")
    else:
        print("Wrong Choice :) ")

else:
    print("Wrong Choice :) ")
