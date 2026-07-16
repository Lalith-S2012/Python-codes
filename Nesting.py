print("Hello, select your ride:")
print("1. Bike")
print("2. Car")

choice = input("Enter your Choice: ")
if choice == "1" or choice == "Bike":
    print("What kind of Bike")
    print("1. Scooty\n")
    print("2. Scooter\n")

    choice2 = input("Enter your second Choice: ")
    if choice2 == "1" or choice2 == "Scooty":
        print("You Have Selected Scooty")
    else:
        print("You have selected Scooter")

elif choice == "2" or choice == "Car":
    print("What type of car? ")
    print("1. Sedan")
    print("2. SUV")

    choice3=input("Enter your third Choice: ")

    if choice3== "1" or choice3 == "Sedan":
        print("You have selected Sedan")
    else:
        print("You have Chose SUV")

else:
    print("Wrong Choice :) ")
