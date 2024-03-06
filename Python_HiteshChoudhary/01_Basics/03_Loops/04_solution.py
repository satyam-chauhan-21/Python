#-------------------------------------------------------------------------------#
#                             4. Reverse a String
#-------------------------------------------------------------------------------#
# Problem: Reverse a string using a loop.

input_str = input("Enter a String to reverse : ")
reversed_str = ""
# print(reversed_str)

'''below for loop give output last character of the string, because in first iteration loop will assign the first character of input_string, then in second iteration loop will assign the second character of the input_str and oweright the first character, and following this process loop will assign last character of the input_str and overwrite all the character which occurs earlier.'''
# for i in input_str:
#     reversed_str = i

# print(reversed_str)

'''for solving above problem we have to store all the letters of the input_string for that we are using below method. in this mwthod we take "reversed_str" in loop & assigning concatination of "reversed_str" and "iterator" so that this logic will hold all the previous assigned character(value) in it and adds new character(value) from next iteration. but this logic will store same string as input_string.'''
'''in below loop this happens so that we get same string we enter in input_str.
now supppose our input string is "python" 
    so in the fisrt iteration, 
        first "reversed_str"(which is empty now) will concatinate with "p"(the first character of our input string) and store in "reversed_str"
    
    reversed_str = p

    in second iteration,
        "p"(value stored in "reversed_str") will concatinate with "y"(iterator) and assigned in "reversed_str".
    
    reversed_str = py

    in third iteration,
        "py"(value stored in "reversed_str") will concatinate with "t"(iterator) and assigned in "reversed_str".
    
    reversed_str = pyt

    in fourth iteration,
        "pyt"(value stored in "reversed_str") will concatinate with "h"(iterator) and assigned in "reversed_str".
    
    reversed_str = pyth

    in fifth iteration,
        "htyp"(value stored in "reversed_str") will concatinate with "o"(iterator) and assigned in "reversed_str".
    
    reversed_str = pytho

    in sixth iteration,
        "ohtyp"(value stored in "reversed_str") will concatinate with "n"(iterator) and assigned in "reversed_str".
    
    reversed_str = python

    in seventh iteration we don't have any character so loop will ends here and we get same string as we input in input_str.
        
'''
# for i in input_str:
#     reversed_str = reversed_str + i

# print(reversed_str)



'''for solving above problem we just change the position of "iterator" and "reversed_str". 
now supppose our input string is "python" 
    so in the fisrt iteration, 
        first "p"(the first character of our input string) will concatinate with "reversed_str"(which is empty now) and store in "reversed_str"
    
    reversed_str = p

    in second iteration,
        "y"(iterator) will concatinate with "p"(value stored in "reversed_str") and assigned in "reversed_str".
    
    reversed_str = yp

    in third iteration,
        "t"(iterator) will concatinate with "yp"(value stored in "reversed_str") and assigned in "reversed_str".
    
    reversed_str = typ

    in fourth iteration,
        "h"(iterator) will concatinate with "typ"(value stored in "reversed_str") and assigned in "reversed_str".
    
    reversed_str = htyp

    in fifth iteration,
        "o"(iterator) will concatinate with "htyp"(value stored in "reversed_str") and assigned in "reversed_str".
    
    reversed_str = ohtyp

    in sixth iteration,
        "n"(iterator) will concatinate with "ohtyp"(value stored in "reversed_str") and assigned in "reversed_str".
    
    reversed_str = nohtyp

    in seventh iteration we don't have any character so loop will ends here and we get our reversed_string.
        
'''

for i in input_str:
    reversed_str = i + reversed_str

print(reversed_str)