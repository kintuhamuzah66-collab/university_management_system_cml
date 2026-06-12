from .person import Person

class Student(Person):
    def __init__(self, id, first_name, last_name, other_name=None, major=""):
        super().__init__(id, first_name, last_name, other_name)
        self._major = major

        self._course_units = []

    # major getter and setter
    @property
    def major(self):
        return self._major
    
    @major.setter
    def major(self, value):
        if not value:
            raise ValueError("Major cannot be empty")
        self._major = value

    # courses getter and setter
    @property
    def course_units(self):
        return self._couse_units
    
    @course_units.setter
    def course_units(self, courseunits):
        if not courseunits:
            raise ValueError("Courses cannot be empty")
        for course in courseunits:
            if not course:
                raise ValueError("Course cannot be empty")
            self._courses.append(course)
