# # Single Level Heritance : 
# # Base Class :      Person 


# # Child Class :      child (inherit Person class)



# class Person : 
#     # class variable
#     fAge = 40 
#     def __init__(self,fname):
#         # instance Variable
#         self.fathername = fname

#     # Method : 
#     def bioData(self):
#         print(f"Person name is {self.fathername}.and Age is {self.fAge}.")


# class Child(Person) : 
#     def __init__(self,fname,cname,age):
#         super().__init__(fname)
#         self.Childname = cname
#         self.cAge = age

# c1 =  Child("Ajaybhai","Raj",20)

# print(c1.Childname)
# print(c1.cAge)
# c1.bioData()

####################################################################
# Multi Level Inheritance : 

# Base Class :    GrandFather 

# Child of Base Class + new Parent Class :  Father  (inherit Grand Father)


# Child of Parent Class : Child (inherit Father)


# class GrandFather : 
#     GrandFatherName = "Rajesh"

#     def bioData(self,v1,v2):
#         print(f"My Name is {v1}.my Age is {v2}.")


# class Father(GrandFather) : 
#     Fathername = "Ajay"

# class Child(Father) : 
#     def __init__(self,cname,age):
#         self.childname = cname
#         self.age = age


c1 = Child("Raj",20)

print(c1.childname)
print(c1.age)
# print(c1.Fathername)
# print(c1.GrandFatherName)



f1  = Father()
# print(f1.Fathername)
# print(f1.GrandFatherName)

g1 = GrandFather() 
# print(g1.GrandFatherName)

g1.bioData(g1.GrandFatherName,70)


f1.bioData(f1.Fathername,45)


c1.bioData(c1.childname,c1.age)