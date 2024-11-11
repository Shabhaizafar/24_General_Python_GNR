# myStr = "Royal Technosoft p ltd"
    #    012
# print(myStr)


# print(myStr.index('y')) # 2 
# print(myStr.index('o')) # 1 
# print(myStr.index('o',4)) # 11 
# print(myStr.index('o',4,10)) #  ValueError: substring not found

# print(myStr.index('Z'))



# mystr = "Ⅻ"     # A string with Roman numerals
# mystr = "٢٣٤٥"
# mystr = "²"
# mystr = "2"
# mystr = "we²"

# # myStr.isalnum  : True/False
# #  check : given string is alpha or num or alpha+num
# print(mystr.isalnum())  #

# myStr.isalpha
#  check : given string is alpha
# print(mystr.isalpha())

# myStr.isdecimal
# print(mystr.isdecimal()) 
# # myStr.isdigit
# print(mystr.isdigit())   # ²,power,sub
# # myStr.isnumeric
# print(mystr.isnumeric())   # roman

# mystr = "asdf😀"
# myStr.isupper  : True /false
# print(mystr.isupper())

# myStr.islower
# print(mystr.islower())

# myStr.istitle
# print(mystr.istitle())

# myStr.isspace 
# print(mystr.isspace())

# myStr.isascii
# print(mystr.isascii())

# myStr.isidentifier
# print(mystr.isidentifier())


# number/decimal  : positive number :  1,2,3,4,5


# ///////
# myStr1 = "12345"  # A string with regular digits
# myStr2 = "٢٣٤٥"  # A string with Arabic digits

# print(myStr1.isdecimal())  # True (because 12345 contains only decimal digits)
# print(myStr1.isdigit())    # True (because 12345 is composed of digits)
# print(myStr1.isnumeric())  # True (because 12345 is numeric)

# print(myStr2.isdecimal())  # False (because Arabic digits are not decimal)
# print(myStr2.isdigit())    # True (because Arabic digits are recognized as digits)
# print(myStr2.isnumeric())  # True (because Arabic digits are numeric)

# print(myStr3.isdecimal())  # False (Roman numerals are not decimal)
# print(myStr3.isdigit())    # False (Roman numerals are not considered digits)
# print(myStr3.isnumeric())  # True (Roman numerals are considered numeric)



# royal techno   : lower
# ROYAL TECHNO   : upper 
# Royal Techno   : title


