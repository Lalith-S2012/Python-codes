Amount =int(input("Please Enter Amount For Withdraw: "))

note1 = Amount//100
note2 = (Amount%100)//50
note3 = ((Amount%100)%50)//10

print("notes of 100 rands: ", note1)
print("notes of 50 rand: ", note2)
print("notes of 10 rand: ", note3) 