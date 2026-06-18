import logging
logger = logging.getLogger(__name__)

from classes.course_unit import CourseUnit

class Course:
    def __init__(self, code, name, department):
        self.code = code
        self.name = name
        self.department = department

        self.course_units = []

    @property
    def code(self):
        return self._code 
    
    @code.setter
    def code(self, value):
        if not value or not str(value).strip():
            # log and raise error
            logger.error("Failed to set course code. Course code cannot be empty")
            raise ValueError("Course code cannot be empty")
        # set course course
        self._code = value

    # name properties
    @property
    def name(self):
        return self._name 
    
    @name.setter
    def name(self, value):
        if not value or not str(value).strip():
            # log and raise error
            logger.error("Failed to set course name. Course name cannot be empty")
            raise ValueError("Course name cannot be empty")
        # set course name
        self._name = value

    # course unit properites
    @property
    def course_units(self):
        return tuple(self._course_units)
    
    # add course units to course
    def add_course_unit(self, course_unit: CourseUnit):
        pass