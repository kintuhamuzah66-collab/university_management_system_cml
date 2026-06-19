import logging
logger = logging.getLogger(__name__)

from classes.course import Course

class Department:
    def __init__(self, name):
        self.name = name

        self.courses = []

    @property
    def name(self):
        return self._name 
    
    @name.setter
    def name(self, value):
        """Sets the name of the department"""

        if not value or not str(value).strip():
            logger.error("Failed to set department name. It cannot be empty")
            raise ValueError("Department name cannot be empty!")
        
        self._name = value
        logger.info(f"Department name set to: {self._name}")

    @property
    def courses(self):
        return tuple(self._courses)
    
    def add_course(self, course: Course):
        """Adds course to department courses if it does not already exist"""

        if course in self._courses:
            logger.warning("Course not added because it already exists!")
            return
        
        self._courses.append(course)
        logger.info(f"{course.name} successfully added to {self._name} department")