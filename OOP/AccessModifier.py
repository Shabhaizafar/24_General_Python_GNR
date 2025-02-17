# # Python does not have built-in access modifiers like private, protected, and public as found in languages such as C++ or Java. Instead, Python uses naming conventions to emulate these behaviors. By default, all class members are public and can be accessed from anywhere in the program.


# # Public Access Modifier: 
# # Theoretically, public methods and fields can be accessed directly by any class.

# class Person : 
#     def __init__(self):
#         self.Persondata = "Person Class"

#     def printData(self):
#         print(self.Persondata)

# class Child(Person) : 
#     def __init__(self):
#         super().__init__()
#         self.Childdata = 'Child Class'
    

# obj1 = Child()

# print(obj1.Childdata)

# obj1.printData()

# print(dir(obj1))


# Protected Access Modifier:
# Theoretically, protected methods and fields can be accessed within the same class it is declared and its subclass.


# class Person : 
#     _Persondata = None
#     def __init__(self,fname):
#         self._Persondata = fname

#     def _printData(self):
#         print(self._Persondata)

# class Child(Person) : 
#     def __init__(self,fname,cname):
#         super().__init__(fname)
#         self.Childdata = cname

#     def printdata(self):
#         print(self.Childdata,self._Persondata)


# obj1 = Child("Person Main","Child Class")

# print(obj1.Childdata)
# print(obj1._Persondata)

# print(dir(obj1))



# ##########################################
# 1. Write a Python program to create a class representing a Circle. Include methods to calculate its area and perimeter.
# Click me to see the sample solution

# 2. Write a Python program to create a person class. Include attributes like name, country and date of birth. Implement a method to determine the person's age.
# Click me to see the sample solution

# 3. Write a Python program to create a calculator class. Include methods for basic arithmetic operations.
# Click me to see the sample solution

# 4. Write a Python program to create a class that represents a shape. Include methods to calculate its area and perimeter. Implement subclasses for different shapes like circle, triangle, and square.
# Click me to see the sample solution

# 5. Write a Python program to create a class representing a binary search tree. Include methods for inserting and searching for elements in the binary tree.
# Click me to see the sample solution


# dob =  "12-12-2023"
# from datetime import datetime  as dt

# data = dt.today()
# print(data.date())


# 6. Write a Python program to create a class representing a stack data structure. Include methods for pushing and popping elements.
# Click me to see the sample solution

# 7. Write a Python program to create a class representing a linked list data structure. Include methods for displaying linked list data, inserting and deleting nodes.
# Click me to see the sample solution

# 8. Write a Python program to create a class representing a shopping cart. Include methods for adding and removing items, and calculating the total price.
# Click me to see the sample solution

# 9. Write a Python program to create a class representing a stack data structure. Include methods for pushing, popping and displaying elements.
# Click me to see the sample solution

# 10. Write a Python program to create a class representing a queue data structure. Include methods for enqueueing and dequeueing elements.
# Click me to see the sample solution

# 11. Write a Python program to create a class representing a bank. Include methods for managing customer accounts and transactions.
