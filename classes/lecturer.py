from classes.person import Person

class lecturer(Person):
    def __init__(self, id, first_name, last_name, other_name=None):
        super().__init__(id, first_name, last_name, other_name)

        self._course_units = []

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