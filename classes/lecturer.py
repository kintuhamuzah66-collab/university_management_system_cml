from classes.person import Person

class lecturer(Person):
    def __init__(self, id, first_name, last_name, other_name=None):
        super().__init__(id, first_name, last_name, other_name)

        self._courses = []

    # courses getter and setter
    @property
    def courses(self):
        return self._courses
    
    @courses.setter
    def courses(self, courses):
        if not courses:
            raise ValueError("Courses cannot be empty")
        for course in courses:
            if not course:
                raise ValueError("Course cannot be empty")
            self._courses.append(course)

