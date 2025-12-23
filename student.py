
def addstudent(students):
    enrol = input("Enter Your Enrolment number: ")
    fname = input("Enter Your First Name: ")
    lname = input("Enter Your last Name: ")
    department = input("Enter Your Department: ")
    sem = input("Enter your Semester: ")
    student = {"enrol": enrol,"fname":fname, "lname":lname, "department":department, "sem":sem}
    students.append(student)
    print("Student added successfully.")

def showstudent(students):
    if not students:
        print("Please add student")
    else:
        for s in students:
            print(f"Enrollment: {s['enrol']},First Name:{s['fname']}, Last Name: {s['lname']}, Department: {s['department']}, semester: {s['sem']}")


def searchtudent(students):
    enrol = input("Enter Your Enrolment number: ")
    for s in students:
        if s['enrol'] == enrol:
            print(f"Enrollment: {s['enrol']},First Name:{s['fname']}, Last Name: {s['lname']}, Department: {s['department']}, semester: {s['sem']}")
        else:
            print("Please Enter valid number")

def updatestudent(students):
    enrol = input("Enter Your Enrolment number: ")
    for s in students:
        if s['enrol'] == enrol:
            fname = input(f"Enter new first name (curent: {s['fname']})")
            lname = input(f"Enter new last name (curent: {s['lname']})")
            department = input(f"Enter new department (curent: {s['department']})")
            sem = input(f"Enter new sem (curent: {s['sem']})")
        else:
            print("Please Enter valid number")

def deletestudent(students):
    enrol = input("Enter Your Enrolment number: ")
    for s, i in enumerate(students):
        if s['enrol'] == enrol:
            del students[i]
        else:
            print("Please Enter valid number")

           
def studentmanagement():
    students = []
    while True:
        print("1. Add Student")
        print("2. Show Student")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = int(input("Enter your choice: "))

        match choice:
            case 1:
                addstudent(students)
            case 2:
                showstudent(students)
            case 3:
                searchtudent(students)
            case 4:
                updatestudent(students)
            case 5:
                deletestudent(students)
            case 6:
                exit()
            case _:
                print("Please Enter valid number")



if __name__ =="__main__":
    studentmanagement()
