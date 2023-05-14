class Parent_Student1: # Parent Class
    def __init__(self,fname,lname,age) -> None: # instance of the class
        self.fname = fname
        self.lname = lname
        self.age = age

class Parent_Student2: # Parent Class
     def __init__(self,fname,lname,age) -> None: # self is an instance of the class
        self.fname = fname
        self.lname = lname
        self.age = age

class Child_Student(Parent_Student1,Parent_Student2): # Child Class
     def __init__(self,fname,lname,age) -> None: # Self is an instance of the class
        self.fname = fname
        self.lname = lname
        self.age = age
        
stud1=Parent_Student1("Meenakshi","B",22) 
stud2=Parent_Student2("Smita","B",26)    
print(stud1.__dict__)  # prints the data in the form of key and value    
print(stud2.__dict__)