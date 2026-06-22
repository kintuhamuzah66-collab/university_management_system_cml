import logging
logger = logging.getLogger(__name__)

from classes.person import Person

class Student(Person):
    def __init__(self, personal_id, full_name, major):
        super().__init__(personal_id, full_name)
        self.major = major

    def __str__(self):
        return f"ID: {self.personal_id}\nName: {self.full_name} Major: {self.major}"

    # major properties
    @property
    def major(self):
        return self._major
    
    @major.setter 
    def major(self, value):
        if not value or str(value).strip():
            # log and raise error
            logger.error("Failed to set major. Major cannot be empty")
            raise ValueError("Major cannot be empty")
        # set major
        self._major = value