import csv
import os
from utils.constants import CSV_FILE, IMPORT_ERRORS_FILE, COLUMNS

def validate_row(row):
    """Validate student row (types, ranges). Returns (is_valid, error_msg)."""
    try:
        # Roll No must be int
        int(row["Roll_No"])

        # Age must be int
        int(row["Age"])

        # Attendance 0–100
        att = float(row["Attendance_%"])
        if not (0 <= att <= 100):
            return False, "Invalid Attendance"

        # Marks 0–100
        for field in ["Mid1_Marks", "Mid2_Marks", "Quiz_Marks", "Final_Marks"]:
            m = float(row[field])
            if not (0 <= m <= 100):
                return False, f"Invalid {field}"
    except Exception as e:
        return False, f"Error: {str(e)}"

    return True, ""

def load_existing_rolls():
    """Return set of existing roll numbers in master file."""
    rolls = set()
    if os.path.exists(CSV_FILE):
        with open(CSV_FILE, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                rolls.add(row["Roll_No"])
    return rolls

def bulk_import():
    """UC6 - Bulk Import from a CSV file"""

    file_path = input("\nEnter path of CSV to import: ").strip()
    if not os.path.exists(file_path):
        print("File not found.")
        return

    existing_rolls = load_existing_rolls()
    valid_rows = []
    error_rows = []

    with open(file_path, "r") as f:
        reader = csv.DictReader(f)
        line_num = 1
        for row in reader:
            line_num += 1
            # Check duplicates
            if row["Roll_No"] in existing_rolls:
                row["Error"] = "Duplicate Roll_No"
                error_rows.append((line_num, row))
                continue

            # Validate row
            ok, error = validate_row(row)
            if ok:
                valid_rows.append(row)
                existing_rolls.add(row["Roll_No"])
            else:
                row["Error"] = error
                error_rows.append((line_num, row))

    # Append valid rows to CSV
    file_exists = os.path.exists(CSV_FILE)
    with open(CSV_FILE, "a", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=COLUMNS)
        if not file_exists:
            writer.writeheader()
        writer.writerows(valid_rows)

    # Write errors to import_errors.csv
    if error_rows:
        with open(IMPORT_ERRORS_FILE, "a", newline="") as f:
            fieldnames = COLUMNS + ["Error", "Line_Number"]
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            if os.path.getsize(IMPORT_ERRORS_FILE) == 0:
                writer.writeheader()
            for line_num, row in error_rows:
                row["Line_Number"] = line_num
                writer.writerow(row)

    print(f"\n Import finished: {len(valid_rows)} rows added, {len(error_rows)} errors.")
    if error_rows:
        print(f"See {IMPORT_ERRORS_FILE} for error details.")
