# class GrandFather : 
#     def __init__(self):
#         self.GrandFatherName = "Rajesh"

#     def bioData(self,v1,v2):
#         print(f"My Name is {v1}.my Age is {v2}.")


# class Father(GrandFather) : 
#     def __init__(self):
#         super().__init__()
#         self.Fathername = "Ajay"

# class Child(Father) : 
#     def __init__(self,cname,age):
#         super().__init__()
#         self.childname = cname
#         self.age = age


# c1 = Child("Raj",20)

# print(c1.childname)
# print(c1.age)
# print(c1.Fathername)
# print(c1.GrandFatherName).



# class class1:
#     class1name = "Person1"

# class class2(class1):
#     def __init__(self):
#         self.class2name = "ChildClass"


# obj1 = class2()

# print(obj1.class1name)
# print(obj1.class2name)



# class class1:
#     def __init__(self):
#         self.class1name = "Person1"

# class class2(class1):
#     def __init__(self):
#         super().__init__()
#         self.class2name = "ChildClass"


# obj1 = class2()

# print(obj1.class1name)
# print(obj1.class2name)




# class class1:
#     def __init__(self,cname):
#         self.class1name = cname

# class class2(class1):
#     def __init__(self,cname):
#         super().__init__(cname)
#         self.class2name = "ChildClass"


# obj1 = class2("Person")

# print(obj1.class1name)
# print(obj1.class2name)



# class class1:
#     class1name = "Person1"

# class class2:
#     class2name = "Person2"

# class class3(class1,class2):
#     class3name = "Child Class"


# obj1 = class3()

# print(obj1.class1name)
# print(obj1.class2name)
# print(obj1.class3name)


# Multiple : self :required
# class class1:
#     def __init__(self):
#         self.class1name = "Person1"

# class class2:
#     def __init__(self):
#         self.class2name = "Person2"

# class class3(class1,class2):
#     def __init__(self):
#         class1.__init__(self)
#         class2.__init__(self)
#         self.class3name = "Child Class"


# obj1 = class3()

# print(obj1.class1name)
# print(obj1.class2name)
# print(obj1.class3name)


# class class1:
#     def __init__(self,c1):
#         self.class1name = c1

# class class2:
#     def __init__(self,c2):
#         self.class2name = c2

# class class3(class1,class2):
#     def __init__(self,c1,c2):
#         class1.__init__(self,c1)
#         class2.__init__(self,c2)
#         self.class3name = "Child Class"


# obj1 = class3('Person1',"Person2")

# print(obj1.class1name)
# print(obj1.class2name)
# print(obj1.class3name)



# loading 
class class1: 
    def __init__(self):
        self.cname = "class1"

    def __init__(self):
        self.cname = "class2"
    
    def add(self):
        print("a")
    def add(self,v1):
        print("z",v1)

obj = class1()
print(obj.cname)


obj.add()

