# Object Oriented Programming is a fundamental concept in Python, empowering developers to build modular, maintainable, and scalable applications. By understanding the core OOP principles (classes, objects, inheritance, encapsulation, polymorphism, and abstraction), programmers can leverage the full potential of Python OOP capabilities to design elegant and efficient solutions to complex problems.

# OOPs is a way of organizing code that uses objects and classes to represent real-world entities and their behavior. In OOPs, object has attributes thing that has specific data and can perform certain actions using methods.


#=>  OOPs Concepts in Python : 

# Class in Python
# Objects in Python
# Polymorphism in Python
# Encapsulation in Python
# Inheritance in Python
# Data Abstraction in Python


#=>  Python Class : 
# A class is a collection of objects. Classes are blueprints for creating objects. A class defines a set of attributes and methods that the created objects (instances) can have.

#=>  Some points on Python class:  

# Classes are created by keyword class.
# Attributes are the variables that belong to a class.
# Attributes are always public and can be accessed using the dot (.) operator. Example: Myclass.Myattribute.

# /////////

# object  == dict

# How to create a single Object or dict : 
# empty dict
# dictname = {}

# dictname = {
#     "fname" : "Raj"
# }

# empty dict
# dictname = dict()


# students  :  


# stu1 = {
#     "fname" : 1,
#     "lname" : 1,
#     "age" : 1,
#     "std" : 1,
#     "rollno" : 1
# }


#=>  How to Create a Class : 

class Student : 
    def __init__(Zafar,fname,lname):
        Zafar.Firstname = fname;
        Zafar.Lastname = lname;



# print(type(Student))

st1 = Student("Raj","Shah")
st2 = Student("Ajay","Patel")


print(st1.Firstname)
print(st2.Firstname)






