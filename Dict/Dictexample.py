myDict = {
    "Id" : 100,
    "PhoneNo": 12,
    "reference" : 1000
}
key1 = input("ENter Key : ")
value1 = int(input("Enter Value"))
# value1 in list(myDict.values())
if (key1 in list(myDict.keys()) and value1 == myDict[key1]):
    print("Exist")
else:
    print("Doesn't Exist")


# myDict2 = {
#     "cmp" : "sdfg"
# }
# for i in myDict2: 
#     myDict.setdefault(i,myDict2[i])

# print(myDict)
# descDict = {

# }
# newLi = list(myDict.values())
# newLi.sort(reverse=True)
# for i in newLi:
#     for key in myDict : 
#         if(myDict[key]==i):
#             descDict.setdefault(key,i)
# print(descDict)

            
            