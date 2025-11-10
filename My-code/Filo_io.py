import csv

student = []

with open("student.csv") as file:
    reader = csv.reader(file)
    for name, home in reader:
        student.append({"name": name, "home": home})

for student in sorted(student, key=lambda student: student["name"]):
    print(f"{student['name']} is from {student['home']}")