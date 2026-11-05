print("=== Welcome to the Guessing Game ===")

secnum = 26

for i in range(1, 5) :
    guess1=int(input("Enter your guess: "))

    if guess1 == secnum:
        print("Good job, You have guessed it right!!!")
    elif guess1 > 40:
        print("Ice Cold, Try again: ")
    elif guess1 > 35 and guess1 <40:
        print("Cold, Try again: ")
    elif guess1 > 26 or guess1 < 30:
        print("Warm, Try again: ")
    elif guess1 > 24 or guess1 < 28:
        print("Hot, Try again: ")
    elif guess1 > 1 or guess1 < 10:
        print("Ice Cold, Try again: ")
    elif guess1 > 10 or guess1 < 24:
        print("Warm, Try again: ")


