#-------------------------------------------------------------------------------#
#                   5. Find the First Non-Repeated Character
#-------------------------------------------------------------------------------#
# Problem: Given a string, find the first non-repeated character.

input_str = input("Enter String : ")

for char in input_str:
    if input_str.count(char) == 1:
        print(char)
        break # iss "break" se loop aur nahi iterate karega kyoki hame to first non repeated char chahiye vo milne ke baad loop stop ho jayega, but if we don't write break here so loop will iterate after we get out result and this is not optimized method, so putting "break" keyword id optimized approch.

'''
here count(value) used to chack that how many times a value occurs in the string if it returns 1, so it's means that value is only occurs one time & also means that value is not repeating. and if it returns number more than 1 so it means, that value is occurs more than one time and repeating.

so that in this for loop, in if condition becomes true that means given character is not repeating.
'''