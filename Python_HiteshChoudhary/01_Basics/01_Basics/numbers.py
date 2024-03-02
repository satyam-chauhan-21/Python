'''
don't write math operation like this
    2 + 5 * 4 / 6 
instead of add parantheses which make code more readeble and industry standard.
    (2 + 5) * (4 / 6) 

    
don't make operation like 
    40 + 2.23
first make conversion it can be explisit  but first make both operands same data type then perform any operations
    float(40) + 2.23
'''

#-------------------------------------------------------------------------------#
#                   difference between str() & repr() :
#-------------------------------------------------------------------------------#
# print(str('hello')) # output : hello
# print(repr('hello')) # output : 'hello'
'''
From the above output, we can see if we print a string using the repr() function then it prints with a pair of quotes
 and if we calculate a value we get a more precise value than the str() function.
'''

# print(type(str('hello'))) # output : <class 'str'>
# print(type(repr('hello'))) # output : <class 'str'>

#-------------------------------------------------------------------------------#
'''
- In this example, we are creating a DateTime object of the current time and we are printing it into two different formats.
- str() displays today’s date in a way that the user can understand the date and time. repr() prints an “official” representation 
of a date-time object (means using the “official” string representation we can reconstruct the object).
'''
# import datetime
# today = datetime.datetime.now()

# # Prints readable format for date-time object
# print(str(today)) # output : 2024-02-16 14:29:11.340597

# # prints the official format of date-time object
# print(repr(today)) # output : datetime.datetime(2024, 2, 16, 14, 29, 11, 340597)

#-------------------------------------------------------------------------------#

'''
there are function for converting numbers in Octal, Binary, Hexa
oct()
hex()
bin()
'''

print(oct(64)) # output : 0o100 (here 0o represents octal number)
print(hex(64)) # output : 0x40 (here 0x represents hexadecimal number)
print(bin(64)) # output : 0b1000000 (here 0b represents binary number)

# some different methods for converting numbers
# print(int('number in string format', base))
print(int('100', 2)) # output : 4
print(int('100', 8)) # output : 64
print(int('100', 16)) # output : 256
print(int('100', 11)) # output : 121

#-------------------------------------------------------------------------------#
# reverse another number to normal number
print(int('0b10000000', 0)) # output : 128
print(int('0o100', 0)) # output : 164
print(int('0x10', 0)) # output : 16
#-------------------------------------------------------------------------------#