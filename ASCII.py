print(ord('A'))    

print(ord('a'))     

print(ord('J'))    

print(ord('o'))     

print(ord('0')) 

print(ord('7')) 

print(ord('@'))     

print(chr(65))     

print(chr(97))      

# Get input from user

char = input("Enter a single character: ")

if type(char) is str and len(char) == 1:

    print("Valid input")

else:

    print("Please enter exactly one character!")


ascii_val = ord(char)

print(f"Character: {char}")

print(f"ASCII Value: {ascii_val}")