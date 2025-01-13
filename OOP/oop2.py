# How to create a class : 
# class Student:
#     def __init__(self,fname,lname):
#         self.Firstname = fname
#         self.Lastname = lname
        

# # How to Create an Object using Class : 
# st1 = Student("Ajay","Shah")
# st2 = Student("Rajesh","Patel")


# print(st1.Firstname)
# print(st1.Lastname)
# print(st2.Firstname)
# print(st2.Lastname)


# //##########################################
# Class Variable and Instance Variable.

class Student:
    # Class Variable
    Age = 12
    def __init__(self,fname,lname):
        #Instance Variable
        self.Firstname = fname
        self.Lastname = lname
        
st1 = Student("Ajay","Shah")
st2 = Student("Rajesh","Patel")


# print(st1.Firstname)
# print(st1.Lastname)
# print(st1.Age)
# print(st2.Firstname)
# print(st2.Lastname)
# print(st2.Age)


# How to Change/Update entity Value 
# st1.Age = 100
# print(st1.Age)
# print(st2.Age)


# print(st1)  # <__main__.Student object at 0x000001BE54156120>
# print(type(st1)) # <class '__main__.Student'>
