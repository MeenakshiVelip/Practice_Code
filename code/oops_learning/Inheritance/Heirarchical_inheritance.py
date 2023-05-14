class Parent_Student: # Super Class
    def __init__(self,fname,lname,age) -> None: # instance of the class
        self.fname = fname
        self.lname = lname
        self.age = age

class Child_Student1(Parent_Student): # First child class named Child_Student1
     def __init__(self,fname,lname,age) -> None: # self is an instance of the class
        self.fname = fname
        self.lname = lname
        self.age = age

class Child_Student2(Parent_Student): # Second child class named Child_Student2
     def __init__(self,fname,lname,age) -> None: # Self is an instance of the class
        self.fname = fname
        self.lname = lname
        self.age = age
        
stud1=Parent_Student("Meenakshi","B",22) 
stud2=Parent_Student("Smita","B",26)    
print(stud1.__dict__)  # prints the data in the form of key and value    
print(stud2.__dict__)