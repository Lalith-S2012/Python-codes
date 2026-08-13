def greet_customer():
    print("Welcome to the Lemonade Stand")
    print("Fresh Lemonade, Made just for you")

greet_customer()

price_per_cup = float(input("Enter the price per cup in Dollars: "))
cups_sold = int(input("Enter the number of cups sold: "))

def calculate_total(price, cups):
    total = price * cups 
    return total

total_cost = calculate_total(price_per_cup, cups_sold)

rounded_total = round(total_cost, 2)
print("Total Cost:", total_cost)

amount_paid = float(input("Enter the amount Paid by the customer: "))

def calculate_change(paid, total):
    change = paid - total
    return change 

change_due = calculate_change(amount_paid, rounded_total)
rounded_change = round(change_due, 2)

def thank_you_message(cups):
    if cups >= 5:
        return "Wow, Big Order, Thank you so Much!"
    else:
        return "Thanks for stopping by the stand!"

closing_message = thank_you_message(cups_sold)

print("====Lemonade Stand Receipt====")
print("Price Per Cup:", price_per_cup)
print("Cups Sold:", cups_sold)
print("Total Cost:", total_cost)
print("Amount Paid:", amount_paid)
print("Change Due:", change_due)
print(closing_message)