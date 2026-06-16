from .lecturer import Lecturer
from .student import Student
from .department import Department
from .person import Person

import logging

logger = logging.getLogger(__name__)


class AcademicRegistrar(Person):
    def __init__(self, id, first_name, last_name, other_name=None):
        super().__init__(id, first_name, last_name, other_name)
        
        self.departments = []
        self.students = []
        self.lecturers = []

    # manage departments
    def add_department(self, name, courses):
        try:
            department = Department(name)
            department.courses = courses
            self.departments.append(department)

            logger.info(f"Department {department.name} successfully added")
            return True
        
        except Exception as e:
            logger.error(f"{e} occered when trying to delete {department.name}")
            return False
    
    def remove_department(self, name):
        try:
            department_generator = (d for d in self.departments if d.name == name)

            department = next(department_generator, None)

            if department:
                self.departments.remove(department)
                logger.info(f"{department.name} successfully removed")
                return True
            else:
                logger.warning(f"Department not found!")
                return False

        except Exception as e:
            logger.exception("Something went wrong")
            return False
        
    def find_department(self, name):
        try:
            department_generator = (s for s in self.departments if s.name == name)

            department = next(department_generator, None)

            if department:
                logger.info(f"{department.name} found")
                return department
            else:
                logger.warning(f"Department not found!")
                return False
            
        except Exception as e:
            logger.exception("Something went wrong")
            return False
        