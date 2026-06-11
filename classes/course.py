class Course:
    def __init__(self, course_id, course_name):
        self._course_id = course_id
        self._course_name = course_name
        
        self.course_units = []

    # course id getter and setter
    @property
    def course_id(self):
        return self._course_id
    
    @course_id.setter
    def course_id(self, id):
        if not id:
            raise ValueError("Course ID cannot be empty")
        if " " in id or not id.isalnum():
            raise ValueError("Course ID can only contain letters and numbers")

        self._course_id = id

    # course name getter and setter
    @property
    def course_name(self):
        return self._course_name
    
    @course_name.setter
    def course_name(self, name):
        if not name:
                raise ValueError("Course name cannot be empty")

        self._course_name = name

    # course units getter and setter
    @property
    def course_units(self):
        return len(self._course_units), self._course_units 

    @course_units.setter
    def course_units(self, course_units):
        if not course_units:
                raise ValueError("Course units cannot be empty")
        for unit in course_units:
             if not unit:
                raise ValueError("Course unit cannot be empty")
             self._course_units.append(unit)