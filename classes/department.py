from .course import Course

class Department:
    def __init__(self, name):
        self._name = name
        self._courses = []

    # name getter and setter
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Department name cannot be empty")
        self._name = value

    # courses getter and setter
    @property
    def courses(self):
        return self._courses

    @courses.setter
    def courses(self, course_id, course_name, course_units):
        if not course_id:
            raise ValueError("Course ID cannot be empty")
        if " " in course_id or not course_id.isalnum():
            raise ValueError("Course ID can only contain letters and numbers")
        
        if not course_name:
            raise ValueError("Course name cannot be empty")

        if not course_units:
            raise ValueError("Course units cannot be empty")
        for unit in course_units:
             if not unit:
                raise ValueError("Course unit cannot be empty")

        course = Course(course_id, course_name)
        course.course_units = course_units
        self._courses.append(course)
