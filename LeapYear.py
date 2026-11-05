year = int(input("Enter a Year: "))

def leap_year(year):
    if year % 4 == 0:
        print("The year you have entered is a leap year")
    else:
        print("The Year you have Entered is not a Leap year")

leap_year(year)
   