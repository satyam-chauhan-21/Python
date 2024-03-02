#-------------------------------------------------------------------------------#
#                               Strings in Python
#-------------------------------------------------------------------------------#
# # we can store string using single, double & triple quotes in python.
# name1 = 'hello'
# name2 = "hellu"
# name3 = '''helly'''

# print(name1)
# print(name2)
# print(name3)


#-------------------------------------------------------------------------------#
#                   String is treated as List(Array)
#-------------------------------------------------------------------------------#
# so we can use all the property or methods of List in String.

# name = "karan"
# first_char = name[0]
# print(first_char)

#-------------------------------------------------------------------------------#
#                               Slicing of String
#-------------------------------------------------------------------------------#
# '''
# how to slice : string_name[starting_index : ending_index(Which is not included) : jumping_index]
# '''
# str1 = "Karan is Pagal"
# sliced_str = str1[0:5]
# print(sliced_str) # output : karan

# # some operation on slicing so it yourself
# number_list ="012345678"

# sliced_str = number_list[:]
# print(sliced_str) # output : 012345678

# sliced_str = number_list[:5]
# print(sliced_str) # output : 01234

# sliced_str = number_list[2:]
# print(sliced_str) # output : 2345678

# sliced_str = number_list[0:8:2]
# print(sliced_str) # output : 0246

#-------------------------------------------------------------------------------#
#                             some methods of String
#-------------------------------------------------------------------------------#

# string_name.lower() : used to convert string in lower case
# string_name.upper() : used to convert string in upper case
# but this methods does not affect our original string because string is immutable

# name = "Lemon Tea"
# print(name.lower()) # output : lemon tea
# print(name.upper()) # output : LEMON TEA

#-------------------------------------------------------------------------------#
#      strip() : this method remove all spaces before and after the string
#-------------------------------------------------------------------------------#

# str_1 = "   Hello Jenna  "
# print(str_1) 
# '''
# will print string with spaces but if we want to remove this spaces ther is a method called 
#     strip() : this method remove all spaces before and after the string.
# '''
# print(str_1.strip())

#-------------------------------------------------------------------------------#
#          replace("value in original string", "value to replace with")
#-------------------------------------------------------------------------------#

# chai = "Lemon Tea"
# print(chai) # output : Lemon Tea
# print(chai.replace("Lemon", "Not")) # output : Not Tea

#-------------------------------------------------------------------------------#
#                         Converting String in to List 
#-------------------------------------------------------------------------------#
# split() : used to convert string into a List

# chai = "Lemon, Ginger, Masala, Oolong, Ice"
# print(chai.split()) # output : ['Lemon,', 'Ginger,', 'Masala,', 'Oolong,', 'Ice']
# '''
# in above's print statement split() method converted string into List on the bases of space means it make elements 
# in List until any space occurs if the space is occurs in string it make another element until another space is 
# not occur. but we can give parameter so that it consider that params we gives to it, if that parameter occurs 
# in the string so itmes will made by that parameter.
# '''

# print(chai.split(", ")) # output : ['Lemon', 'Ginger', 'Masala', 'Oolong', 'Ice']
# '''
# in above example we give parameter like if ", " a comma and space comes in string the cut and make another 
# element of the List
# '''

#-------------------------------------------------------------------------------#
#                              find() in string 
#-------------------------------------------------------------------------------#
# this mathod is used to find any element in a string it can be a string or a character or anything. and if that element is not present in the string so it will return "-1".
# nameOfTea = "Ginger Chai"

# print(nameOfTea.find("Chai")) # output : 7
# print(nameOfTea.find("chai")) # output : -1

#-------------------------------------------------------------------------------#
#                              count() in string 
#-------------------------------------------------------------------------------#
# '''
# # this method will return the count of the given value, means it returns the count of the value we give as 
# parameter to this count() method.
# '''
# greettings = "very very very goood morning"
# print(greettings.count("very")) # output : 3

# greettings = "very very vary goood morning"
# print(greettings.count("vary")) # output : 1

#-------------------------------------------------------------------------------#
#                     putting variables into another string
#-------------------------------------------------------------------------------#

# pizza1 = "Italian"
# pizza2 = "Neapolitan"
# pizza3 = "Detroit"
# pizza4 = "French Break"
# pizza5 = "Bagel"
# quantity = 3

# orderedPizza = "I have order {} delicious {} pizza's."
# print(orderedPizza) # output : I have order {} delicious {} pizza's.
# print(orderedPizza.format(quantity,pizza1)) # output : I have order 3 delicious Italian pizza's.

# pizz = ["Italian", "Neapolitan", "Detroit", "French Break", "Bagel"]
# # i want to use math.random method to put different values in below string's second {} braces. so build that algo.
# orderedPizza = "I have order {} delicious {} pizza's."

#-------------------------------------------------------------------------------#
#                              List to String
#-------------------------------------------------------------------------------#
# "".join(List_name) : used to convert List into a string.

# myList = ["karan", "manav", "mihir", "ravi"]

# # print(type("".join(myList))) # output : karanmanavmihirravi
# # print(" ".join(myList)) # output : karan manav mihir ravi
# # print(", ".join(myList)) # output : karan, manav, mihir, ravi
# # print("-".join(myList)) # output : karan-manav-mihir-ravi
# # print("*".join(myList)) # output : karan*manav*mihir*ravi
# # print("->".join(myList)) # output : karan->manav->mihir->ravi

# # print(type("".join(myList))) # output : <class 'str'>

#-------------------------------------------------------------------------------#
#                           printing special character
#-------------------------------------------------------------------------------#

# words = "he said, \"programming is good\""
# print(words) # output : he said, "programming is good"

# # printing row string

#-------------------------------------------------------------------------------#
# fullName = "manav\nchavda"
# print(fullName) # will print name in two rows. to print as it is with "\n" we can use "r" before string initialization
# fullName = r"manav\nchavda"
# print(fullName) # output : manav\nchavda

# this can be used in storing path
path = r"c:\user\folder1\folder2"
print(path) # output : c:\user\folder1\folder2

# path2 = "c:\user\folder1\folder2"
# print(path2) # SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \uXXXX escape

path3 = "c:\\user\\folder1\\folder2"
print(path3) # output : c:\user\folder1\folder2