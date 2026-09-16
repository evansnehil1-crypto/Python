students = {
    "Alice": 85,
    "Bob": 72,
    "Charlie": 91,
    "David": 68,
    "Emma": 88
}

total = 0

for score in students.values():
    total = total + score

    average = total / len(students)

print("Class Average", average)

top_student = max(students, key = students.get)
bottom_student = min(students, key = students.get)

print("Top Scorer:", top_student)

print("Bottom Scorer:", bottom_student)

name = input("Enter a student name: ")

score = students.get(name, "Student Not Found")

print(name, ":", score)