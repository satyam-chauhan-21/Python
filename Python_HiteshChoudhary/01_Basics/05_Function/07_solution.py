#-------------------------------------------------------------------------------#
#                          7. Function with *args
#-------------------------------------------------------------------------------#
# Problem: Write a function that takes variable number of arguments and returns their sum.

'''
function with parameter "*args" can accept multiple arguments.
and this arguments stored in a "tuple".
'''

def sum_all(*args):
    # print(args) # will outputs a tuple means it will stored in a tuple when we use multiple arguments. we can perform all operation or methos of  tuple on this arguments.
    # # like below,
    # for i in args:
    #     print(i * 2)
    # sum(args) # we can't used sum() like this it should be used with return in functions and stored in variables because sum() returns sum of it parameters so it should be stored somewhere. or use it with return statment in function.
    return sum(args)

print(sum_all(1,2,3))
print(sum_all(1,2,3,56,8,4,2,7))
print(sum_all(1,2,3,2,3,5))
print(sum_all(1,2,2,4,5,7,3,8,96,2,5,7,3))