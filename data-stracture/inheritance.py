
class Student:
    def __init__(self, name, rollno, grade ):
        self.name=name
        self.rollno=rollno
        self.grade=grade
    def display (self):
        print (f"student name:{self.name}\nstdent roll no:{self.rollno}\ngrade:{self.grade}")
class Teacher(Student):
       def __init__(self, name, rollno, grade, teacher, salary):
           super().__init__(name, rollno, grade )
           self.teacher=teacher
           self.salary=salary
       def display ():
            super().display(self)
            print (f"teacher name:{self.teacher}\nteacher salary:{self.salary}")
sre=Student("Phone",45,"p")      
sre.display()
sd=Teacher("jeshan",33,"A","wagh",39860)
sd.display()