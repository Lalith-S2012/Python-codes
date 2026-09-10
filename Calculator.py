def add(a, b):
    add1 = a + b
    return add1

def sub(a, b):
    sub1 = a - b
    return sub1

def mult(a, b):
    mult1 = a * b
    return mult1

def div(a, b):
    try:
        div1 = a / b
        return div1
    except ZeroDivisionError:
        print("You Cannot Divide a number by Zero!")

while True:    
    try:
        a = int(input("Enter a number: "))
        b = int(input("Enter another Number: "))

        oper = int(input("Enter the number next to the operation you want to operate\n1. addition\n2. subtraction\n3. multiplication\n4. division "))

        if oper == 1:
            print(f"{a} + {b} =", add(a, b))
        elif oper == 2:
            print(f"{a} - {b} =", sub(a, b))
        elif oper == 3:
            print(f"{a} x {b} =", mult(a, b))
        elif oper == 4:
            print(f"{a} / {b} =", div(a, b))
        else:
            print("Invalid Input!")
    
    except ValueError:
        print("Type In a Number!")

    quest = input("Do you want to continue?, type in y for yes and n for no: ")

    if quest == "n":
        break
    else:
        continue
                    

        
    

     












