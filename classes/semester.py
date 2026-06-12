class Semester:
    def __init__(self, semester_id, academic_year):
        self._semester_id = semester_id
        self._academic_year = academic_year

    # semester id getter and setter
    @property
    def semester_id(self):
        return self._semester_id    
    
    @semester_id.setter
    def semester_id(self, id):
        if not id:
            raise ValueError("Semester ID cannot be empty")
        if " " in id or not id.isnum():
            raise ValueError("Semester ID can only contain numbers")

        self._semester_id = id

    # academic year getter and setter
    @property
    def academic_year(self):
        return self._academic_year
    
    @academic_year.setter
    def academic_year(self, year):
        if not year:
            raise ValueError("Academic year cannot be empty")
        if " " in year or not year.isnum():
            raise ValueError("Academic year can only contain numbers")

        self._academic_year = year