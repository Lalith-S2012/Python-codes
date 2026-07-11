numn=int(input("Enter a Numerator"))
numd=int(input("Enter a Denominator"))

num = numn % numd
if num == 0:
    print("The numbers that you have entered are divisible")
else:
    print("The numbers that you have entered are not divisible")
