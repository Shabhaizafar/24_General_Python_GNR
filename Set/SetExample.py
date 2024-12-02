# # Set
# A = {2, 4, 5, 6}
# # List
# # Compared Value's only
# lis = [1, 2, 3, 4, 5]
# # Dictionary dict, Set is formed on Keys
# # dict = {1: 'Apple', 2: 'Orange'}

# # Dictionary dict2
# dict2 = {'Apple': 1, 'Orange': 2}
# # print("Set A and List lis disjoint?", A.isdisjoint(lis))
# # print("Set A and dict are disjoint?", A.isdisjoint(dict))
# print("Set A and dict2 are disjoint?", A.isdisjoint(dict2))
########################################################################
mySet = {11,12,44,5,13,14,15}
# 14. Write a Python program to find the maximum and minimum values in a set.
print(min(mySet))
print(max(mySet))

# minNum = list(mySet)[0]
# maxNum = list(mySet)[0]
# for i in mySet : 
#     if(minNum>i):
#         minNum = i 
#     if(maxNum<i):
#         maxNum = i
# print(minNum)
# print(maxNum)
############################################



# 15. Write a Python program to find the length of a set.
# setLength = len(list(mySet))
# print(setLength)


# 16. Write a Python program to check if a given value is present in a set or not.

# print(20 in mySet)


# 17. Write a Python program to check if two given sets have no elements in common.

mySet2 = {100,12}
# mySet.intersection_update(mySet2)
# print(len(mySet)==0)


# 19. Write a Python program to find elements in a given set that are not in another set.
print(mySet.difference(mySet2))


# 20. Write a Python program to remove the intersection of a second set with a first set.