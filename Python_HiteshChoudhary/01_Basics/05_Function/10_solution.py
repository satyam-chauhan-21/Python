#-------------------------------------------------------------------------------#
#                           10. Recursive Function
#-------------------------------------------------------------------------------#
# Problem: Create a recursive function to calculate the factorial of a number.

import math
import random

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
    
number = math.floor(random.random() * 100)
print(f"factorial of {number} = {factorial(number)}")