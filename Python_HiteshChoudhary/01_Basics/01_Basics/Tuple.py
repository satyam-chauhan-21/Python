#-------------------------------------------------------------------------------#
#                                   Tuple
#-------------------------------------------------------------------------------#

# Tuple in python are similer to List but the major difference is that, List is mutable and Tuple is immutable.
# means if we once made a Tuple then we can't reassign new element in that or we can't change the existing element in that tuple.
# Tuple is made using () "parantheses" and List is made using [] "brackets".
# and some mathod are also same like: slicing, len().

# here I've made a tuple of colors.
# color = ("Black", "Red", "Green", "Blue", "White")

# # we can access it's elements like this
# print(color[0])
# print(color[2])
# print(color[4])

# # we can't assignn elements in this tuple of color
# color[1] = "Orange" # output : TypeError: 'tuple' object does not support item assignment


#-------------------------------------------------------------------------------#
#                           Concatenatting Tuple
#-------------------------------------------------------------------------------#
# # now suppose we have this color tuple and we have one another tuple is newColor.
# color = ("Black", "Red", "Green", "Blue", "White")
# newColor = ("Orange", "Safron", "Lovander", "Yellow")

# # now we can add this tuples in new tuple like this,
# allColor = color + newColor
# print(allColor) # output : ('Black', 'Red', 'Green', 'Blue', 'White', 'Orange', 'Safron', 'Lovander', 'Yellow')

#-------------------------------------------------------------------------------#
#                          Checking condition in Tuple
#-------------------------------------------------------------------------------#

# chai = ("Black Tea", "Harbal Tea", "Oolong Tea", "Ginger Tea", "Oolong Tea")

# if "Oolong Tea" in chai:
#     print(chai.count("Oolong Tea"))
# else:
#     print("not in chai")

#-------------------------------------------------------------------------------#
#                               Unwrapping Tuple
#-------------------------------------------------------------------------------#
# unwrapping tuple means storing tuples elements in individual variables like below,
# suppoe we have a tuple thing with 3 elements,
thing = ("phone", "mouse", "monitor")
for i in thing:
    print(i)

# # now we want to store this elements in individual variable,
# (var1, var2, var3) = thing # noties here i've used only three variable because the "thing" tuple contains three elements, So create as many variables as there are elements in the tuple.

# print(var1) # output : phone
# print(var2) # output : mouse
# print(var3) # output : monitor
# print(type(var3)) # output : <class 'str'>


