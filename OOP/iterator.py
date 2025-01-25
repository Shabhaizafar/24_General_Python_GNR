# iterator and iterable : 
#  String ,List ,Set,Tuble   >> iterable  

# Object ::
# myList = [11,12,13,14,59]
# myStr = "Zafar"

# for i in myStr: 
#     print(i)

# myiterator = iter(myStr)

# print(myiterator.__next__())
# print(myiterator.__next__())
# print(myiterator.__next__())
# print(myiterator.__next__())
# print(myiterator.__next__())
# print(myiterator.__next__()) # 6th  None


# Class : 

class Math : 
    # def __init__(self):
    #     pass
    def __iter__(self):
        self.number1 = 10
        return self
    def __next__(self):
        self.number1+=5
        if self.number1 <= 100:
            return self.number1
        # raise StopIteration
    
obj = Math()

myiterator = iter(obj)

# print(myiterator.__next__())
# print(myiterator.__next__())
# print(myiterator.__next__())


while(1):
    print(myiterator.__next__())
