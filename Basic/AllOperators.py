# Arithmetic operators
'''
+	Addition	x + y	
-	Subtraction	x - y	
*	Multiplication	x * y	
/	Division	x / y	
%	Modulus	x % y	
**	Exponentiation	x ** y	
//	Floor division	x // y

'''

# Assignment operators
'''
=	x = 5	x = 5	
+=	x += 3	x = x + 3	
-=	x -= 3	x = x - 3	
*=	x *= 3	x = x * 3	
/=	x /= 3	x = x / 3	
%=	x %= 3	x = x % 3	
//=	x //= 3	x = x // 3	
**=	x **= 3	x = x ** 3	
&=	x &= 3	x = x & 3	
|=	x |= 3	x = x | 3	
^=	x ^= 3	x = x ^ 3	
>>=	x >>= 3	x = x >> 3	
<<=	x <<= 3	x = x << 3	
:=	print(x := 3)	x = 3
print(x)

'''
# Comparison operators
'''
==	Equal	x == y	
!=	Not equal	x != y	
>	Greater than	x > y	
<	Less than	x < y	
>=	Greater than or equal to	x >= y	
<=	Less than or equal to	x <= y
'''

# Logical operators
'''
and 	Returns True if both statements are true	x < 5 and  x < 10	
or	Returns True if one of the statements is true	x < 5 or x < 4	
not	Reverse the result, returns False if the result is true	not(x < 5 and x < 10)
'''

# Identity operators
'''
is 	Returns True if both variables are the same object	x is y	
is not	Returns True if both variables are not the same object	x is not y
'''
# n1 = 12
# n2 = 12

# print(n1)
# print(n2)
# print(n1 is n2)
# print(n1 is not n2)



# id(): 
# print(id(n1))
# print(id(n2))


# Membership operators
'''
in 	Returns True if a sequence with the specified value is present in the object	x in y	
not in	Returns True if a sequence with the specified value is not present in the object	x not in y
'''
# myList = [11,12,13,14,15]
# print(myList)

# print([12,13] in myList)  //False
# print(12,13 in myList)   

# Bitwise operators
'''
& 	AND	Sets each bit to 1 if both bits are 1	x & y	
|	OR	Sets each bit to 1 if one of two bits is 1	x | y	
^	XOR	Sets each bit to 1 if only one of two bits is 1	x ^ y	
~	NOT	Inverts all the bits	~x	
<<	Zero fill left shift	Shift left by pushing zeros in from the right and let the leftmost bits fall off	x << 2	
>>	Signed right shift	Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off	x >> 2
'''
# print(12 & 6)
# print(12 | 6)
# print(12 ^ 6)
# print(~(-12)) 
    # - (number + 1)

# Left Shift 
# print(12<<2) #
    # 110000  = 32+16 = 48
# print(15<<3)

# Right Shift
# print(12>>2)
    # 11 = 2+1  = 3 
# print(15>>3)



# n1 = 12
# n2 = 6

# n1&=n2
'''
n1&=n2 
n1 = n1&n2
n1 = 1100 & 0110
   = 0100
   =4
'''
# print(n1)