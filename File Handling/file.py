# File Read : 
# Read Mode : 
# Open : Open File/Create File (depends on Mode)
file1 = open("D://Royal/24_General_Python_GNR/File Handling/file1.txt",'r')

# read() : Fetch Data and you can use or stored data.
# print(file1.read())   # use
# str1 = file1.read()   # stored
# print(str1)

# print(file1.readline())  #Hello Everyone,    empty string only
# print(file1.readline())  #Welcome to My Home.!!  empty string only
# print(file1.readline())  #Do you want Tea or Coffee ?  empty string only
# print(file1.readline())  # empty string only empty string only

# print(file1.readline(1)) # H      # 1 : it's decide Howmany Char Print
# print(file1.readline(5)) # ello   # 5 : it's decide Howmany Char Print


# print(file1.readline(20))

# print(len(file1.readline()))


# print(file1.readlines())
# print(file1.readlines(1))    # 1(is indicate index) : it's Decide Howmany Lines 
# print(file1.readlines(3))    # 1 : it's Decide Howmany Lines 


# print(file1.readlines(17))



for i in range(0,4):
    print(file1.readline())

# close : File Terminate 
file1.close()


#################################3
# 1. Write a Python program to read an entire text file.


# 2. Write a Python program to read first n lines of a file.


# 4. Write a Python program to read last n lines of a file.


# 5. Write a Python program to read a file line by line and store it into a list.


# 6. Write a Python program to read a file line by line store it into a variable.


# 7. Write a Python program to read a file line by line store it into an array.


# 8. Write a python program to find the longest words.
