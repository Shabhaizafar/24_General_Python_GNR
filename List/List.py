# Python Lists are just like dynamically sized arrays, declared in other languages (vector in C++ and ArrayList in Java). In simple language, a list is a collection of things, enclosed in [ ] and separated by commas. 

# The list is a sequence data type which is used to store the collection of data.
# How to Create Empty List in a Python : 

# myList = []  # List 
# print(myList)

# Numbers
# myList1 = [1,2,3,4,5,6]
# print(myList1)

# String 
# myList2 = ["Zafar","Raj","Ajay"]
# print(myList2)

# Boolean 
# myList3 = [True,False]
# print(myList3)


# Mix All
# myList4 = [1,2,"Zafar",True]
# print(myList4)

# print(type(myList4))   # <class 'list'>


# myList = [1,1,1,1,1]
# print(myList)

# length   : Data ? 
# len()  : sequence data type[List,Tuple,Dict,String] (workable)
        # Number[int,float,complex],Boolean  (not workable)

# length   1 2    3      4
# myList4 = [1,2,"Zafar",True,"Royal"]
# index    0 1   2      3
# print(myList4)
# print(len(myList4))
# print(myList4[2])
# print(myList4[4])  #  IndexError: list index out of range

# How to Find Range Specific Type  :   Index range = len(seqvariableName)-1
                                        #          = len(myList)-1
                                        #          = 4  - 1
                                        #          = 3
# How to Access Last Value : 
# print(myList4[len(myList4)-1])


#########################################
# List Methods : 
myList = [11,12,13,14,"Royal","Techno","soft",True]
print(myList)

# 1) append :  Add Newdata 
# myList.append("NewOne") # Valid
# myList.append("NewOne","NewTwo") #TypeError: list.append() takes exactly one argument (2 given)
# print(myList)

# 2) remove :  remove Specific Data (Value as an argument)(not Index)
# myList.remove(11)
# myList.remove(15) # ValueError : list.remove(x): x not in list

# print(myList)


# 10 to 11 AM 
