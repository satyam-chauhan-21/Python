#---------------------------------------------------------------------#
#                             User Input
#---------------------------------------------------------------------#
'''
for user input in Python we have to use input() function.
ans pass some tring as parameter for example, "enter values :" , "enter number : " etc.
'''

#now let's take input and store it in a variable then print that value

name = input("enter your name : ")
print("entered name is ",name)


#---------------------------------------------------------------------#
#                             Problem
#---------------------------------------------------------------------#
#now let's take two number and print their sum

num1 = input("enter the first number : ") # input : 2
print("type of num1 is ",type(num1))
num2 = input("enter the second number : ") # input : 3
print("type of num2 is ",type(num2))

sum = num1 + num2

print ( "sum of ", num1, " and ", num2, " is ", sum)
#output : sum of  2  and  3  is  23

"""
we entered two numbers first : 2 , second : 3 and we expected output 5.
but the output we get is 23.
"""

#---------------------------------------------------------------------#
#                         Solution : TypeCast
#---------------------------------------------------------------------#
"""
as above problem we get to know that input() function is take everything as string.
so if we want to take number or integers so first we normally get the input then typecast this input in integer.
"""

num1 = int(input("enter first number : ")) # input : 2
print("type of num1 is ",type(num1))
num2 = int(input("enter second number : ")) # input : 3
print("type of num2 is ",type(num2))

sum = num1 + num2 

print("sum of ", num1, " and ", num2, " is ", sum) # output : sum of  2  and  3  is  5