# 16. Write a Python program to find the second lowest total marks of any student(s) from the given names and marks of each student using lists and lambda. Input the number of students, the names and grades of each student.
# Input number of students: 5
# Name: S ROY
# Grade: 1
# Name: B BOSE
# Grade: 3
# Name: N KAR
# Grade: 2
# Name: C DUTTA
# Grade: 1
# Name: G GHOSH
# Grade: 1
# Names and Grades of all students:
# [['S ROY', 1.0], ['B BOSE', 3.0], ['N KAR', 2.0], ['C DUTTA', 1.0], ['G GHOSH', 1.0]]
# Second lowest grade: 2.0
# Names:
# N KAR

# myDetails = []
# n = int(input("ENter the Value of N : "))
# for i in range(0,n):
#     tempList = []
#     tempList.append(input("Enter Your Name : "))
#     tempList.append(float(input("Enter Your Grade : ")))

#     myDetails.append(tempList)

# print(myDetails)
# myDetails = sorted(myDetails,key=lambda x : x[1])
# print(myDetails)

# secondLowestValue = myDetails[0][1]
# Name = None
# for i in myDetails:
#     if(i[1]>secondLowestValue):
#         secondLowestValue = i[1]
#         Name = i[0]
#         break
# print("Second lowest grade :",secondLowestValue)
# print("Name :",Name)

#-------------------------------------- ------------------------------------------------------

# 17. Write a Python program to find numbers divisible by nineteen or thirteen from a list of numbers using Lambda.
# Orginal list:
# myList =[19, 65, 57, 39, 152, 639, 121, 44, 90, 190]
# Numbers of the above list divisible by nineteen or thirteen:
# [19, 65, 57, 39, 152, 190]

# ans = filter(lambda x : x%19==0 or x%13==0,myList)
# print(list(ans))


#--------------------------------------

# 18. Write a Python program to find palindromes in a given list of strings using Lambda.
# Orginal list of strings:
# myList = ['php', 'w3r', 'Python', 'abcd', 'Java', 'aaa']
# List of palindromes:
# ['php', 'aaa']

# ans = filter(lambda x : ''.join(list(reversed(x))) == x ,myList)
# print(list(ans))





#--------------------------------------

# 19. Write a Python program to find all anagrams of a string in a given list of strings using Lambda.
# Orginal list of strings:
# mylist = ['bcda', 'abce', 'cbda', 'cbea', 'adcb']
# # Anagrams of 'abcd' in the above string:
# # ['bcda', 'cbda', 'adcb']
# a = "abcd"
# ans = list(filter(lambda x : ''.join(list(sorted(a))) == ''.join(list(sorted(x))),mylist))
# print(ans)

#--------------------------------------

# 20. Write a Python program to find the numbers in a given string and store them in a list. Afterward, display the numbers that are longer than the length of the list in sorted form. Use the lambda function to solve the problem.
# Original string: sdf 23 safs8 5 sdfsd8 sdfs 56 21sfs 20 5
# Numbers in sorted form:
# 20 23 56
# myStr = "sdf 23 safs8 5 sdfsd8 sdfs 56 21sfs 20 5"

# filter(lambda x : x.isdigit() and , sorted(myStr.split(' ')))


# print()
#--------------------------------------

# 21. Write a Python program that multiplies each number in a list with a given number using lambda functions. Print the results.
# Original list: [2, 4, 6, 9, 11]
# Given number: 2
# Result:
# 4 8 12 18 22
#--------------------------------------

# 22. Write a Python program that sums the length of a list of names after removing those that start with lowercase letters. Use the lambda function.
# Result:
# 16
#--------------------------------------

# 23. Write a Python program to calculate the sum of the positive and negative numbers of a given list of numbers using the lambda function.
# Original list: [2, 4, -6, -9, 11, -12, 14, -5, 17]
# Sum of the positive numbers: -32
# Sum of the negative numbers: 48
#--------------------------------------

# 24. Write a Python program to find numbers within a given range where every number is divisible by every digit it contains.
# Sample Output:
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
#--------------------------------------

# 25. Write a Python program to create the next bigger number by rearranging the digits of a given number.
# Original number: 12
# Next bigger number: 21
# Original number: 10
# Next bigger number: False
# Original number: 201
# Next bigger number: 210
# Original number: 102
# Next bigger number: 120
# Original number: 445
# Next bigger number: 454
