print("Enter marks obtained in 4 subjects")
math=int(input("Maths: "))
english=int(input("English: "))
Science=int(input("Science: "))
Afrikaans=int(input("Afrikaans: "))

sum=math+english+Science+Afrikaans
perc= (sum/400)*100

print(end="Percentage Mark = ")
print(perc)

