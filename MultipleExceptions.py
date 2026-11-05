try:
    num1, num2 = eval(input("Enter two numbers, seperated by a Coma: "))
    result = num1 / num2
    print("Result is: ", result)

except ZeroDivisionError: 
    print("Division by Zero is an Error")

except SyntaxError:
    print("Comma is missing. Enter numbers Seperated by a Comma")

except:
    print("Wrong Input")

else:
    print("No Exceptions")

finally:
    print("This will Execute no matter what")
    