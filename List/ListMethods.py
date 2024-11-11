# List Methods : .
# myList  = [101,100,111,200,300,1001,100,"Royal","Soft",True]
# print(myList)

# len()
# print(len(myList))

# 1) appand :  Add a Single Data at a Time (after Last Index)
# no return 

# ans = myList.append(1000) # None
# print(myList)
# print(ans)

# myList.append(["Z","A"]) # add list at new Index 
# print(myList)

# 2) remove : remove specific single Data at a Time
# no return 

# ans = myList.remove(100)
# print(myList)
# print(ans)

# 3) clear :  clear All Data  
# no return 

# myList.clear()
# print(myList)

# 4) copy :   return Shallow Copy
# newCopyList = myList.copy()   # shallow copy 
# print(newCopyList)
# print(id(myList))
# print(id(newCopyList))

# 5) count :  if value exist then return counter value else return 0.
# ans = myList.count(10011)
# print(ans)



# 5) extend : add new Multiple Data (which is Itrable) at Last Index 
# No return

# myList.extend(["Z","A"])
# myList.extend((12,13))
# myList.extend("Zafar")
# myList.extend(111)    # TypeError: 'int' object is not iterable
# print(myList)

# ans = myList.extend([11,12])
# print(ans)


# 6) index : 
# return 

# ans = myList.index(100)   # checking from starting index and return first occurnce
# ans = myList.index(100,3)   # checking from 3 index and return first occurnce index Value


#                 value,starting point ,ending point  
# ans = myList.index(100,3,5)   # checking from 3 index to 4-1 index and if exist then return first occurnce index Value  else showing Error
# print(ans)

# 7)  insert : add new specific Value at specific Index Number
# myList.insert(3,"Z")

# if Index doesn't exist then add at a Last index
# myList.insert(33,"Z")
# myList.insert(3,"Z","A") #TypeError: insert expected 2 arguments, got 3

# print(myList)


# pop,reverse,sort : 



'''
1) 

fruits = [
    "apple", "banana", "cherry", "date", "elderberry", 
    "fig", "grape", "honeydew", "kiwi", "lemon",
    "mango", "nectarine", "orange", "papaya", "quince",
    "raspberry", "strawberry", "tangerine", "ugli fruit", "vanilla",
    "watermelon", "zucchini"
]

2) 

mixed_list = [
    42, "hello", 3.14, True, None,
    "Python", 7, False, 99.99, "OpenAI",
    [1, 2, 3], {"key": "value"}, (4, 5), 
    {1, 2, 3}, complex(2, 3)
]
'''



'''
14/10/2024
'''
# myList  = [101,100,111,200,300,1001,100,"Royal","Soft",True]
# index:    0   1   2   3   4    5   6    7       8      9
# index2:  -10 -9  -8  -7  -6   -5  -4    -3     -2     -1              
# print(myList)

# print(myList[0])
# print(myList[-10])


# pop,reverse,sort : 

# recap :  remove : 
# myList.remove(101)
# print(myList)

# pop() : remove  specific index(negative index/positive) Value 
# if length greathan 0 then return deleted Value else showing error
# myList.pop(-1)   # default
# myList.pop(-3)  
# myList.pop(5)  
# ans = myList.pop(5)   

# print(myList)
# print(ans)



# reverse() : 
# myList.reverse()
# print(myList[0])

# myList = [14,11,56,12,30,10,5,3,19]

# myList = [10,1,111,10001,11,1111,1001]
# print(myList)
# myList.sort()   # acending
# myList.sort(reverse=True)   # decending

# print(myList)