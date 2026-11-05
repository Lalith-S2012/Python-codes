mark = {"Eli": 87, "Omphile": 98, "Jerome": 56, "Matt": 72, "William": 78}
print(mark)
total = 0

for i in mark.values():
    total = i + total 
    
avg = total / len(mark)
print("The average is: ", avg)

maximum = max(mark.values())
minimum = min(mark.values())

for name, score in mark.items():
    if score == maximum:
        ms = name
    if score == minimum:
        mss = name

print(ms, " got the highest mark")
print(mss, " got the lowest mark")

search = input("Enter the Student you want to search: ")

score = mark.get(search)

if score is not None:
    print(score)
else:
    print("Type in the Student name with the correct spelling")

