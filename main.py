import database_design as d  # Import database_design module

def main():
    print("Hogwarts School of Witchcraft and Wizardry")
    print("Student/Teacher Management System")
    print("1. Add a Student")
    print("2. Add a Teacher")
    print("3. Add a Course")
    print("4. View all Students")
    print("5. View all Admins")
    print("6. View all Courses")
    print("7. Delete a Record")
    print("8. Exit")

    validation = True
    while validation:
        start = input("Enter your choice (1-8):")  # Ask for user input
        if start == "1":
            d.insert_student()  # Call insert_student function
        elif start == "2":
            d.insert_admin()  # Call insert_admin function
        elif start == "3":
            d.insert_course()  # Call insert_course function
        elif start == "4":
            d.student_list()  # Call student_list function
        elif start == "5":
            d.admin_list()  # Call admin_list function
        elif start == "6":
            d.course_list()  # Call course_list function
        elif start == "7":
            d.delete_record()  # Call delete_record function
        elif start == "8":
            validation = False  # Exit loop
            print("Exiting the program.")
        else:
            print("Invalid choice. Please try again.")  # Handle invalid input

main()
