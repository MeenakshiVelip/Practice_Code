class Parent_Student: # A Parent/Base class named Student
    def __init__(self,fname,lname,age) -> None: # instance of the class
        self.fname = fname
        self.lname = lname
        self.age = age

class Child_Student(Parent_Student): # A child/Derived class named Child_Student
     def __init__(self,fname,lname,age,USN) -> None: # instance of the class
        self.fname = fname
        self.lname = lname
        self.age = age
        self.USN = USN
stud=Parent_Student("Meenakshi","B",22)    
print(stud.__dict__)  # prints the data in the form of key and value    