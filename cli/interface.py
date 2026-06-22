import logging
logger = logging.getLogger(__name__)
import sys

from classes.course import Course
from classes.course_unit import CourseUnit
from classes.department import Department
from classes.lecturer import Lecturer
from classes.registrar import AcademicRegistrar
from classes.student import Student


def menu():
    print("SLAU Management System".center(30, "-"))
    print("\n")

    registrar = AcademicRegistrar()

    while True:
        print("\nMange Students". center(30))
        print("1. Register Student")
        print("2. Show registered students")
        print("3. Search student")

        print("Manage Lecturers".center(30))
        print("4. Register Lecturer")
        print("5. Show registered lecturers")
        print("6. Search lecturer")

        print("Manage Departments".center(30))
        print("7. Register Department")
        print("8. Show registered departments")
        print("9. Search department")

        print("10. Exit\n\n")

        choice = input("Enter choice: ")
        print("\n")

        if choice == "1":
            full_name = input("Enter full name: ").strip()
            major = input("Enter major (course): ").strip()
            student_id = input("Assign personal number: ").strip()

            student = Student(student_id, full_name, major)
            if registrar.register_student(student):
                logger.info("Student successfully registered")
        elif choice == "2":
            students = registrar.students
            for student in  students:
                print(student)
        elif choice == "3":
            pass
        elif choice == "4":
            pass
        elif choice == "5":
            pass
        elif choice == "6":
            pass
        elif choice == "7":
            pass
        elif choice == "8":
            pass
        elif choice == "9":
            pass
        elif choice == "10":
            print("Exiting......")
            sys.exit()