
# 1. **List Comprehension with Conditions**:  
#    Write a Python one-liner using list comprehension to find all numbers in a list that are divisible by 3 and 5, and store their squares in a new list.  
# n1 = int(input("Enter the Value of N1 : "))
# n2 = int(input("Enter the Value of N2 : "))
# mainList = []
# comprehensionList = []
# if(n1<n2):
#     for i in range(n1,n2+1):
#         mainList.append(i)
# else:
#     temp = n1
#     n1 = n2
#     n2 = temp
    
#     for i in range(n1,n2+1):
#         print(i)
#         mainList.append(i)

# print("Values which is Divisable by 3 and 5 : ")
# for i in mainList : 
#     if i%3==0 and i%5==0 :
#         # comprehensionList.append(i*i)
#         print(i)
#         comprehensionList.append(pow(i,2))
# print(mainList)

# print(comprehensionList)





# 2. **Tuple Manipulation**:  
#    Given a tuple `t = (5, 10, 15, 20, 25)`, write a Python function that rotates the tuple elements to the left by 2 positions.  
# myTuple = (5, 10, 15, 20, 25)
# print("Main Tuple : ",myTuple)

# myList = list(myTuple)
# finalList = []
# n = int(input("Enter Position Number : "))
#                     # starting index   :   ............ending
# finalList.extend(myList[n:])
#                     # starting index  :    ending index+1
#                                             # -1
# finalList.extend(myList[0:n])
# myTuple = tuple(finalList)
# print("After Rotate : ",myTuple)


# 3. **String Pattern Matching**:  
#    Write a Python function that extracts all unique words (case-insensitive) from a string and returns them as a sorted list. Ignore punctuation.
mystr = """
Python is a versatile programming language that excels in handling various data structures like lists, tuples, strings, sets, and dictionaries. Lists allow dynamic storage of elements, supporting operations like slicing, filtering, and sorting. Tuples are immutable sequences used when data integrity is crucial. Strings offer powerful manipulation methods for pattern matching, splitting, and formatting. Sets are collections of unique elements, ideal for operations like union, intersection, and difference. Dictionaries, or key-value pairs, enable efficient data retrieval and organization. Python's comprehensions and built-in functions simplify processing these structures, making it a powerful tool for tasks ranging from basic operations to advanced data processing.
"""
myList = [] 
temp = ""
for i in mystr : 
    if(ord(i)>=65 and ord(i)<=90):
        temp+=i;
    elif(ord(i)>=97 and ord(i)<=122):
        temp+=i;
    elif ord(i) == 39 : 
        temp+=i;
    else:
        if temp=="":
            continue
        myList.append(temp.lower())
        temp=""

mySet = set(myList)
myList = list(mySet)
myList.sort()
print(myList)
# 4. **Set Operations with Comprehensions**:  
#    Write a Python function to find the symmetric difference of two sets and return only the elements that are prime numbers.  

# 5. **Nested Dictionary Processing**:  
#    Write a Python function that takes a nested dictionary and returns a flat dictionary where keys are the original keys joined by `"."`.  
#    Example:  
#    ```python
#    Input: {"a": {"b": {"c": 1}}, "d": 2}  
#    Output: {"a.b.c": 1, "d": 2}
#    ```  

# 6. **List of Tuples Sorting**:  
#    Given a list of tuples `[(1, 'apple'), (3, 'banana'), (2, 'cherry')]`, write a Python function to sort the list by the second element of each tuple in descending order.  

# 7. **String Frequency Analysis**:  
#    Write a Python function to count the frequency of each character in a string (ignoring case) and return the result as a dictionary.  

# 8. **Set-Based List Deduplication**:  
#    Write a Python function that takes a list of strings, removes duplicates (case-insensitively), and returns the result sorted in ascending order.  

# 9. **Dictionary Filtering**:  
#    Write a Python function to filter a dictionary, keeping only the key-value pairs where the value is of type `int` and greater than 10.  

# 10. **Combining Data Structures**:  
#     Write a Python function that takes a list of tuples representing key-value pairs, converts it into a dictionary, and then finds the set of all keys that have numeric values greater than 50.  



# //////////////////////////////
# List Comprehension with Filtering and Transformation:
# Write a Python one-liner using list comprehension to extract all numbers from a list that are prime and store their cubes in a new list.

#-------------------------------------------
# Tuple Pair Swapping:
# Given a tuple t = (1, 2, 3, 4, 5, 6), write a Python function to swap each adjacent pair of elements (e.g., (1, 2, 3, 4, 5, 6) → (2, 1, 4, 3, 6, 5)).

#-------------------------------------------

# String Word Frequency Analysis:
# Write a Python function that counts the frequency of each unique word (case-insensitive) in a string and returns a dictionary sorted by the word's frequency in descending order. Ignore punctuation.

#-------------------------------------------
