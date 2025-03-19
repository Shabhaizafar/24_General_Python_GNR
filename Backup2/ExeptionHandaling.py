# a=12
# print(a)


try: 
    print(12/0)
except NameError:
    print("Variable 'a' is not defined")
except ZeroDivisionError : 
    print("ZeroDivisionError")
except :
    print("dfgh")

else: 
    print("Your Program Execute Successfully")
finally : 
    print("Finally")