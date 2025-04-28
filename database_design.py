import os
import sqlite3

#cur.execute on all
create_admin_table =  """create table if not exists HogwartAdmin (WizardID INTEGER PRIMARY KEY AUTOINCREMENT, Name TEXT NOT NULL, CourseID INT);"""
create_course_table =  """create table if not exists Courses (CourseID INTEGER PRIMARY KEY AUTOINCREMENT, CourseName TEXT NOT NULL);"""
create_student_table =  """create table if not exists Students (WizardID INTEGER PRIMARY KEY AUTOINCREMENT, Name TEXT NOT NULL, House TEXT NOT NULL, Year INTEGER NOT NULL);"""

con = sqlite3.connect('Hogwarts.db')
cur = con.cursor()

cur.execute(create_admin_table)
cur.execute(create_course_table)
cur.execute(create_student_table)

insert_admin =  "insert into HogwartAdmin (Name, CourseID) values (?,?);"
insert_student_query =  "insert into Students (Name, House, Year) values (?, ?, ?);"
insert_course = "INSERT INTO Courses (CourseName) VALUES (?);"

student_list = "SELECT Name, House, Year FROM Students;"
student_count = "SELECT COUNT(*) FROM Students"

student_list_query = "SELECT Name, House, Year FROM Students;"
student_count_query = "SELECT COUNT(*) FROM Students;"
admin_list_query = "SELECT WizardID, Name, CourseID FROM HogwartAdmin;"
course_list_query = "SELECT CourseID, CourseName FROM Courses;"

course_data =  [
    ('Astronomy',),
    ('Charms',),
    ('Defense Against the Dark Arts',),
    ('Flying',),
    ('Herbology',),
    ('History of Magic',),
    ('Potions',),
    ('Transfiguration',),
    ('Care of Magical Creatures',),
    ('Divination',),
    ('Muggle Studies',),
    ('Study of Ancient Runes',),
    ('Alchemy',),
    ('Other Staff',),
]

admin_data = [
    ('Albus Dumbledore', 14),
    ('Minerva McGonagall', 8),
    ('Severus Snape', 7),
    ('Filius Flitwick', 2),
    ('Pomona Sprout', 5),
    ('Rubeus Hagrid', 9),
    ('Gilderoy Lockhart', 10),
    ('Horace Slughorn', 11),
    ('Sybill Trelawney', 12),
    ('Remus Lupin', 13),
    ('Alastor Moody', 4),
    ('Firenze', 1),
]
cur.execute("SELECT COUNT(*) FROM Courses;")
if cur.fetchone()[0] == 0:
    cur.executemany(insert_course, course_data)

cur.execute("SELECT COUNT(*) FROM HogwartAdmin;")
if cur.fetchone()[0] == 0:
    cur.executemany(insert_admin, admin_data)
con.commit()

def insert_student():
    name = input("Enter the student's name: ")
    year = input("Enter the student's year (1-7): ")
    house = input("Enter the student's house (Gryffindor, Slytherin, Hufflepuff, Ravenclaw): ")
    if year not in ['1', '2', '3', '4', '5', '6', '7']:
        print("Invalid year. Please enter a number between 1 and 7.")
        return
    elif house not in ['Gryffindor', 'Slytherin', 'Hufflepuff', 'Ravenclaw']:
        print("Invalid house. Please enter one of the following: Gryffindor, Slytherin, Hufflepuff, Ravenclaw.")
        return
    else:
        cur.execute(insert_student_query, (name, house, year))
        con.commit()
        print(f"Student {name} added successfully!")

def insert_course():
    course_id = input("Enter the course ID: ")
    course_name = input("Enter the course name: ")
    cur.execute(insert_course, (course_id, course_name))
    con.commit()
    print(f"Course {course_name} added successfully!")

def insert_admin():
    name = input("Enter the admin's name: ")
    course_id = input("Enter the course/occupation ID: ")
    cur.execute(insert_admin, (name, course_id))
    con.commit()
    print(f"Admin {name} added successfully!")

def all_students():
    cur.execute("SELECT Name, House, Year FROM Students;")
    students = cur.fetchall()
    if students:
        print("List of all students:")
        for student in students:
            print(f"Name: {student[0]}, House: {student[1]}, Year: {student[2]}")
    else:
        print("No students found.")

def student_by_year():
    year = input("Enter the year (1-7): ")
    cur.execute("SELECT Name, House, Year FROM Students WHERE Year = ?;", (year,))
    students = cur.fetchall()
    if students:
        print(f"Students in Year {year}:")
        for student in students:
            print(f"Name: {student[0]}, House: {student[1]}, Year: {student[2]}")
    else:
        print(f"No students found in Year {year}.")

def student_by_house():
    house = input("Enter the house name: ")
    cur.execute("SELECT Name, House, Year FROM Students WHERE House = ?;", (house,))
    students = cur.fetchall()
    if students:
        print(f"Students in House {house}:")
        for student in students:
            print(f"Name: {student[0]}, House: {student[1]}, Year: {student[2]}")
    else:
        print("No students found in that house.")

def student_list():
    while True:
        print("1. View all students")
        print("2. View students by year")
        print("3. View students by house")
        print("4. Exit")

        student_choice = input("Enter your choice (1-3):")
        if student_choice == "1":
            all_students()
        elif student_choice == "2":
            student_by_year()
        elif student_choice == "3":
            student_by_house()
        elif student_choice == "4":
            print("Exiting student list.")
            break
        else:
            print("Invalid choice. Please try again.")
            student_list()

def admin_list():
    cur.execute(admin_list_query)
    admins = cur.fetchall()
    if admins:
        print("List of all admins:")
        for admin in admins:
            print(f"WizardID: {admin[0]}, Name: {admin[1]}, CourseID: {admin[2]}")
    else:
        print("No admins found.")

def course_list():
    cur.execute(course_list_query)
    courses = cur.fetchall()
    if courses:
        print("List of all courses:")
        for course in courses:
            print(f"CourseID: {course[0]}, CourseName: {course[1]}")
    else:
        print("No courses found.")