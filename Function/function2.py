# Syntax  :
# lambda argument : expression

# write a Program to Print Square of Given Number.
# lambda num : pow(num,2)
# square =  lambda num : num**2

# print(square(2))


# write a Program to Print pow of Given Number.

# ans = lambda base,power : pow(base,power)
# print(ans(2,3))


#-----------------------------------------------------
# 1. Write a Python program to create a lambda function that adds 15 to a given number passed in as an argument, also create a lambda function that multiplies argument x with argument y and prints the result.
# Sample Output:
# 25
# 48
# adds15 = lambda num1 : num1+15
# print(adds15(10))
# multiplies = lambda x,y : x*y 
# print(multiplies(10,2))


# 2. Write a Python program to create a function that takes one argument, and that argument will be multiplied with an unknown given number.
# Sample Output:
# Double the number of 15 = 30
# Triple the number of 15 = 45
# Quadruple the number of 15 = 60
# Quintuple the number 15 = 75

# def myFu(i):
#     ans = lambda num : num*i 
#     print(ans(int(input("Enter the Value of N : "))))

# myFu(2)
# myFu(5)



# 3. Write a Python program to sort a list of tuples using Lambda.
# Original list of tuples:
# [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
# Sorting the List of Tuples:
# [('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]


# myList  = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
    #           0         1
#                   0               1                  2                    3

# print(sorted(myList,key= lambda a:a[1]))

# print(myList[1][0])
    

# 4. Write a Python program to sort a list of dictionaries using Lambda.
# Original list of dictionaries :
# [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
# Sorting the List of dictionaries :
# [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}]

#----------------------------------------------------------------

# 5. Write a Python program to filter a list of integers using Lambda.
# Original list of integers:
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Even numbers from the said list:
# [2, 4, 6, 8, 10]
# Odd numbers from the said list:
# [1, 3, 5, 7, 9]

# myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
# print(myList)

# ans1 = filter(lambda x : x%2==0,myList)
# ans2 = filter(lambda x : x%2!=0,myList)
# # ans = filter(lambda x : x%3==0 and x%2==0,myList)

# print(list(ans1))
# print(list(ans2))
# ------------------------------------------------------------ # 

# 6. Write a Python program to square and cube every number in a given list of integers using Lambda.
# Original list of integers:
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Square every number of the said list:
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# Cube every number of the said list:
# [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]


# myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
# print(myList)

# ans1 = map(lambda x : pow(x,2),myList)
# ans2 = map(lambda x : x**3,myList)

# print(list(ans1))
# print(list(ans2))
# ------------------------------------------------------------ #
# 7. Write a Python program to find if a given string starts with a given character using Lambda.
# Sample Output:
# True
# False

# mystr = "Royal Technosoft pvt ltd"
# print(mystr.startswith('r'))
# ans = lambda x,ch : x.startswith(ch)
# print(ans(mystr,'r'))



# 9. Write a Python program to check whether a given string is a number or not using Lambda.
# Sample Output:
# True
# True
# False
# True
# False
# True

# Print checking numbers:
# True
# True

# 10. Write a Python program to create Fibonacci series up to n using Lambda.
# Fibonacci series upto 2:
# [0, 1]
# Fibonacci series upto 5:
# [0, 1, 1, 2, 3]
# Fibonacci series upto 6:
# [0, 1, 1, 2, 3, 5]
# Fibonacci series upto 9:
# [0, 1, 1, 2, 3, 5, 8, 13, 21]