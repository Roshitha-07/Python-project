import csv
from utils.constants import CSV_FILE, COLUMNS


def search_student():

    print(" Student Lookup ")
    search = input("Enter Roll No or Name: ").strip()

    found = False
    results = []

    try:
        with open(CSV_FILE, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                if search.isdigit() and int(search) == int(row["Roll_No"]):
                    results = [row]
                    found = True
                    break
                # Partial Name match (case-insensitive)
                elif search.lower() in row["Name"].lower():
                    results.append(row)
                    found = True
    except FileNotFoundError:
        print(f" {CSV_FILE} not found. No records available.")
        return

    if found:
        print("\n Search Results")
        for r in results:
            print(f"Roll_No: {r['Roll_No']}, Name: {r['Name']}, Branch: {r['Branch']}, "
                  f"Year: {r['Year']}, Gender: {r['Gender']}, Age: {r['Age']}, "
                  f"Attendance: {r['Attendance_%']}%, "
                  f"Mid1: {r['Mid1_Marks']}, Mid2: {r['Mid2_Marks']}, "
                  f"Quiz: {r['Quiz_Marks']}, Final: {r['Final_Marks']}")
    else:
        print(" No student found with that Roll No or Name.")
