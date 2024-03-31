#-------------------------------------------------------------------------------#
#                             6. Lambda Function
#-------------------------------------------------------------------------------#
# Problem: Create a lambda function to compute the cube of a number.

'''
- lambda function is one line function.
    to use it we have to write "lambda" keyword.
- used for small task.
- we can hold it in a variable.
Syntax:
lambda argument : work to do 
'''
import math
import random
cube = lambda x:x ** 3

number = math.floor(random.random() * 10)
print(f"{number} ** 3 = {cube(number)}")
