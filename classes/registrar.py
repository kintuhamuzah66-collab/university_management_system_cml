from .lecturer import Lecturer
from .student import Student
from .department import Department

import logging

logger = logging.getLogger(__name__)


class AcademicRegistrar:
    def __init__(self, id, first_name, last_name, other_name=None):
        super().__init__(id, first_name, last_name, other_name)
        
        self.departements = []
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
                # logger infor
                return True
            else:
                # logger infor
                return False

        except Exception as e:
            #logger infor
            return False
        



if __name__ == "__main__":
    # Configure logging to print to the console with a clean format
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
    )

    # Now run your code, and your logs will appear!
    