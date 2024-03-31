#-------------------------------------------------------------------------------#
#                         8. Function with **kwargs
#-------------------------------------------------------------------------------#
# Problem: Create a function that accepts any number of keyword arguments and prints them in the format key: value.

# def print_kwaregs(name,power):
#     print(f"name : {name}, power : {power}")

# # we can call function with named arguments.
# print_kwaregs(name="Hitesh",power="Leraning") # output : name : Hitesh, power : Leraning
# print_kwaregs(power="Leraning", name="Hitesh") # output : name : Hitesh, power : Leraning

#-------------------------------------------------------------------------------#

# def print_kwaregs(name,power):
#     print(f"name : {name}, power : {power}")

# print_kwaregs(name="Hitesh",power="Leraning",enamy = "Dr. Jackaal") # output : TypeError: print_kwaregs() got an unexpected keyword argument 'enamy'
# to avoid above error we use "**kwargs" as function parameter.

#-------------------------------------------------------------------------------#

# def print_kwaregs(**kwargs):
#     for key,value in kwargs.items():
#         print(f"{key} : {value}")

# # print_kwaregs(name="Hitesh",power="Leraning",enamy = "Dr. Jackaal")

#-------------------------------------------------------------------------------#

# def print_kwaregs(**kwargs):
#     for key,value in kwargs.items():
#         print(f"{key} : {value}")

# # print_kwaregs(name="Hitesh",power="Leraning",enamy = "Dr. Jackaal")

# dictionay = {
#     "hello" : "hilo",
#     "hello1" : "hilo1",
#     "hello2" : "hilo2",
#     "hello3" : "hilo3",
# }

# print_kwaregs(dictionay) # output : TypeError: print_kwaregs() takes 0 positional arguments but 1 was given

#-------------------------------------------------------------------------------#

# def print_kwaregs(kwargs):
#     for key,value in kwargs.items():
#         print(f"{key} : {value}")

# # print_kwaregs(name="Hitesh",power="Leraning",enamy = "Dr. Jackaal")

# dictionay = {
#     "hello" : "hilo",
#     "hello1" : "hilo1",
#     "hello2" : "hilo2",
#     "hello3" : "hilo3",
# }

# print_kwaregs(dictionay) # output : work properly

#-------------------------------------------------------------------------------#


def print_kwaregs(**kwargs):
    for key,value in kwargs.items():
        print(f"{key} : {value}")

print_kwaregs(name="Hitesh",power="Leraning",enamy = "Dr. Jackaal")
print_kwaregs(name="Hitesh",power="Leraning")
print_kwaregs(name="Hitesh",)