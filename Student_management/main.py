from clerk.add_students import add_student
# from clerk.delete_student import delete_student
 # from faculty.lookup_student import lookup_student
# from faculty.update_student import update_student
# from hod.summary_reports import generate_summary

def role_menu():
    print("\n Login as ")
    print("1. Clerk")
    print("2. Faculty")
    print("3. HOD")
    print("4. Exit")
    return input("Enter choice: ")

def clerk_menu():
    while True:
        print("\n Clerk Menu ")
        print("1. Add Student")
        print("2. Delete Student")
        print("3. Back")
        ch = input("Choice: ")
        if ch == "1":
            add_student()
        elif ch == "2":
            delete_student()
        elif ch == "3":
            break

def faculty_menu():
    while True:
        print("\n Faculty Menu ")
        print("1. Lookup Student")
        print("2. Update Student")
        print("3. Back")
        ch = input("Choice: ")
        if ch == "1":
            lookup_student()
        elif ch == "2":
            update_student()
        elif ch == "3":
            break

def hod_menu():
    while True:
        print("\n HOD Menu ")
        print("1. Generate Summary Report")
        print("2. Back")
        ch = input("Choice: ")
        if ch == "1":
            generate_summary()
        elif ch == "2":
            break

def main():
    while True:
        choice = role_menu()
        if choice == "1":
            clerk_menu()
        elif choice == "2":
            faculty_menu()
        elif choice == "3":
            hod_menu()
        elif choice == "4":
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
