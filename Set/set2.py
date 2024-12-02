# mySet = {True,False,11,1001}

# print(mySet)
# # mySet.pop()
# mySet.remove(True)
# print(mySet)
# dict{}
# tuple ()
# list []
# set {}

# mySet1 = set([11,12,13,14,15])
# mySet2 = set([11,1,13,14,5])

# print(mySet1)
# print(mySet2)

# mySet1.difference
# return new Set   : new variable stored
#  not effect in orignal  Sets
# mySet2.difference(mySet1)
# print(mySet2.difference(mySet1)) # {1,5}
# print(mySet1.difference(mySet2)) # {12,15}



# mySet1.difference_update
# return None
# Modifed Org Set 
# mySet1.difference_update(mySet2)
# print(mySet1)
# print(mySet2)

#################################################
# mySet1 = set([11,12,13,14,15])
# mySet2 = set([11,1,13,14,5])

# print(mySet1)
# print(mySet2)
# mySet1.intersection
# return new Set   : new variable stored
#  not effect in orignal  Sets

# Same
# print(mySet1.intersection(mySet2))
# print(mySet2.intersection(mySet1))



# mySet1.intersection_update
# mySet1 = set([11,12,13,14,15])
# mySet2 = set([11,1,13,14,5])

# mySet2.intersection_update(mySet1)
# print(mySet1)
# print(mySet2)

#################################################
# mySet1 = set([11,12,13,14,15])
# mySet2 = set([11,1,13,14,5])

# # print(mySet1)
# # print(mySet2)
# mySet1.symmetric_difference 
# print(mySet1.symmetric_difference(mySet2))

# mySet1.symmetric_difference_update
# mySet1.symmetric_difference_update(mySet2)
# mySet2.symmetric_difference_update(mySet1)
# mySet2.symmetric_difference_update(mySet2)


# print(mySet1)
# print(mySet2)
################################
# mySet1 = set([1,12,13,14,15])
# mySet2 = set(["True"])

# print(mySet1)
# print(mySet2)
# # mySet1.isdisjoint
# print(mySet1.isdisjoint(mySet2))




mySet1 = set([1,12,13,14,15])

# mySet1.issubset

# print(mySet1.issubset([1,12,13,14,15,16]))


# set1  > set2    >>> issubset
# mySet1.discard
# mySet1.remove(10)
# mySet1.discard(10)
# print(mySet1)
# mySet1.remove()  # if exist then remove else error