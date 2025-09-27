import csv
import os
from ..utils.constants import CSV_FILE, COLUMNS

DELETED_FILE = "data/students_deleted.csv"

def delete_student():

    roll = input("\nEnter Roll No of student to delete: ").strip()
    found = False
    rows = []
    deleted_row = None

    # Read all rows from main CSV
    try:
        with open(CSV_FILE, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row["Roll_No"] == roll:
                    found = True
                    deleted_row = row
                    print(f"\n Found student: {row['Name']} (Roll {row['Roll_No']})")
                    confirm = input("Are you sure you want to delete? (Y/N): ").strip().lower()
                    if confirm == "y":
                        print("Record marked for deletion.")
                        continue  
                    else:
                        print(" Deletion cancelled.")
                        rows.append(row) 
                else:
                    rows.append(row)
    except FileNotFoundError:
        print(f" {CSV_FILE} not found.")
        return

   
    with open(CSV_FILE, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=COLUMNS)
        writer.writeheader()
        writer.writerows(rows)


    if deleted_row:
        if not os.path.exists(DELETED_FILE):
            with open(DELETED_FILE, "w", newline="") as f:
                writer = csv.DictWriter(f, fieldnames=COLUMNS)
                writer.writeheader()
        with open(DELETED_FILE, "a", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=COLUMNS)
            writer.writerow(deleted_row)

        print(f" Student {deleted_row['Name']} (Roll {deleted_row['Roll_No']}) deleted and moved to {DELETED_FILE}")
    else:
        if not found:
            print(" Student not found.")
