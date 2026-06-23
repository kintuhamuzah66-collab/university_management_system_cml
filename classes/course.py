from typing import TYPE_CHECKING
import logging
logger = logging.getLogger(__name__)

if TYPE_CHECKING:
    from classes.course_unit import CourseUnit

class Course:
    def __init__(self, code, name, department):
        self.code = code
        self.name = name
        self.department = department

        self._codecourse_units = []

    def __eq__(self, other):
        if not isinstance(other, Course):
            return False
        return self.course_code == other.course_code

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
        logger.info(f"Course code set to: {self._code}")

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
        logger.info(f"Course name set to {self._name}")

    # course unit properites
    @property
    def course_units(self):
        return tuple(self._course_units)
    
    def add_course_unit(self, course_unit: 'CourseUnit'):
        """ Adds course unit to course if it does not exist"""
        if course_unit in self._course_units:
            logger.warning("Course Unit already exits!")
            return
        self._course_units.append(course_unit)
        logger.info(f"{course_unit.name} successfully added to {self._name}")