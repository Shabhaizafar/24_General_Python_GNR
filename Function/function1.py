#=> what is a Function : 
    #- Block of Code.
    #- Code re-useblity.
    #- maintablity.

# Syntax : 
# in C : 

# step1 : declaration.
# variable :  int a;
# void sayhello();

# step2 : initialization.
# variable : a = 12;
# void sayhello(){
#     code;
# }

# step3 : function calling/invoked
# variable : printf(a);
# sayhello();
#########################################
# in Python  : 
# step1 :  function initialization.
# def functionname():
#     code 

# step2 : function calling/invoked.
# functionname()


# def sayHello():
#     print("Hello")


# sayHello()

########################
# type : 
# 1) without argument and without rtn 

# def sayHello():
#     print("Hello")

# sayHello()

# 2) with argument and without rtn 
# def addition(n1,n2):                # n1,n2 Paramanter 
#     print("Addition is : ",n1+n2)

# addition(12,13)                     # 12,13 Argument 


# 3) without argument and with rtn 
# def addition():         
#     n1 = 12
#     n2 = 13 
#     return n1+n2

# without Storing 
# print(addition())

#with Storing 
# ans  = addition()
# print(ans)


# 4) with argument and with rtn 
# def addition(n1,n2):
#     return n1+n2


# without Storing 
# print(addition(12,13))

# with Storing 
# ans  = addition(14,15)
# print(ans)


#################################################

# recursion : 
# => Function called it's Self.

# def sayHello():
#     print("Hello Everyone!!")
#     sayHello()

# sayHello()

# DSA : C,CPP,JAVA,PYTHON,..etc 

# while(1):
#     print("Hello Everyone!!")


###############################################
# fibonacci Series : 
# 0,1,1,2,3,5,8,13,21... 
# a
#   b
# a+b=c 
# n = int(input("Enter the Number of Values : "))
# a = 0
# b = 1
# def fibonacci(a,b,temp,n):
#     i = temp
#     print(a,end=',')
#     c = a+b 
#     a = b 
#     b = c 
#     if(i==n):
#         return
#     temp+=1
#     return fibonacci(a,b,temp,n)

# fibonacci(a,b,1,n)






# switch : break 
# if : X 
# loop : break 
# function : return 


# Write a Python program to get the sum of a non-negative integer using recursion.
# Test Data:
# sumDigits(345) -> 12
# sumDigits(45) -> 9
