# Abstraction : 
# Abstraction in Python is a fundamental concept in object-oriented programming (OOP) that allows you to define a common interface for a group of related classes. It ensures that all subclasses provide specific implementations for certain methods, hiding the complexity of the implementation details while exposing only essential functionalities.

# import module

# class details(module.printData) : 
#     def __init__(self,fname,lname,age):
#         self.firstname = fname
#         self.lastname = lname 
#         self.age = age 
    

# b1 = details("Raj","Shah",20)

# print(b1.firstname)
# print(b1.lastname)
# print(b1.age)
        
# b1.print()

# from datetime import datetime

# mydate = datetime.now()

# print(mydate.today())



from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    # def area(self):
    #     return self.width * self.height

    # def perimeter(self):
    #     return 2 * (self.width + self.height)
    
# r1 = Rectangle(100,100)

# print(r1.area())
# print(r1.perimeter())