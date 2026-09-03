import random
playing = True 
number = str(random.randint(0,9))
print("I will generate a number from 0 to 9, and you have to guess the number, one digit at a time.")
while playing:
    guess = input("Give me your Best Guess! \n")
    if number == guess:
        print("You win the Game!!!")
        print("The Number was ", number)
        break

    else:
        print("Your Guess wasn't Right, Please Try Again. \n")
        
