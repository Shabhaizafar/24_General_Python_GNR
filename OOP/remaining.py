# Method overriding and Method Overloading (Not Possible) : 
# Constructuor overriding and Constructuor Overloading (Not Possible) : 

# class Class1 : 
#     def __init__(self):   # Constructor 
#         pass

#     def Data(self):      # Metohd
#         pass


# class Class2(Class1) : 
#     def __init__(self):  # Constructor Overriding
#         pass
    
#     def Data(self):   # Method overriding 
#         pass



# class Father : 
#     def __init__(self):
#         self.Lastname = "Shah"
#         self.age = 40
    
#     def property(self):
#         print("Property Value  : 10000000000000000000")


# class Child(Father) :
#     def __init__(self,cname,age,gender):
#         super().__init__()
#         self.childname = cname
#         self.age = age
#         self.gender = gender
#     def property(self):
#         print("Property Value : 0")

# # c1 = Child()

# # print(c1.childname)
# # print(c1.Lastname)
# # c1.property()

# c1 = Child("Raj",20,"Male")

# print(c1.childname)
# print(c1.age)
# print(c1.gender)
# print(c1.Lastname)

# c1.property()

##################################################
class GrandFather : 
    def __init__(self):
        self.GrandFatherName = "Rajesh"

    def bioData(self,v1,v2):
        print(f"My Name is {v1}.my Age is {v2}.")


class Father(GrandFather) : 
    def __init__(self):
        super().__init__()
        self.Fathername = "Ajay"

class Child(Father) : 
    def __init__(self,cname,age):
        super().__init__()
        self.childname = cname
        self.age = age


c1 = Child("Raj",20)

print(c1.childname)
print(c1.age)
print(c1.Fathername)
print(c1.GrandFatherName)



# GrandFather.bioData("Z")

## get set 
## construct and Method remaining 

