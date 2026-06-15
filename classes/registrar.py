from .lecturer import Lecturer
from .student import Student
from .department import Department

class AcademicRegistrar:
    def __init__(self, first_name, last_name, other_name=None):
        super().__init__(first_name, last_name, other_name)
        
        self.departements = []
        self.students = []
        self.lecturers = []

    # manage departments
    def add_department(self, name, courses):
        try:
            department = Department(name)
            department.courses = courses
            self.departements.append(department)
        except Exception as e:
            print(f"Error adding department: {e}")
    
    def remove_department(self, name):
        try:
            for department in self.departements:
                if department.name == name:
                    self.departements.remove(department)
                    return
            print(f"Department {name} not found")
        except Exception as e:
            print(f"Error removing department: {e}")

    def get_departments(self):
        if self.departements:
            return self.departements
        else:
            print("No departments found")
            return []

    def get_department(self, name):
        try:
            for department in self.departements:
                if department.name == name:
                    return department
            print(f"Department {name} not found")
            return None
        except Exception as e:
            print(f"Error getting department: {e}")
            return None
        
    def update_department(self, name, new_name=None, new_courses=None):
        try:
            department = self.get_department(name)
            if department:
                if new_name:
                    department.name = new_name
                if new_courses:
                    department.courses = new_courses
                return department
            elif department is None:
                print(f"Department {name} not found")
                return None 
        except Exception as e:
            print(f"Error updating department: {e}")
            return None
        

    # manage students
    def register_student(self, id, first_name, last_name, other_name=None, major=None):
        try:
            student = Student(id, first_name, last_name, other_name)
            student.major = major
            self.students.append(student)
            return student
        except Exception as e:
            print(f"Error registering student: {e}")
            return None
        
    def remove_student(self, id):
        try:
            for student in self.students:
                if student.id == id:
                    self.students.remove(student)
                    return True
            print(f"Student with ID {id} not found")
            return False
        except Exception as e:
            print(f"Error removing student: {e}")
            return False