import array as arr
marks = arr.array('i', [78, 56, 94, 85, 79])
print("These are the marks of different subjects:", marks)

print("The number of Subjects:", len(marks))

perc = ((sum(marks))/500)*100
print("The Average is:", perc)

