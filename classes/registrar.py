from typing import TYPE_CHECKING
import logging
logger = logging.getLogger(__name__)

if TYPE_CHECKING:
    from classes.student import Student
    from classes.lecturer import Lecturer
    from classes.department import Department
    from classes.course import Course

class AcademicRegistrar():
    def __init__(self):
        self.departments = []
        self.students = []
        self.lecturers = []

    @property
    def departments(self):
        return (self._departments)
    
    @property
    def students(self):
        return (self._students)
    
    @property
    def lecturers(self):
        return (self._lecturers)
    
    # Get student, department or lecturer
    def get_student(self, p_id):
        """Searches for a student by id"""
        try:
            search_student = (s for s in self.students if s.personal_id == p_id)
            student = next(search_student, 0)
            if student:
                logger.info(f"Student {student.full_name} is found")
                return student 
            else:
                logger.warning(f"Student not found!")
                return False
        except Exception:
            logger.exception("Something went wrong!")
            return False

    def get_department(self, name):
        """Searches for a department by name"""
        try:
            search_department = (d for d in self.departments if d.name == name)
            department = next(search_department, 0)

            if department:
                logger.info(f"Department with name: {department.name} successfully found")
                return department
            else:
                logger.warning(f"Department with name {name} not found!")
                return False
        except Exception:
            logger.exception("Something went wrong")
            return False

    def get_lecturer(self, p_id):
        """Searches for a lecturer by id"""
        try:
            search_lecturer = (l for l in self.lecturers if l.personal_id == p_id)
            lecturer = next(search_lecturer, 0)

            if lecturer:
                logger.info(f"Lecturer with ID: {lecturer.personal_id} successfully found!")
                return lecturer
            else:
                logger.warning(f"Lecturer with ID: {p_id} not found!")
                return False
        except Exception:
            logger.exception("Something went wrong!")
            return False


    # REGISTRATION CORNER
    def register_student(self, student: 'Student'):
        """Registers new student"""
        try:
            if student in self._students:
                logger.warning(f"{student.full_name} cannot be registered twice!")
                return False
            # check course if it exists in the departments
            for department in self.departments:
                if student.major in department.courses:
                    self.students.append(student)
                    logger.info("Student successfully registered to university")
                    return True
                else:
                    logger.warning(f"Course {student.major} not available")
                    return False
        except Exception:
            logger.exception("Something went wrong!")
            return False
        
    def register_lecturer(self, lecturer: 'Lecturer'):
        """Registers new lecturer"""
        try:
            if lecturer in self.lecturers:
                logger.warning(f"Adding lecturer skipped. {lecturer.full_name} already exists!")
                return False
            else:
                self.lecturers.append(lecturer)
                logger.info("Lecturer successfully registered")
                return True
        except Exception:
            logger.exception("Something went wrong!")
            return True
    
    def register_department(self, department: 'Department'):
        """Adds a new department"""
        try:
            if department in self.departments:
                logger.warning(f"Department addition skipped. {department.name} already exists")
                return False
            else:
                self.departments.append(department)
                logger.info(f"{department.name} successfully added to departments")
                return True
        except Exception:
            logger.exception("Something went wrong")
            return False

    