cp = int(input("Enter the cost of 10 oranges "))
sp = int(input("Enter the selling price of 1 orange "))

cp_1= cp/10
if cp_1 > sp:
    print("You have made a Loss of ", int(cp_1-sp))
else:
    print("You have made a Profit of ", int(sp-cp_1) )

