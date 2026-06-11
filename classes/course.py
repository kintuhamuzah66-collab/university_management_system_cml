class Course:
    def __init__(self, course_id, course_name):
        self.course_id = course_id
        self.course_name = course_name
        
        self.course_units = []

    @property
    def course_id(self):
        return self._course_id
    
    @course_id.setter
    def course_id(self, id):
        try:
            if not id:
                raise ValueError("Invalid id")
        except ValueError:
            print("Course ID cannot be empty")
        
        self._course_id = id

    @property
    def course_name(self):
        return self._course_name
    
    @course_name.setter
    def course_name(self, name):
        try:
            if not name:
                raise ValueError("Invalid name")
        except ValueError:
            print("Course name cannot be empty")

        self._course_name = name

    @property
    def course_units(self):
        return len(self._course_units), self._course_units 

    @course_units.setter
    def course_units(self, course_units):
        try:
            if not course_units:
                raise ValueError("Invalid error")
        except ValueError:
            print(f"You added zero course units to {self.course_name}")
        