math=int(input("Enter your math marks: "))
english=int(input("Enter your english marks: "))
physics=int(input("Enter your physics marks: "))
history=int(input("Enter your history marks: "))

total=math+english+physics+history
average=int(total/4)

validRange = range(0, 101)

if average not in validRange:
    print("Invalid Input")

elif average in range(91, 101):
    print("Your grade is A1")

elif average in range (81, 91):
    print("Your grade is A2")

elif average in range (71, 81):
    print("Your grade is A3")

elif average in range (61, 71):
    print("Your grade is A4")

elif average in range (51, 61):
    print("Your grade is A5")

elif average in range (41, 51):
    print("Your grade is A6")

elif average in range (31, 41):
    print("Your grade is A7")

elif average in range (21, 31):
    print("Your grade is A8")

elif average in range (11, 21):
    print("Your grade is A9")

elif average in range (0, 11):
    print("Your grade is A10")
