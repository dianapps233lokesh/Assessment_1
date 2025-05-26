class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print(f"Name:{self.name} and Age:{self.age}")

class Student(Person):
    def __init__(self,name,age,section):
        self.section=section
        super().__init__(name,age)
    
    def displayStudent(self):
        print(f"Name:{self.name}\nAge:{self.age}\nSection:{self.section}")


obj=Student("lokesh",20,"dianapps")
obj.displayStudent()