# 28. Write a Python program to sort a given list of lists by length and value using lambda.
# Original list:
# [[2], [0], [1, 3], [0, 7], [9, 11], [13, 15, 17]]
# Sort the list of lists by length and value:
# [[0], [2], [0, 7], [1, 3], [9, 11], [13, 15, 17]]

# myList = [[2], [0], [1, 3], [0, 7], [13, 15, 17],[1,2]] 
#                                         # length , Value 
                                        
# myList = sorted(myList,key= lambda x : (len(x),x) )


# print(myList)


#####################################

# 29. Write a Python program to find the maximum value in a given heterogeneous list using lambda.
# Original list:
# myList = ['Python', 3, 2, 4, 5, 'version']
# # Maximum values in the said list using lambda:
# # 5

# ans = max(list(filter(lambda x: type(x)== type(1),myList)))
# print(ans)
####################################
# 33. Write a Python program to check whether a given string contains a capital letter, a lower case letter, a number and a minimum length using lambda.
# Input the string: W3resource
# ['Valid string.']


# myStr = "3resource"

# ans = sorted(myStr)

# output = list(filter(lambda x: x.isdigit(),ans)),list(filter(lambda x: x.islower(),ans)),list(filter(lambda x: x.isupper(),ans))

# print(output)
# if(len(output[0])!=0  and len(output[1])!=0 and len(output[2])!=0 and len(output)==3):
#     print(["Valid String"])
# else: 
#     print(["No Valid String"])
# -------------------------------------------------------------
# 41. Write a Python program to reverse strings in a given list of string values using lambda.
# Original lists:
# ['Red', 'Green', 'Blue', 'White', 'Black']
# Reverse strings of the said given list:
# ['deR', 'neerG', 'eulB', 'etihW', 'kcalB']


# myList = ['Red', 'Green', 'Blue', 'White', 'Black']
# ans  =  list(map(lambda x : ''.join(list(reversed(x))),myList))
# print(ans)
#--------------------------------------

# 42. Write a Python program to calculate the product of a given list of numbers using lambda.
# list1: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Product of the said list numbers:
# 3628800
# list2: [2.2, 4.12, 6.6, 8.1, 8.3]
# Product of the said list numbers:
# 4021.8599520000007

# myList = [2.2, 4.12, 6.6, 8.1, -8.3]
# print(myList)
# ans = [1]

# list(map(lambda x : ans.append(ans[len(ans)-1]*x),myList))

# print(ans[-1])
# sorted
# reversed
# map
# filter 
# min 
# max 

#--------------------------------------

# 43. Write a Python program to multiply all the numbers in a given list using lambda.
# Original list:
# [4, 3, 2, 2, -1, 18]
# Mmultiply all the numbers of the said list: -864
# Original list:
# [2, 4, 8, 8, 3, 2, 9]
# Mmultiply all the numbers of the said list: 27648
#--------------------------------------

# 44. Write a Python program to calculate the average value of the numbers in a given tuple of tuples using lambda.
# Original Tuple:
# ((10, 10, 10), (30, 45, 56), (81, 80, 39), (1, 2, 3))
# Average value of the numbers of the said tuple of tuples:
# (30.5, 34.25, 27.0)
# Original Tuple:
# ((1, 1, -5), (30, -15, 56), (81, -60, -39), (-10, 2, 3))
# Average value of the numbers of the said tuple of tuples:
# (25.5, -18.0, 3.75)

# myTuple = ((10, 10, 10), (30, 45, 56), (81, 80, 39), (1, 2, 3))
# print(myTuple)

# myList  = list(myTuple)
# mylist2 = [0,0,0]


# for i in myList:
#     for j in range(0,len(myList[0])):
#         mylist2[j] = mylist2[j]+i[j]

# ans = tuple(map(lambda x : x/len(myTuple),mylist2))
# print(ans)
#--------------------------------------

# 45. Write a Python program to convert string elements to integers inside a given tuple using lambda.
# Original tuple values:
# (('233', 'ABCD', '33'), ('1416', 'EFGH', '55'), ('2345', 'WERT', '34'))
# New tuple values:
# ((233, 33), (1416, 55), (2345, 34))


print(tuple(map(lambda x : tuple(map(lambda z : int(z),filter(lambda y : y.isdigit(),x))),(('233', 'ABCD', '33'), ('1416', 'EFGH', '55'), ('2345', 'WERT', '34')))))




