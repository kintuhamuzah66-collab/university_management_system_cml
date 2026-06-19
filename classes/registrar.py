from typing import TYPE_CHECKING
import logging
logger = logging.getLogger(__name__)

if TYPE_CHECKING:
    from classes.student import Student
    from classes.lecturer import Lecturer

class AcademicRegistrar():
    def __init__(self):
        self.departments = []
        self.students = []
        self.lecturers = []

    