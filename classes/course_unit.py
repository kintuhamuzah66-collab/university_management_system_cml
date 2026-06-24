import logging
logger = logging.getLogger(__name__)

class CourseUnit:
    def __init__(self, code, name):
        self.code = code
        self.name = name

        self._enrolled_student_ids = []
        self._lecturer_ids = []

    # code properties
    @property
    def code(self):
        return self._code 
    
    @code.setter
    def code(self, value):
        if not value or not str(value).strip():
            # log and raise error
            logger.error("Failed to set course unit code. It cannot be empty")
            raise ValueError("Course unit code cannot be empty")
        # set course unit code
        self._code = value

    # name properties
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not value or not str(value).strip():
            #log and raise error
            logger.error("Failed to set course unit name. It cannot be empty")
            raise ValueError("Course unit name cannot be empty")
        # set course unit name
        self._name = value

    # enrolled student ids properties
    @property
    def enrolled_student_ids(self):
        return tuple(self._enrolled_student_ids)
        
    def enroll_student(self, student_id):
        if not student_id or not str(student_id).strip():
            # log and raise error
            logger.error("Failed to enroll student. Student id to be enrolled cannot be empty")
            raise ValueError("Student id to be enrolled cannot be empty")
        # enroll student
        self._enrolled_student_ids.append(student_id)

    # lecturer ids properties
    @property 
    def lecturer_ids(self):
        return self._lecturer_ids
    
    def taught_by(self, lecturer_id):
        if not lecturer_id or not str(lecturer_id).strip():
            # log and raise error
            logger.error("Failed to add lecturer id to lecturer ids. lecturer_id cannot be empty")
            raise ValueError("Lecturer id cannot be empty")
        # add lecturer id to lecturer ids list
        self._lecturer_ids.append(lecturer_id)