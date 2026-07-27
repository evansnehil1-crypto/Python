total_chores = 4
original_count = total_chores
print(f"You have {original_count} chores to finish today!\n")

completed_count = 0
chore_num = 1

while chore_num <= total_chores:
    if chore_num == 1:
        next_chore = "Make your bed"
    elif chore_num == 2:
        next_chore = "Feed the dog"
    elif chore_num == 3:
        next_chore = "Take out the trash"
    else:
        next_chore = "Wash the dishes"

    answer = input(f"Have you finished: {next_chore}? (yes/no): ")

    if answer == "yes":
        completed_count += 1
        chore_num += 1
        print("Great job! Chore completed.")
    else:
        print("Okay, finish it and check again!")

    print(f"Chores remaining: {total_chores - completed_count}")
    print()

print("===== ALL CHORES COMPLETE! =====")

x = 1 
help = 1
while(x==1):
    print(x)
    help = help+1
    if(help == 5):
        break