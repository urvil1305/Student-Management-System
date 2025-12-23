def add_student(students):
    enrol = input("Enter Enrollment number: ")
    fname = input("Enter First Name: ")
    lname = input("Enter Last Name: ")
    department = input("Enter Department: ")
    sem = input("Enter Semester: ")
    student = {
        "enrol": enrol,
        "fname": fname,
        "lname": lname,
        "department": department,
        "sem": sem
    }
    students.append(student)
    print("\n Student added successfully.\n")


def show_students(students):
    if not students:
        print("\n No student records found. Please add a student.\n")
    else:
        print("\n--- Student Records ---")
        for s in students:
            print(f"Enrollment: {s['enrol']}, First Name: {s['fname']}, "
                  f"Last Name: {s['lname']}, Department: {s['department']}, "
                  f"Semester: {s['sem']}")
        print()


def search_student(students):
    enrol = input("Enter Enrollment number to search: ")
    for s in students:
        if s['enrol'] == enrol:
            print(f"\n Student Found: Enrollment: {s['enrol']}, "
                  f"First Name: {s['fname']}, Last Name: {s['lname']}, "
                  f"Department: {s['department']}, Semester: {s['sem']}\n")
            return
    print("\n Student not found.\n")


def update_student(students):
    enrol = input("Enter Enrollment number to update: ")
    for s in students:
        if s['enrol'] == enrol:
            print("\n--- Update Student ---")
            s['fname'] = input(f"Enter new first name (current: {s['fname']}): ") or s['fname']
            s['lname'] = input(f"Enter new last name (current: {s['lname']}): ") or s['lname']
            s['department'] = input(f"Enter new department (current: {s['department']}): ") or s['department']
            s['sem'] = input(f"Enter new semester (current: {s['sem']}): ") or s['sem']
            print("\n Student details updated successfully.\n")
            return
    print("\n Student not found.\n")


def delete_student(students):
    enrol = input("Enter Enrollment number to delete: ")
    for i, s in enumerate(students):
        if s['enrol'] == enrol:
            del students[i]
            print("\n Student deleted successfully.\n")
            return
    print("\n Student not found.\n")


def student_management():
    students = []
    while True:
        print("===== Student Management System =====")
        print("1. Add Student")
        print("2. Show Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("\ Invalid input! Please enter a number.\n")
            continue

        match choice:
            case 1:
                add_student(students)
            case 2:
                show_students(students)
            case 3:
                search_student(students)
            case 4:
                update_student(students)
            case 5:
                delete_student(students)
            case 6:
                print("\n Exiting... Thank you for using Student Management System.\n")
                break
            case _:
                print("\ Please enter a valid choice (1-6).\n")


if __name__ == "__main__":
    student_management()
