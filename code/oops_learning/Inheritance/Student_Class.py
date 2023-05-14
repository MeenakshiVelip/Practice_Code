class Student: 
    # A class named Student
    def __init__(self,fname,lname,age) -> None:  #__init__ is a constructor
        # instance of the class
        self.fname = fname
        self.lname = lname
        self.age = age
stud=Student("Meenakshi","B",22)        # Student(stud,"Meenakshi","B",22)
# creating an object named stud
print(stud.__dict__) 
# prints the data in the form of key and value