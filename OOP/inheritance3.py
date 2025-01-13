# 1 : Single Level Inheritance.
# Base Class : Person (Parent Class)
                # |
                # |
# Child Class : Child   (inherit Person)
#################################################################
# 2 : Multi Level Inheritance.
# Base Class :                   GrandFather (Parent Class)
                                  # |
                                  # |
# Child Class/Next Parent Class : Father   (inherit GrandFather)
                                 # |
                                 # |
# Child Class :                   Child  (inherit Father)
#################################################################
# 3 :  Multiple Inheritance.

# Base Class 1 :                  Father    (Parent class1)
                                  # |
                                  # |
# Base Class 2 :             Mother )       (Parent class2)
                            #   |   | 
                            #   |   |
# Child Class :                 Child (inherit Father and Mother)

# class Father : 
#     def __init__(self,fname,lname):
#         self.Fathername = fname
#         self.Lastname = lname


# class Mother : 
#     def __init__(self,mname,lname):
#         self.Mothername = mname
#         self.Lastname = lname

# class Child (Father,Mother): 
#     def __init__(self,cname,lname,fname,mname):
#         Father.__init__(self,fname,lname)
#         Mother.__init__(self,mname,lname)
#         self.Childname = cname

#     def bioData(self):
#         print(f"My name is {self.Childname} {self.Fathername} {self.Lastname}.My Mother name is {self.Mothername}.")
    


# c1 = Child("Raj","Shah","Rajeshbhai","Savitaben")

# c1.bioData()



########################################################################
"""
---

### 1. **Single-Level Inheritance**
**Problem:**  
A school has teachers and students. Each person has a name and an ID. Teachers have an additional attribute, `subject`, which indicates what they teach. Create a Python program using single-level inheritance to represent this relationship and demonstrate how a teacher can introduce themselves, including their subject.

---

### 2. **Multi-Level Inheritance**
**Problem:**  
A vehicle manufacturing company has different types of vehicles. The base class `Vehicle` contains common attributes like `brand` and `model`. The class `Car` inherits from `Vehicle` and adds attributes like `number_of_doors`. The class `ElectricCar` further inherits from `Car` and adds an attribute `battery_capacity`. Write a Python program using multi-level inheritance to model this hierarchy and demonstrate creating an electric car and displaying its details.

---

### 3. **Multiple Inheritance**
**Problem:**  
A company has employees who can either be engineers, managers, or both. An `Employee` class contains common details like `name` and `employee_id`. An `Engineer` class has an attribute `specialization`, and a `Manager` class has an attribute `department`. Create a Python program using multiple inheritance to represent an employee who is both an engineer and a manager, and display their details.

---
"""