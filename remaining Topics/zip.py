# myTuple1 = (1,2,3,4)
# myTuple2 = ("Zafar","Raj","Shah","Ajay")


# print(myTuple1)
# print(myTuple2)

# ans  = zip(myTuple1,myTuple2)  #object
# print(tuple(ans))
# print(set(tuple(ans)))
# print(list(ans))
# print(dict(ans))
# print(str(tuple(ans)))





# ( 
#  )
#####################
# zip > set 
# zip > list 
# zip > dict 



# partition ,translate ,maketrans


# from functools import reduce

# myList = [11,12,13,14,15]

# print(myList)


# ans  =  reduce(lambda a,b : a+b,myList,0)

# # print(ans)

# //////////////////////
# partition :
# The partition() method splits a string into three parts based on a specified separator. It returns a tuple containing:

# The part before the separator.
# The separator itself.
# The part after the separator.
# Syntax:
# string.partition(separator)

# myStr = "Royal Technosoft pvt ltd"
# print(myStr)
# ans = myStr.partition(" ")
# print(ans)



# maketrans : 
# The str.maketrans() method is used to create a translation table for character replacements. It works with the translate() method.

# Syntax:
# str.maketrans(x[, y[, z]])
# Parameters:
# x: A dictionary mapping characters to their replacements, or a string specifying characters to replace.
# y (optional): A string specifying replacement characters (used if x is a string).
# z (optional): A string specifying characters to delete.


myStr = "Royal"

ans= myStr.maketrans("ZAFAR")
print(ans)

# Z : # translate 

