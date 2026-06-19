from typing import TYPE_CHECKING
import logging
logger = logging.getLogger(__name__)

if TYPE_CHECKING:
    from classes.student import Student
    from classes.lecturer import Lecturer
    from classes.department import Department

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
    
    # STUDENT SECTION
    def register_student(self, student: 'Student'):
        """Registers new student and and rejects existing ones"""
        try:
            if student in self._students:
                logger.warning(f"{student.full_name} cannot be registered twice!")
            return

            # check course if it exists in the departments
        except ValueError:
            pass
        