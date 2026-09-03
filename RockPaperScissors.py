import random

while True:
    user_action = input("Enter a Choice, (Rock, Paper, Scissors)")
    possible_actions = ["rock", "paper", "scissors"]

    computer_action = random.choice(possible_actions)
    print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")

    if user_action == computer_action:
        print(f"Both players Selected {user_action}, so it is a tie!!!")
    elif user_action == "rock":
        if computer_action == "scissors":
            print("Rock smashes Scissors!!! You Win!")
        else:
            print("Paper Covers Rock!!! You Lose!")
    elif user_action == "paper":
        if computer_action == "rock":
            print("Paper Covers Rock!!! You Win!")
        else:
            print("Scissors Cuts Paper!!! You Lose!")
    elif user_action == "scissors":
        if computer_action == "paper":
            print("Scissors Cuts Paper!!! You Win!")
        else:
            print("Rock Smashes Scissors!!! You Lose!")

    play_again = input("Play Again, (y/n) ")
    if play_again != "y":
        break