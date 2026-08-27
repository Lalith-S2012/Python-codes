print("You will now have to guess a Password.. The Password consists of 6 letters and 3 Numbers at the end")

while True:
    password = input("Enter the Password: ")
    if password.lower() == "python123":
        print("Well done, You have Guessed the password")
        break
    else:
        print("Wrong Password, Please Enter the Password Again")
        
    
