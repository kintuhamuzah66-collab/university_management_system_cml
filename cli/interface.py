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
        print("Manage Students". center(30))
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
        print("10. Add course to department")
        print("11. Show available courses in department")
        print("12. Add course unit to department course")

        print("13. Exit\n")

        choice = input("Enter choice: ")
        print("\n")

        if choice == "1":
            # Register student
            full_name = input("Enter full name: ").strip()
            major = input("Enter major (course code): ").strip()
            student_id = input("Assign personal number: ").strip()

            student = Student(student_id, full_name, major)
            if registrar.register_student(student):
                logger.info("Student successfully registered")
        elif choice == "2":
            # show available students
            students = registrar.students
            for student in  students:
                print(student)
        elif choice == "3":
            # look for student by personal number
            personal_number = input("Enter student personal number: ").strip()
            student = registrar.get_student(personal_number)
            if student:
                print(student)
            else:
                print("Student not found!")
        elif choice == "4":
            pass
        elif choice == "5":
            pass
        elif choice == "6":
            pass
        elif choice == "7":
            # register department
            name = input("Enter department name: ").strip()
            department = Department(name)
            register = registrar.register_department(department)
            if register:
                print()
            else:
                print()
        elif choice == "8":
            # show available departments
            departments = registrar.departments
            if len(departments) == 0:
                print("No department found!")
            else:
                for department in departments:
                    print(department)
        elif choice == "9":
            # Search department
            name = input("Enter department name: ").strip()
            department = registrar.get_department(name)
            if department:
                print(department)
            else:
                print("Department not found!")
        elif choice == "10":
            # add course to department
            department_name = input("Enter department name: ").strip()
            department: 'Department' = registrar.get_department(department_name)
            if department:
                name = input("Enter course name: ").strip()
                code = input("Enter course code: ").strip()
                course = Course(code, name, department_name)
                department.add_course(course)
                print(f"{course.name} successfully added to {department.name}")
            else:
                print("Adding course failed!")
        elif choice == "11":
            # show available courses in a department
            department_name: 'Department' = input("Enter department name: ").strip()
            dep_courses = registrar.show_department_courses(department_name)

            if dep_courses:
                for course in dep_courses:
                    print(course)
            else:
                print("No course found!")
        elif choice == "12":
            # add course unit to department course
            dep_name = input("Enter department name: ").strip()
            course_code = input("Enter course code: ").strip()
            course_unit_name = input("Enter course unit name: ").strip()
            course_unit_code = input("Enter course unit code: ").strip()
            
            department = registrar.get_department(dep_name)
            if department:
                for course in department.courses:
                    if course.code == course_code:
                        course_unit = CourseUnit(course_unit_code, course_unit_name)
                        registrar.add_course_unit_to_course(dep_name, course_code, course_unit)
                        print(f"{course_unit.name} successfully added to {course.name}")
                        return True
                print("Failed to add course unit")
                return False
            print("Department not found!")
            
        elif choice == "13":
            print("Exiting......")
            break