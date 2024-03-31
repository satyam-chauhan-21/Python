#-------------------------------------------------------------------------------#
#                         1. Basic Function Syntax
#-------------------------------------------------------------------------------#
# Problem: Write a function to calculate and return the square of a number.

def printSqure(num):
    return num ** 2

number = int(input("enter number : "))
print(f"Squre of {number} is ",printSqure(number))