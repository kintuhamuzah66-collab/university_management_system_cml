from typing import TYPE_CHECKING
import logging
logger = logging.getLogger(__name__)

if TYPE_CHECKING:
    from classes.student import Student
    from classes.lecturer import Lecturer
    from classes.department import Department
    from classes.course import Course
    from classes.course_unit import CourseUnit

class AcademicRegistrar():
    def __init__(self):
        self._departments = []
        self._students = []
        self._lecturers = []

    @property
    def departments(self):
        return tuple(self._departments)
    
    @property
    def students(self):
        return tuple(self._students)
    
    @property
    def lecturers(self):
        return tuple(self._lecturers)
    
    def get_student(self, p_id):
        """Searches for a student by id"""
        try:
            # Use self._students directly for slight performance, or keep self.students
            search_student = (s for s in self._students if s.personal_id == p_id)
            student = next(search_student, None) 
            if student:
                logger.info(f"Student {student.full_name} is found")
                return student 
            else:
                logger.warning(f"Student not found!")
                return False
        except Exception:
            logger.exception("Something went wrong!")
            return False

    def get_department(self, name):
        """Searches for a department by name"""
        try:
            search_department = (d for d in self._departments if d.name == name)
            department = next(search_department, None)

            if department:
                logger.info(f"Department with name: {department.name} successfully found")
                return department
            else:
                logger.warning(f"Department with name {name} not found!")
                return False
        except Exception:
            logger.exception("Something went wrong")
            return False

    def get_lecturer(self, p_id):
        """Searches for a lecturer by id"""
        try:
            search_lecturer = (l for l in self._lecturers if l.personal_id == p_id)
            lecturer = next(search_lecturer, None)

            if lecturer:
                logger.info(f"Lecturer with ID: {lecturer.personal_id} successfully found!")
                return lecturer
            else:
                logger.warning(f"Lecturer with ID: {p_id} not found!")
                return False
        except Exception:
            logger.exception("Something went wrong!")
            return False

    # REGISTRATION CORNER
    def register_student(self, student: 'Student'):
        """Registers new student"""
        try:
            if student in self._students:
                logger.warning(f"{student.full_name} cannot be registered twice!")
                return False
            
            # Check if the course exists in ANY department
            for department in self._departments:
                for course in department.courses:
                    if course.code == student.major:
                        self._students.append(student)  
                        logger.info("Student successfully registered to university")
                        return True
            logger.warning(f"Course {student.major} not available")
            return False
        except Exception:
            logger.exception("Something went wrong!")
            return False
        
    def register_lecturer(self, lecturer: 'Lecturer'):
        """Registers new lecturer"""
        try:
            if lecturer in self._lecturers:
                logger.warning(f"Adding lecturer skipped. {lecturer.full_name} already exists!")
                return False
            else:
                self._lecturers.append(lecturer)  
                logger.info("Lecturer successfully registered")
                return True
        except Exception:
            logger.exception("Something went wrong!")
            return False  
    
    def register_department(self, department: 'Department'):
        """Adds a new department"""
        try:
            if department in self._departments:
                logger.warning(f"Department addition skipped. {department.name} already exists")
                return False
            else:
                self._departments.append(department)  
                logger.info(f"{department.name} successfully added to departments")
                return True
        except Exception:
            logger.exception("Something went wrong")
            return False
        
    def add_course_to_dep(self, course: 'Course'):
        """Adds course to department"""
        try:
            department: Department = self.get_department(course.department)
            if department:
                department.add_course(course)
                logger.info("Course successfully added to department")
                return True
        except Exception:
            logger.exception("Something went wrong!")
            return False
        
    def show_department_courses(self, dep_name: str):
        """Shows the courses offered by a department"""
        try:
            department: 'Department' = self.get_department(dep_name)
            if department:
                if len(department.courses) == 0:
                    logger.warning("Department has no courses yet")
                    return False
                logger.info("Returned department courses")
                return department.courses
        except Exception:
            logger.exception("Something went wrong!")
            return False
        
    def add_course_unit_to_course(self, dep_name, course_code, course_unit: 'CourseUnit'):
        """Adds course unit to a department course"""
        try:
            department: 'Department' = self.get_department(dep_name)
            if department:
                for course in department.courses:
                    if course.code == course_code:
                        if course_unit not in course.course_units:
                            course.add_course_unit(course_unit)
                            logger.info(f"{course_unit.name} successfully added to {department.name} courses")
                            return True
                        logger.warning(f"{course_unit.name} already exists!")
                        return False
        except Exception:
            logger.exception("Something went wrong")
            return False
                        
    def show_course_units_in_dep_course(self, dep_name, course_code):
        """returns course units in department course"""
        try:
            department: 'Department' = self.get_department(dep_name)
            if department:
                for course in department.courses:
                    if course.code == course_code:
                        logger.info(f"{course.name} successfully found in {department.name}")
                        return course.course_units
            else:
                logger.warning("Department not found!")
                return False
        except Exception:
            logger.exception("Something went wrong!")
            return False
        
