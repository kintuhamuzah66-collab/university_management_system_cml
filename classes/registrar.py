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

            # log code
            return True
        
        except Exception as e:
            #log code to signal error
            return False
    
    def remove_departement(self, name):
        try:
            department_generator = (d for d in self.departements if d.name == name)

            department = next(department_generator, None)

            if department:
                self.departments.remove(department)
                # logger infor
                return True
            else:
                # logger infor
                return False

        except Exception as e:
            #logger infor
            return False