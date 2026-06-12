from .person import Person

class Student(Person):
    def __init__(self, id, first_name, last_name, other_name=None, major=""):
        super().__init__(id, first_name, last_name, other_name)
        self._major = major

    # major getter and setter
    @property
    def major(self):
        return self._major
    
    @major.setter
    def major(self, value):
        if not value:
            raise ValueError("Major cannot be empty")
        self._major = value

