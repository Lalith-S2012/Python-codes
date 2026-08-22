def square(a):
    return a*a

def cube(b):
    return b*b*b

def number(x):
    if x % 2 == 0:
        print("The number is Even")
        print("The square of this number is", square(x))
    else:
        print("The number is Odd")
        print("The Cube of this number is", cube(x))

num_1 = int(input("Enter a Number: "))
number(num_1)



