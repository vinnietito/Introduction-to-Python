class Student:
    """A class representing a student"""
    def __init__(self, n, a):
        self.full_name = n
        self.age = a
        
    def get_age(self):
        return self.age
    
    
# Derived class
class BIT_student(Student):
    """A class extending Student."""
    def __init__(self, n, a):
        super().__init__(n, a)
        self.department_num = d
        