#-------------------------------------------------------------------------------#
#                          9. List Uniqueness Checker
#-------------------------------------------------------------------------------#
# Problem: Check if all elements in a list are unique. If a duplicate is found, exit the loop and print the duplicate.

items = ["apple", "banana", "orange", "apple", "mango"]

unique_item = set()

for item in items:
    if item in unique_item:
        print("Duplicate :", item)
        break
    unique_item.add(item)

print(type(unique_item)) # output : <class 'set'>
'''
here we take variable "unique_item" and assign an empty "set()" to it then we are adding "item" of List "items" in "unique_item" using this for Loop and, but before adding this items in "unique_item" we are checking , if that item is already present in "unique_item" or not, if that item is present in "unique_item" so that item is "Duplicate" and print that Item.
'''
'''
note that here we are using a set(). and set() does not cantains any type of "Duplicated" value in it. that why we are using it.
'''