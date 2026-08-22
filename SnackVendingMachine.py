def calculate_change (paid, price):
    change = paid - price
    return change

snack_price = 25
print(" Snack Vending Machine")
print(f"This snack costs {snack_price} units. ")
print("Accepted Coins, 1, 5, 10, or 25.")

total_inserted = 0
coins_inserted = 0

while True:
    coin = int(input("Insert a coin (1, 5, 10 or 25): "))

    if coin != 1 and coin != 5 and coin != 10 and coin != 25:
        print("Invalid Coin... Enter Again: ")
        continue
    total_inserted += coin
    coin += 1
    print(f"Inserted coin {coin}. Total so far: {total_inserted}.")

    if total_inserted >= snack_price:
        print("Enough Money Inserted!")
        break

change_due = calculate_change(total_inserted, snack_price)

print("Dispensing your Snack...")

if change_due == 0:
    pass
else:
    print(f"Here is you Change: {change_due} units.")

print("Purchase Summary")
print("Snack Price: ", snack_price)
print("Coins Inserted: ", coins_inserted)
print("Total Paid: ", total_inserted)
print("Change Given: ", change_due)
print("Thanks for the Purchase, Buy more Next Time!!!")
