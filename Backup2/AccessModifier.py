#  Public , private,protected : 

# # Public Access Modifier: 
# # Theoretically, public methods and fields can be accessed directly by any class.

# Protected Access Modifier:
# Theoretically, protected methods and fields can be accessed within the same class it is declared and its subclass.


# class Person:
#     def __init__(self,fname,lname):
#         self.firstname = fname
#         self.lastname = lname

#     def display(self):
#         print(f'Your name is {self.firstname} {self.lastname}')

    
# p1  = Person("Raj","Shah")

# print(p1.firstname)
# print(p1.lastname)



class Person : 
    firstname = "Raj"
    _lastname = "Shah"
    __age = 12

    def display(self):
        print(f'Your name is {self.firstname} {self._lastname}')
    
    def _display(self):
        print(f'Your name is {self.firstname} {self._lastname}')

    def __display(self):
        print(f'Your name is {self.firstname} {self._lastname}')

class Child (Person) : 
    pass

p1 = Person()

print(p1.firstname)
print(p1._lastname)
p1.display()
print(p1.__age)
# p1._display()
# p1.__display()



print(dir(p1))
