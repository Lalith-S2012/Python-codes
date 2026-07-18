a = float(input("Enter the first number (a): "))
b = float(input("Enter the second number (b): "))
c = float(input("Enter the third number (c): "))

print(f"\nBefore swapping: a = {a}, b = {b}, c = {c}")

a, b, c = b, c, a

print(f"After swapping:  a = {a}, b = {b}, c = {c}")