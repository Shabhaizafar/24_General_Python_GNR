# Read a File  : 
# print(open("D://Royal/24_General_Python_GNR/File Handling/file2.txt",'r'))

# Read File : 
myfile = open("D://Royal/24_General_Python_GNR/File Handling/file1.txt",'r')

# Create a File :  (w: write mode : file Create if Doesn't Exist)
#                 #  (if File Exists then it's Overwrite the File)
# myfile = open("D://Royal/24_General_Python_GNR/File Handling/file2.txt",'w')

# # myfile.write("Hello Everyone!!!")
# # myfile.write("My Name is Zafar!!")


# myfile.close() # Close the File

                #  (if File Exists then it's Overwrite the File)
# myfile = open("D://Royal/24_General_Python_GNR/File Handling/file3.txt",'a')

# myfile.write("Hello Everyone!!!")
# myfile.write("\nMy Name is Zafar!!")


# myfile.close() # Close the File



# print(open('D://Royal/24_General_Python_GNR/File Handling/file4.txt','w'))
# print(open('D://Royal/24_General_Python_GNR/File Handling/file5.txt','a'))
# print(open('D://Royal/24_General_Python_GNR/File Handling/file4.txt','x'))


# myfile = open("D://Royal/24_General_Python_GNR/File Handling/file3.txt",'a')

# myfile.write("Hello Everyone!!!")
# myfile.write("\nMy Name is Zafar!!")


# myfile.close() # Close the File

import os

# os.remove('D://Royal/24_General_Python_GNR/File Handling/file4.txt')

os.rmdir('D://Royal/24_General_Python_GNR/File Handling')