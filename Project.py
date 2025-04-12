# ADD STUDENT
def add_student():
    with open("D:\\projects\\student.txt", "a") as f:
        reg = input("Enter registration number: ")
        name = input("Enter student name: ")
        father = input("Enter father name: ")
        gpa = input("Enter GPA: ")
        f.write(f"{reg},{name},{father},{gpa}")
    print("Student data has been added.")

# DISPLAY STUDENT
def display_student():
    with open("D:\\projects\\student.txt", "r") as f:
        print("Registration No., Name, Father Name, GPA")
        for line in f:
            print(line.strip())

# SEARCH STUDENT
def Search_student():
    reg = input("Enter registration number to search: ")
    found = False
    with open("D:\\projects\\student.txt", "r") as f:
        for line in f:
            data = line.strip().split(",")
            if reg == data[0]:
                print(f"Student found: {line.strip()}")
                found = True
                break
    if not found:
        print("Student not available.")

# MODIFY STUDENT
def modify_student():
    reg = input("Enter registration number to modify: ")
    updated_lines = []
    found = False
    with open("D:\\projects\\student.txt", "r") as f:
        for line in f:
            data = line.strip().split(",")
            if reg == data[0]:
                print("Updating student record...")
                name = input("Enter new name: ")
                father = input("Enter new father name: ")
                gpa = input("Enter new GPA: ")
                updated_lines.append(f"{reg},{name},{father},{gpa}\n")
                found = True
            else:
                updated_lines.append(line)
    with open("D:\\projects\\student.txt", "w") as f:
        f.writelines(updated_lines)
    if found:
        print("Student record updated.")
    else:
        print("Student not found.")

# DELETE STUDENT
def delete_student():
    reg = input("Enter registration number to delete: ")
    found = False
    with open("D:\\projects\\student.txt", "r") as f:
        lines = f.readlines()
    
    with open("D:\\projects\\student.txt", "w") as f:
        for line in lines:
            if not line.startswith(reg + ","):
                f.write(line)
            else:
                found = True
    
    if found:
        print(f"Student with registration number {reg} has been deleted.")
    else:
        print(f"Student with registration number {reg} not found.")

# ADD COURSE
def add_course():
    with open("D:\\projects\\course.txt", "a") as f:
        reg = input("Enter registration number: ")
        course_code = input("Enter course code: ")
        course_name = input("Enter course name: ")
        marks = input("Enter marks: ")
        grades = input("Enter grades: ")
        f.write(f"\n{reg},{course_code},{course_name},{marks},{grades}")  
    print("Course data has been added.")

# DISPLAY COURSES
def display_courses():
    with open("D:\\projects\\course.txt", "r") as f:
        print("Registration No., Course Code, Course Name, Marks, Grades")
        for line in f:
            print(line.strip())

# SEARCH COURSE
def Search_course():
    reg = input("Enter registration number to search: ")
    course_code = input("Enter course code to search: ")
    found = False
    with open("D:\\projects\\course.txt", "r") as f:
        for line in f:
            data = line.strip().split(",")
            if reg == data[0] and course_code == data[1]:
                print(f"Course found: {line.strip()}")
                found = True
                break
    if not found:
        print("Course not found.")

# MODIFY COURSE
def modify_courses():
    reg = input("Enter registration number to modify: ")
    course_code = input("Enter course code to modify: ")
    updated_lines = []
    found = False
    with open("D:\\projects\\course.txt", "r") as f:
        for line in f:
            data = line.strip().split(",")
            if reg == data[0] and course_code == data[1]:
                print("Updating course record...")
                course_name = input("Enter new course name: ")
                marks = input("Enter new marks: ")
                grades = input("Enter new grades: ")
                updated_lines.append(f"{reg},{course_code},{course_name},{marks},{grades}\n")
                found = True
            else:
                updated_lines.append(line)
    with open("D:\\projects\\course.txt", "w") as f:
        f.writelines(updated_lines)
    if found:
        print("Course record updated.")
    else:
        print("Course not found.")

# DELETE COURSE
def delete_course():
    reg = input("Enter registration number: ")
    course_code = input("Enter course code: ")
    updated_lines = []
    found = False
    with open("D:\\projects\\course.txt", "r") as f:
        for line in f:
            if not line.startswith(f"{reg},{course_code}"):
                updated_lines.append(line)
            else:
                found = True
    with open("D:\\projects\\course.txt", "w") as f:
        f.writelines(updated_lines)
    if found:
        print("Course record deleted.")
    else:
        print("Course not found.")

# SELECTION
while True:
    print("\nMenu:")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Modify Student")
    print("5. Delete Student")
    print("6. Add Course")
    print("7. Display Courses")
    print("8. Search Course")
    print("9. Modify Course")
    print("10. Delete Course")
    print("11. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        display_student()
    elif choice == "3":
        Search_student()
    elif choice == "4":
        modify_student()
    elif choice == "5":
        delete_student()
    elif choice == "6":
        add_course()
    elif choice == "7":
        display_courses()
    elif choice == "8":
        Search_course()
    elif choice == "9":
        modify_courses()
    elif choice == "10":
        delete_course()
    elif choice == "11":
        print("Exiting program.")
        break
    else:
        print("Invalid choice")