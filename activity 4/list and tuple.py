import os

# Initialize an empty list to store student records
students = []

# Function to display the menu
def display_menu():
    print("\nStudent Record Management System")
    print("1. Open File")
    print("2. Save File")
    print("3. Save As File")
    print("4. Show All Students Record")
    print("5. Order by Last Name")
    print("6. Order by Grade")
    print("7. Show Student Record")
    print("8. Add Record")
    print("9. Edit Record")
    print("10. Delete Record")
    print("11. Exit")

# Function to load records from a file
def open_file():
    global students
    filename = input("Enter the filename to open: ")
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            students = [eval(line) for line in file]
        print("File opened successfully.")
    else:
        print("File does not exist.")

# Function to save records to a file
def save_file():
    filename = input("Enter the filename to save: ")
    with open(filename, 'w') as file:
        for student in students:
            file.write(f"{student}\n")
    print("File saved successfully.")

# Function to save records to a new file
def save_as_file():
    filename = input("Enter the new filename to save as: ")
    with open(filename, 'w') as file:
        for student in students:
            file.write(f"{student}\n")
    print("File saved as successfully.")

# Function to display all student records
def show_all_records():
    if not students:
        print("No records available.")
    else:
        for student in students:
            print(f"ID: {student[0]}, Name: {student[1][0]} {student[1][1]}, Class Standing: {student[2]}, Exam Grade: {student[3]}")

# Function to order records by last name
def order_by_last_name():
    sorted_students = sorted(students, key=lambda x: x[1][1])
    for student in sorted_students:
        print(f"ID: {student[0]}, Name: {student[1][0]} {student[1][1]}, Class Standing: {student[2]}, Exam Grade: {student[3]}")

# Function to calculate the final grade
def calculate_grade(student):
    return 0.6 * student[2] + 0.4 * student[3]

# Function to order records by grade
def order_by_grade():
    sorted_students = sorted(students, key=calculate_grade, reverse=True)
    for student in sorted_students:
        print(f"ID: {student[0]}, Name: {student[1][0]} {student[1][1]}, Final Grade: {calculate_grade(student):.2f}")

# Function to show a specific student record
def show_student_record():
    student_id = int(input("Enter the Student ID: "))
    for student in students:
        if student[0] == student_id:
            print(f"ID: {student[0]}, Name: {student[1][0]} {student[1][1]}, Class Standing: {student[2]}, Exam Grade: {student[3]}")
            return
    print("Student not found.")

# Function to add a new record
def add_record():
    student_id = int(input("Enter Student ID (6 digits): "))
    first_name = input("Enter First Name: ")
    last_name = input("Enter Last Name: ")
    class_standing = float(input("Enter Class Standing Grade: "))
    exam_grade = float(input("Enter Major Exam Grade: "))
    students.append((student_id, (first_name, last_name), class_standing, exam_grade))
    print("Record added successfully.")

# Function to edit an existing record
def edit_record():
    student_id = int(input("Enter the Student ID to edit: "))
    for i, student in enumerate(students):
        if student[0] == student_id:
            first_name = input("Enter new First Name: ")
            last_name = input("Enter new Last Name: ")
            class_standing = float(input("Enter new Class Standing Grade: "))
            exam_grade = float(input("Enter new Major Exam Grade: "))
            students[i] = (student_id, (first_name, last_name), class_standing, exam_grade)
            print("Record updated successfully.")
            return
    print("Student not found.")

# Function to delete a record
def delete_record():
    student_id = int(input("Enter the Student ID to delete: "))
    for i, student in enumerate(students):
        if student[0] == student_id:
            del students[i]
            print("Record deleted successfully.")
            return
    print("Student not found.")

# Main program loop
while True:
    display_menu()
    choice = input("Enter your choice: ")
    if choice == '1':
        open_file()
    elif choice == '2':
        save_file()
    elif choice == '3':
        save_as_file()
    elif choice == '4':
        show_all_records()
    elif choice == '5':
        order_by_last_name()
    elif choice == '6':
        order_by_grade()
    elif choice == '7':
        show_student_record()
    elif choice == '8':
        add_record()
    elif choice == '9':
        edit_record()
    elif choice == '10':
        delete_record()
    elif choice == '11':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")
