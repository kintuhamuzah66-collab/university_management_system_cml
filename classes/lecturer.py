import logging
logger = logging.getLogger(__name__)

from classes.person import Person

class Lecturer(Person):
    def __init__(self, personal_id, full_name):
        super().__init__(personal_id, full_name)
        