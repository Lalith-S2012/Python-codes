total_chores=4
original_count= total_chores
print(f"You have {original_count} chores to finish today\n")

completed_count=0
chore_num=1

while chore_num <= total_chores:
    if chore_num == 1: next_chore = "Make your Bed"
    elif chore_num == 2: next_chore = "Feed your pet"
    elif chore_num == 3: next_chore = "Take out the trash"
    else: next_chore = "Wash the Dishes"

    answer = input(f"Have you finished: {next_chore}? (yes/no) ")

    if answer == "yes":
        completed_count+=1
        chore_num += 1
        print("Great job! Chore completed.")
    else:
        print("Okay, Finish it and check again!")

    print("Chores remaing:", total_chores - completed_count)
    print()

    print("===== All chores Completed =====")
    print("Great work finishing")