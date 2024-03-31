#-------------------------------------------------------------------------------#
#                       9. Generator Function with yield
#-------------------------------------------------------------------------------#
# Problem: Write a generator function that yields even numbers up to a specified limit.

# must see :
# https://youtu.be/JptOj-D6gtw?si=zcSEotHImdjHnDFF From => 45:50

'''
yield is similer to return but it store tha stat of loop or functin from where it return.
'''

#-------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------#
# def even_genrator(limit):
#     for i in range(2, limit+1, 2):
#         return i
    
# # above loop will return first element(which is here 2) then function execution will stop

# for num in even_genrator(10):
#     print(num) 
# # now this loop will give error because even_genrator() will return only one integer value then stop and we know that integers are not iterable.
# # TypeError: 'int' object is not iterable

#-------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------#

def even_genrator(limit):
    for i in range(2, limit+1, 2):
        yield i
    
# above loop will return all elements then stop because of "yield" keyword.

for num in even_genrator(10):
    print(num) # work properly