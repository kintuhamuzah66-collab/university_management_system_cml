class Person:
    def __init__(self, id, first_name, last_name, other_name=None):
        self._id = id
        self._first_name = first_name
        self._last_name = last_name
        self._other_name = other_name

    # id propery and setter
    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, new_id):
        if not new_id:
            raise ValueError("Id cannot be empty")
        if len(new_id) < 7:
            raise ValueError("ID cannot be less that 7 characters")
        
        self._id = new_id

    # first name property and setter
    @property
    def first_name(self):
        return self._first_name
    
    @first_name.setter
    def first_name(self, f_name):
        if not f_name:
            raise ValueError("First name cannot be empty")
        if " " in f_name or not f_name.isalpha():
            raise ValueError("First name can only contain letters")
        
        self._first_name = f_name

    # last name getter and setter
    @property
    def last_name(self):
        return self._last_name
    
    @last_name.setter
    def last_name(self, l_name):
        if not l_name:
            raise ValueError("Last name cannot be empty")
        if " " in l_name or not l_name.isalpha():
            raise ValueError("Last name name can only contain letters")
        
        self._first_name = l_name

    # other name getter and setter
    @property
    def other_name(self):
        return self._other_name
    
    @other_name.setter 
    def other_name(self, oth_name):
        if oth_name is None:
            self._other_name = None
            return
    
        if " " in oth_name or not oth_name.isalpha():
            raise ValueError("Other name can only contain letters")
        
        self._other_name = oth_name