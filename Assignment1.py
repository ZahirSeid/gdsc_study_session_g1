# Zahir Ahmed
# ETS 1501/15
# Task: Student Database

database = {}

def add_student():
    name = input("Enter the student's name: ")
    age = input("Enter the student's age: ")
    grade = input("Enter the student's grade: ")
    StudentID = input("Enter your student ID: ")
    database[name] = {'Age': age, 'Grade': grade, 'StudentID': StudentID}
    print(f"{name} has been added to the database.")

def view_student():
    name = input("Enter the student's name: ")
    if name in database:
        print(f"Name: {name}")
        print(f"Age: {database[name]['age']}")
        print(f"Grade: {database[name]['grade']}")
        print(f"StudentID: {database[name]['StudentID']}")
        
    else:
        print(f"{name} is not in the database.")
        print("Please register")
        option = input("do you want to register ? (Y/N): ")
        if option.upper() == "Y":
            add_student()
        else:
            exit

def list_students():
    for name in database:
        print(f"Name: {name}")
        print(f"Age: {database[name]['age']}")
        print(f"Grade: {database[name]['grade']}")
        print(f"StudentID: {database[name]['StudentID']}")
        print()

def update_student():
    name = input("Enter the student's name: ")
    if name in database:
        age = input("Enter the student's new age: ")
        grade = input("Enter the student's new grade: ")
        database[name]['age'] = age
        database[name]['grade'] = grade
        database[name]['StudentID'] = StudentID
        print(f"{name}'s information has been updated.")
    else:
        print(f"{name} is not in the database.")

def delete_student():
    name = input("Enter the student's name: ")
    if name in database:
        del database[name]
        print(f"{name} has been deleted from the database.")
    else:
        print(f"{name} is not in the database.")
while True:
    print("What would you like to do?")
    print("1. Add a student")
    print("2. View a student")
    print("3. List all students")
    print("4. Update a student's information")
    print("5. Delete a student")
    print("6. Quit")
    choice = input("Enter your choice: ")
    if choice == '1':
        add_student()
    elif choice == '2':
        view_student()
    elif choice == '3':
        list_students()
    elif choice == '4':
        update_student()
    elif choice == '5':
        delete_student()
    elif choice == '6':
        break
    else:
        print("Invalid choice. Please try again.")
