# Hierarchical inheritance : 

# in Python is a type of inheritance where more than one child class is derived from a single parent class.

# class Vehicle: 
#     def __init__(self):
#         pass
#     def printData(self) : 
#         print(f"Vehicle Class : Wheele :{self.tyre}")


# class Car(Vehicle): 
#     tyre = 4
#     def __init__(self,clr):
#         self.color = clr 

# class Bike(Vehicle):
#     tyre = 2
#     def __init__(self,clr):
#         self.color = clr 

        

# c1 = Car("Blue")

# print(c1.color)
# c1.printData()


# b1 = Bike("Red")
# print(b1.color)
# b1.printData()


# ====================================================
# Hybrid inheritance : 

# in Python is a combination of multiple types of inheritance, such as single, multiple, multilevel, and hierarchical. 


# class Human: 
#     def __init__(self):
#         pass
#     def data(self):
#         print("Human Class!!!")


# class Boy(Human):
#     def __init__(self):
#         pass

#     def play(self): 
#         print("Playing Cricket")
        
# class Girl(Human):
#     def __init__(self):
#         pass

#     def speak(self): 
#         print("Speak Normaly like a Woman.")
#     def play(self): 
#         print("Playing KHOKHO")
        
# class Hybrid(Girl,Boy): 
#     def __init__(self):
#         pass


# h1 =  Hybrid()
# h1.speak()
# h1.play()
# h1.data()
# ==========================================



