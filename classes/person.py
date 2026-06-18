import logging
logger = logging.getLogger(__name__)

class Person:
    def __init__(self, personal_id, full_name):
        self.personal_id = personal_id
        self.full_name = full_name

    # personal id properties
    @property
    def personal_id(self):
        return self._personal_id
    
    @personal_id.setter
    def personal_id(self, value):
        if not value:
            # log and raise error
            logger.error("Failed to set personal id. personal Id cannot be empty")
            raise ValueError("Id cannot be empty")
        # set id
        self._personal_id = value


    # full name properties
    @property
    def full_name(self):
        return self._full_name
    
    @full_name.setter
    def full_name(self, value):
        if not value:
            # log and raise error
            logger.error("Failed to set full name. full name cannot be empty")
            raise ValueError("Name cannot be empty")
        # set full name
        self._full_name = value