import csv
import os
from utils.constants import CSV_FILE, COLUMNS

def add_student():
    print("\n Add New Student ")

    while True:
        roll_no = input("Roll No: ").strip()
        if roll_no.isdigit():
            roll_no = int(roll_no)
            break
        else:
            print("Roll No must be a number.")

    # check duplicate
    if os.path.exists(CSV_FILE):
        with open(CSV_FILE, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                if int(row["Roll_No"]) == roll_no:
                    print(" Student with this Roll_No already exists!")
                    return
    
    name = input("Name: ").strip()
    branch = input("Branch: ").strip()
    year = input("Year: ").strip()
    gender = input("Gender: ").strip()
    age = int(input("Age: ")).strip()
    attendance = float(input("Attendance %: "))

    marks = []
    for exam in ["Mid1", "Mid2", "Quiz", "Final"]:
        marks.append(float(input(f"{exam} Marks: ")))

    # write student
    file_exists = os.path.exists(CSV_FILE)
    with open(CSV_FILE, "a", newline="") as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(COLUMNS)
        writer.writerow([
            roll_no, name, branch, year, gender, age,
            attendance, marks[0], marks[1], marks[2], marks[3]
        ])

    print(" Student added successfully!")
