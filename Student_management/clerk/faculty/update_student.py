import csv
from utils.constants import CSV_FILE, COLUMNS

def update_student():
    """UC3 - Update a student's attendance or marks"""
    
    print("\n--- Update Student Records ---")
    roll = input("Enter Roll No of student to update: ").strip()

    updated = False
    rows = []

    
    try:
        with open(CSV_FILE, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row["Roll_No"] == roll:
                    print(f"\nFound Student: {row['Name']} (Roll {row['Roll_No']})")
                    print("Current Attendance:", row["Attendance_%"])
                    print("Current Marks: Mid1:", row["Mid1_Marks"], 
                          "Mid2:", row["Mid2_Marks"], 
                          "Quiz:", row["Quiz_Marks"], 
                          "Final:", row["Final_Marks"])

                    # Ask what to update
                    print("\nWhat do you want to update?")
                    print("1. Attendance")
                    print("2. Marks")
                    choice = input("Enter choice: ")

                    if choice == "1":
                        new_att = input("Enter new Attendance %: ")
                        try:
                            new_att = float(new_att)
                            if 0 <= new_att <= 100:
                                print(f"Old Attendance: {row['Attendance_%']} → New: {new_att}")
                                row["Attendance_%"] = str(new_att)
                                updated = True
                            else:
                                print(" Attendance must be 0-100.")
                        except:
                            print(" Invalid number.")
                    
                    elif choice == "2":
                        for exam in ["Mid1_Marks", "Mid2_Marks", "Quiz_Marks", "Final_Marks"]:
                            new_mark = input(f"Enter new {exam} (leave blank to keep {row[exam]}): ")
                            if new_mark.strip() != "":
                                try:
                                    new_mark = float(new_mark)
                                    if 0 <= new_mark <= 100:
                                        print(f"Old {exam}: {row[exam]} → New: {new_mark}")
                                        row[exam] = str(new_mark)
                                        updated = True
                                    else:
                                        print("Marks must be 0-100.")
                                except:
                                    print(" Invalid number.")
                    else:
                        print(" Invalid choice!")
                rows.append(row)

    except FileNotFoundError:
        print(f" {CSV_FILE} not found. Cannot update records.")
        return

    # Save updated rows back to CSV
    if updated:
        with open(CSV_FILE, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=COLUMNS)
            writer.writeheader()
            writer.writerows(rows)
        print("\n Record updated successfully!")
    else:
        print("\nNo updates made (student not found).")
