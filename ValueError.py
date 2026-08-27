try:
    number = int(input("Enter a Number:"))
    print("The Number Entered is:", number)

except ValueError as ex:
    print("Exception:", ex)
    