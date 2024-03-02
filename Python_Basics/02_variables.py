"""
    variables are container to store values.
    in Python there is no need to specify variables Datatype.
    we can declare variable using below syntex:
        variable_name = variable_value
"""

# var1 = 10       # here "var1" is variable and 10 is its value which is integer type 
# var2 = "manav"  # here "var2" is variable and "manav" is its value which is string type 
# var3 = 23.45    # here "var3" is variable and "23.45" is its value which is floting point type

# by using print() function we can print whatever we want to display in console or terminal

# print(var1) # display value of variable "var1"
# print(var2) # display value of variable "var2"
# print(var3) # display value of variable "var3"

'''
we can display normal text in terminal using print() function, for that we have to use double quotes
    and write whatever we want to display 
'''

# print("hello, my name is name and currently i am pursuing my degree form abc college, i field of interest is software engineering and for that i am learnig C++, Java and Python i have some knowleged of Data Structure and Algorithm and by using it i have solved some basic level questions on different coding platforms.")

# integer
age = 19

# string 
name = "mihir"

# float
cpi = 99.99

# boolean 
isStudent = True

'''
#   printing above variables with some text, for that we have to write text in double quote then add a comma ',' then we can write 
variable name and if we want to add more text so we have to add anothe comma ',' then we can add text inside double quotes,
so by following this above method we can write text and variables togehter.
'''
print("My name is ", name, " age is ",age, " is student ", isStudent , " and CPI is ",cpi) 

#----------------------------------------------------------------------#
#       checking type of variable using type() function
#----------------------------------------------------------------------#

print(type(name))       # output : <class 'str'>
print(type(age))        # output : <class 'int'>
print(type(isStudent))  # output : <class 'bool'>
print(type(cpi))        # output : <class 'float'>

#----------------------------------------------------------------------#
#                              separator
#----------------------------------------------------------------------#
'''
separetor can be any symbol or space which separate variables in print() function 
for using separator we must add : ' sep="value" ' where bydefault value is space and we can add any symbol in it.
'''
x = 10 
y = 20 
z = 30 
print(x,y,z,sep="*")        # output : 10*20*30
print(x,y,z,sep="-")        # output : 10-20-30
print(x,y,z,sep=" -> ")     # output : 10 -> 20 -> 30