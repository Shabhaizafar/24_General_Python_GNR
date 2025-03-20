# myFile = open(File Path,Mode)  
# File Path : txt(work) or binary
# Mode :  r,w,a,a+,r+,w+

myFile = open('D://Royal/24_General_Python_GNR/Backup2/myFile.txt','r')

# Full Data
print(myFile.read())

# Single Single Line
# print(myFile.readline(),myFile.readline(),sep='')
# print(myFile.readline(1))
# print(myFile.readline(10))
# print(myFile.readlines(1))


# myFile.write("Hello")
# myFile.write("Zafar")

# myFile.write("Royal")
# myFile.write("\n\nRoyal")

# m = myFile.readline()
# for i in m:
#     print(i)


myFile.close()