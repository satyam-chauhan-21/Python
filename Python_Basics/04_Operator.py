#---------------------------------------------------------------------#
#                            Operators
#---------------------------------------------------------------------#
# all operator are same as all language but there is a new operator call Floor Division '//'.

#---------------------------------------------------------------------#
#                          Arithmetic operator
#---------------------------------------------------------------------#

# num1 = 10
# num2 = 3

# print("addition is : ", num1 + num2)
# print("subtraction is : ", num1 - num2)
# print("multiplication is : ", num1 * num2)
# print("division is : ", num1 / num2)
# print("modulus is : ", num1 % num2)
# print("exponential is : ", num1 ** num2) # '**' : is used for exponential or x^y (finding power)
# print("floor division is : ", num1 // num2) # '//' : will return integer as output of dividion

#---------------------------------------------------------------------#
#                         Comparison operator
#---------------------------------------------------------------------#

# < > == <= >=

# num1 = 3
# num2 = 4
# print(num1>num2)
# print(num1<num2)
# print(num1>=num2)
# print(num1<=num2)

#---------------------------------------------------------------------#
#                           Logical operator
#---------------------------------------------------------------------#

# # and  or  not

# num1 = 10
# num2 = 3

# expression1 = num1 > num2
# expression2 = num1 < num2

# print(expression1 and expression2) # output : False
# print(expression1 or expression2) # output : True
# print(not False) # output : True
# print(not True) # output : False

#---------------------------------------------------------------------#
#                       Identity Operator
#---------------------------------------------------------------------#

# "is" : return true if both variable are same object
# "is not" : return true if both variable are not same object

# x = 3
# y = 4

# print("if x is y : ", x is y) # output : False
# print("if x is not y : ", x is not y) # output : True

#---------------------------------------------------------------------#
# I've copied this from W3school 

# x = ["apple", "banana"]
# y = ["apple", "banana"]
# z = x

# print(x is z) # returns True because z is the same object as x
# print(x is y) # returns False because x is not the same object as y, even if they have the same content
# print(x == y) # to demonstrate the difference betweeen "is" and "==": this comparison returns True because x is equal to y

# print(x is not z) # returns False because z is the same object as x
# print(x is not y) # returns True because x is not the same object as y, even if they have the same content
# print(x != y) # to demonstrate the difference betweeen "is not" and "!=": this comparison returns False because x is equal to y

#---------------------------------------------------------------------#
#                         Membership Operator
#---------------------------------------------------------------------#
# this operator is used in sequence data type like "list", "tuple", "set".

# in : return true if sequence with specified value is present in the object
# not in : return true if sequence with specified value is not present in the object

# fruits = ["banana", "orenge", "apple", "cherry"]

# print("if banana is present in fruits :", "banana" in fruits) # output : True
# print("if mango is present in fruits :", "mango" in fruits) # output : False
# print("if mango is not present in fruits :", "mango" not in fruits) # output : True
# print("if banana is not present in fruits :", "banana" not in fruits) # output : False

#---------------------------------------------------------------------#
#                         Bitwise Operator
#---------------------------------------------------------------------#
# https://www.geeksforgeeks.org/python-bitwise-operators/

'''
& (and) : retrun True if both bit are 1 (binary operator, needs two operands)
| (or) : retrun True if atleast one bit is 1 (binary operator, needs two operands)
^ (xor) : retrun True if both bit are not same (binary operator, needs two operands)
~ (not) : convert 1 in 0 , and 0 in 1 (unary operator, needs only one operand)
<< (left shift) : shift one bit to left (unary operator, needs only one operand)
<< (left shift) : shift one bit to right (unary operator, needs only one operand)
'''

# a = 5
# b = 3
# print("a & b :", a & b) # output : 1
# print("a & b :", a | b) # output : 7
# print("a & b :", a ^ b) # output : 6
# print("~a :", ~a)       # output : -6


a = 50
# left shift by 1 position
print("a << 1 :", a << 1) # output : 100
# left shift by 2 position
print("a << 2 :", a << 2) # output : 200

# right shift by 1 position
print("a >> 1 :", a >> 1) # output : 25
# right shift by 2 position
print("a >> 2 :", a >> 3) # output : 6

