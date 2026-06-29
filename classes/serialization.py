import json
import logging

logger = logging.getLogger(__name__)

class AcademicRegistrarEncoder(json.JSONEncoder):
    """
    Serializes the full AcademicRegistrar object graph to JSON.
    Handles: AcademicRegistrar, Department, Course, CourseUnit, Student, Lecturer.
    """

    def default(self, obj):
        # Lazy imports to respect your TYPE_CHECKING / circular import pattern
        from classes.registrar import AcademicRegistrar
        from classes.department import Department
        from classes.course import Course
        from classes.course_unit import CourseUnit
        from classes.student import Student
        from classes.lecturer import Lecturer

        if isinstance(obj, AcademicRegistrar):
            return {
                "__type__": "AcademicRegistrar",
                # list() unwraps the tuples your properties return
                "departments": list(obj.departments),
                "students":    list(obj.students),
                "lecturers":   list(obj.lecturers),
            }

        if isinstance(obj, Department):
            return {
                "__type__": "Department",
                "name":    obj.name,
                "courses": list(obj.courses),   # encoder recurses into each Course
            }

        if isinstance(obj, Course):
            return {
                "__type__":    "Course",
                "code":        obj.code,
                "name":        obj.name,
                "department":  obj.department,
                "course_units": list(obj.course_units),  # encoder recurses into each CourseUnit
            }

        if isinstance(obj, CourseUnit):
            return {
                "__type__":            "CourseUnit",
                "code":                obj.code,
                "name":                obj.name,
                # tuples → lists so JSON can handle them
                "enrolled_student_ids": list(obj.enrolled_student_ids),
                "lecturer_ids":         list(obj.lecturer_ids),
            }

        # Student before Person — check the more specific type first
        if isinstance(obj, Student):
            return {
                "__type__":   "Student",
                "personal_id": obj.personal_id,
                "full_name":   obj.full_name,
                "major":       obj.major,
            }

        if isinstance(obj, Lecturer):
            return {
                "__type__":    "Lecturer",
                "personal_id": obj.personal_id,
                "full_name":   obj.full_name,
            }

        # Always fall through to super for unknown types
        return super().default(obj)
    
def academic_registrar_decoder(dct):
    """
    Reconstructs the full object graph from JSON.
    object_hook is called bottom-up — inner objects are already
    reconstructed by the time outer ones are processed.
    So CourseUnit is built before Course, Course before Department, etc.
    """
    from classes.registrar import AcademicRegistrar
    from classes.department import Department
    from classes.course import Course
    from classes.course_unit import CourseUnit
    from classes.student import Student
    from classes.lecturer import Lecturer

    t = dct.get("__type__")

    if t == "CourseUnit":
        unit = CourseUnit(
            code=dct["code"],
            name=dct["name"],
        )
        # Re-enroll students using the public method — keeps validation intact
        for student_id in dct.get("enrolled_student_ids", []):
            unit.enroll_student(student_id)
        # Re-attach lecturers using the public method
        for lecturer_id in dct.get("lecturer_ids", []):
            unit.taught_by(lecturer_id)
        return unit

    if t == "Course":
        course = Course(
            code=dct["code"],
            name=dct["name"],
            department=dct["department"],
        )
        # dct["course_units"] is already a list of CourseUnit objects
        # because object_hook processes inner dicts first
        for unit in dct.get("course_units", []):
            course.add_course_unit(unit)
        return course

    if t == "Department":
        department = Department(name=dct["name"])
        # dct["courses"] is already a list of Course objects
        for course in dct.get("courses", []):
            department.add_course(course)
        return department

    if t == "Student":
        return Student(
            personal_id=dct["personal_id"],
            full_name=dct["full_name"],
            major=dct["major"],
        )

    if t == "Lecturer":
        return Lecturer(
            personal_id=dct["personal_id"],
            full_name=dct["full_name"],
        )

    if t == "AcademicRegistrar":
        registrar = AcademicRegistrar()
        # dct["departments"] / ["students"] / ["lecturers"] are already
        # fully reconstructed object lists at this point
        for department in dct.get("departments", []):
            registrar.register_department(department)
        for student in dct.get("students", []):
            registrar.register_student(student)
        for lecturer in dct.get("lecturers", []):
            registrar.register_lecturer(lecturer)
        return registrar
    