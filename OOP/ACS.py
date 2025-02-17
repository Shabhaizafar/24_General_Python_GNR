# Public Access Modifier:
# Theoretically, public methods and fields can be accessed directly by any class.

# Protected Access Modifier: 
# Theoretically, protected methods and fields can be accessed within the same class it is declared and its subclass.

# Private Access Modifier: 
# Theoretically, private methods and fields can be only accessed within the same class it is declared.

class Person : 
    __properties = None
    __position = None

    def __init__(self,properties,position):
        self.__properties = properties
        self.__position = position
        
    
    def __details(self):
        print("Property : ",self.__properties)
        print("Position : ",self.__position)

    def detailsdata(self):
        print("Property : ",self.__properties)
        print("Position : ",self.__position)



obj = Person("100000000","Developer")

# print("Info :  ")
# print(obj.__properties)
# print(obj.__position)
# print("Details Method : ")
# obj.__details()
# print("Detailsdata Method : ")
# obj.detailsdata()



# print("Info :  ")
# obj.__details()

# print(dir(obj))

# print(obj._Person__properties)

# str = "Royal"

# print(dir(str))

# print(dir([11,12,13,14]))