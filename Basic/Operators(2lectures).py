# Boolean :   data type 
# True ,False 

# v  = True 
# print(v)
# print(type(v))


# Arithmatic  : 
# +,-,*,/,%,**(power),// floor division

# Numbers : 
# n1 = 12
# n2 = 2

# print("Addition :",n1+n2)   #  14
# print("Sub : ",n1-n2)   # 10
# print("Mul :",n1*n2)    # 24
# print("Div : ",n1/n2)   #  6.0  float

# print("Floor Div :",n1//n2)  # 6   int 
# print("Pow :",n1**n2)   # power

# print(pow(n1,n2))  # pow Function 

# Boolean :

# v1 = True 
# v2 = "Z"

#  True : 1    False : 0
# print(v1+v2)  # error



# v = True
# print(int(v))
# print(float(v))
# print(type(str(v)))


# v1 = 12
# v2 = "Z"
# print(v2+v1)



# print("Zafar"*4)

# print(True*4)

# print("Zafar"*True)





#################################################

# relational
# <,>,<=,>=,==,!=
# n1 = 12
# n2 = 13

# print(n1<n2)  # True  
# print(n1>n2)  # F     
# print(n1<=n2)  # T   
# print(n1>=n2)  # F   
# print(n1!=n2)  # T
# print(n1==n2)  # F

# Error
# n1 = "Z"
# n2 = 2
# print(n1<n2)   
# print(n1>n2)       
# print(n1<=n2)     
# print(n1>=n2)     
# print(n1!=n2)  
# print(n1==n2)  



# Follow ASCII Value 
# n1 = "Z"
# n2 = "A"

# print(n1<n2)    
# print(n1>n2)     
# print(n1<=n2)    
# print(n1>=n2)     
# print(n1!=n2)  
# print(n1==n2)



# //Error   
# n1 = "Z"
# n2 = True

# print(n1<n2)   
# print(n1>n2)     
# print(n1<=n2)    
# print(n1>=n2)    
# print(n1!=n2)
# print(n1==n2) 


# In a Relational Op / Comparission Op : 
# Must be Check Type are same or not 
#   if Yes  then Check speciafic Logic  else showing Error 
#################################################

# logical : 
# and ,or, not
 # if Both equestions are True then Return True else return False.

# v1 = 12
# v2 = ""

# print(v2 and v1)


# print(bool(v2))


# or  : 
# if Both Equations are False then return False else return True.

# v1 = 0
# v2 = "" 

# print(v1 or v2)

# not : 
# n1 = 13
# print(not n1)

# n1 = 13
# n2 = False
# n3 = 0 
# n4 = "Royal"
# print((n1 and n2) or (n3 and n4) and (not n4)) # 0
  #         False     or    0       and    False

 #                   0 and False
#                     0 



v1 = " "
v2  = "Zafar"
v3 = None
v4 = 0
v5 = False


# print(bool(None))  # False
print((v2 and v5) or (v1 or v3) and (not v3) or (v1 and v2) or (v3 and v5) or (not v1))

print(type((v2 and v5) or (v1 or v3) and (not v3) or (v1 and v2) or (v3 and v5) or (not v1)))

# (v2 and v5) or (v1 or v3) and (not v3) or (v1 and v2) or (v3 and v5) or (not v1)



##############################################

# assigmnent :
# =,+=,-=,*=,/=,%=         (**,//)

# conditional   : 
# Ternary Op :  (condition)? code1 : code2;
