import logging
logger = logging.getLogger(__name__)

class Department:
    def __init__(self, name):
        self.name = name

        self.courses = []

    # name properties
    @property
    def name(self):
        return self._name 
    
    @name.setter
    def name(self, value):
        if not value or not str(value).strip():
            # log and raise error
            logger.error("Failed to set department name. It cannot be empty")
            raise ValueError("Department name cannot be empty!")
        # set department name
        self._name = value