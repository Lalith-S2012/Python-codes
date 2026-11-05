answer = int(input("Enter the amount of prime numbers you want to see: "))
num = 2
while num <= answer:
    i = 2
    is_prime = True
    while i < num:
        if num%i == 0:
            is_prime = False
            break
        i += 1
    if is_prime:
        print(num)
    num += 1

