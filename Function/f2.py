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


