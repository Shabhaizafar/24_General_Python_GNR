# Match : 
choice= 1

# match choice:
#     case 1 : print("1")
#     case 2 : print("2")
#     case 3 : print("3")


# switch : 
    # case : matched case condition ignored

def addition(a,b):
    return  f"Addition is : {a+b}"

def subraction(a,b):
    return  f"subtraction is : {a-b}"

def multiplication(a,b):
    return  f"multiplication is : {a*b}"

def opration(n1,n2,choice): 
    match choice:
        case 1 : return addition(n1,n2)
        case 2 : return subraction(n1,n2)
        case 3 : return multiplication(n1,n2)


final_opt = opration(12,13,2)
print(final_opt)