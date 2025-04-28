import database_design as d

def main():
    print("Hogwarts School of Witchcraft and Wizardry")
    print("Student/Teacher Management System")
    print("1. Add a Student")
    print("2. Add a Teacher")
    print("3. Add a Course")
    print("4. View all Students")
    print("5. View all Admins")
    print("6. View all Courses")
    print("7. Exit")

    validation = True
    while validation:
        start = input("Enter your choice (1-7):")
        if start == "1":
            d.insert_student()  #call insert student
        elif start == "2":
            d.insert_admin()  #call insert admin
        elif start == "3":
            d.insert_course()  #call insert course
        elif start == "4":
            d.student_list()
        elif start == "5":
            d.admin_list()  #call all admins
        elif start == "6":
            d.course_list() #call all courses
        elif start == "7":
            validation = False
            print("Exiting the program.")
        else:
            print("Invalid choice. Please try again.")

main()