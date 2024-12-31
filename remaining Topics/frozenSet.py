#  Frozenset : 

# A frozenset in Python is an immutable version of a set. While a regular set is mutable (you can add or remove elements), a frozenset cannot be modified after it is created. This makes frozenset hashable, so it can be used as a key in a dictionary or as an element of another set.

# Key Characteristics of frozenset:
# Immutable: Once created, its elements cannot be changed.
# Hashable: It can be used as a key in dictionaries or added to other sets.
# Unordered: Like a regular set, the elements in a frozenset are unordered.
# No duplicates: A frozenset automatically removes duplicate elements.


# Operations on frozenset:
# While you cannot modify a frozenset, you can perform operations that return new sets:

# Union (|)
# Intersection (&)
# Difference (-)
# Symmetric difference (^)


# myList = [11,12,13,13,12,11,14]
# print(myList)

# # How to Create a FrozenSet : 
# Set_of_Frozen = frozenset(myList)

# print(Set_of_Frozen)
# print(type(Set_of_Frozen))


# mySet = {11,12,13}
# print(mySet)
# mySet.add(14)
# print(mySet)


fs1 = frozenset([11,12,13])
fs2 = frozenset([11,14,15])

# print(fs1,fs2)
# # Union (|)
# print(fs1 | fs2)

# Intersection (&)
# print(fs1 & fs2)

# # Difference (-)
# print(fs1 - fs2)
# print(fs2 - fs1)


# # Symmetric difference (^)
# print(fs1 ^ fs2)

# ans = fs1.union(fs2)
# print(ans)

# print(fs1 and fs2)
# print(fs1 or fs2)


# and or 
# ------------------------------------------------------------


### **Question 1:**
# What will be the output of the following code?
# ```python
# fs = frozenset([1, 2, 3, 4, 5])
# print(3 in fs)
# print(fs.add(6))
# ```

# ---

# ### **Question 2:**
# Given the following code, which line will raise an error and why?
# ```python
# fs1 = frozenset([1, 2, 3])
# fs2 = frozenset([3, 4, 5])
# result = fs1 | fs2
# fs1.add(6)
# ```

# ---

# ### **Question 3:**
# How can you use a `frozenset` as a key in a dictionary? Provide an example.

# ---

# ### **Question 4:**
# Write a Python program that creates a `frozenset` from the list `[1, 2, 3, 3, 4, 4, 5]` and prints the union of this `frozenset` with another `frozenset` containing `[4, 5, 6, 7]`.

# ---

# ### **Question 5:**
# What is the difference between a `set` and a `frozenset` in Python? Provide a code example to illustrate one key difference.

# ---
