"""Class Object Constructor Attributes Methods"""

class Student:
    
    def __init__(self, name, id):
        self.name = name
        self.id = id
        print("a student object created")


s1 = Student("Rakib", 11)
s2 = Student("Enam", 12)

print("s1:", s1)
print("s2:", s2)    