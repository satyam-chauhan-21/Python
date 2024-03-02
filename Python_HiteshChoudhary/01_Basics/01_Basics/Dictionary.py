#-------------------------------------------------------------------------------#
#                                  Dictionary
#-------------------------------------------------------------------------------#
# it can store Key-Value pair.

# mobileOS = { "Google" : "android", "Apple" : "ios", "Xiaomi" : "hyper os", "Huawei" : "Harmony OS", "BlackBerry" : "BlackBerry os" }

#-------------------------------------------------------------------------------#
#                   accessing individual items in Dictionary
#-------------------------------------------------------------------------------#

# mobileOS = { "Google" : "android", "Apple" : "ios", "Xiaomi" : "hyper os", "Huawei" : "Harmony OS", "BlackBerry" : "BlackBerry os" }
# # for accessing individual item we can write like this
# print(mobileOS["Google"]) # output : android
# print(mobileOS["Apple"]) # output : ios
# print(mobileOS["Huawei"]) # output : Harmony OS
# print(mobileOS["Xiaomi"]) # output : hyper os

# and there is a method called get() used for accessing items of dictionary
# in this method we have to pass key in quotes as argument of get() method
# dictionary_name.get("key")

# print(mobileOS.get("BlackBerry")) # output : BlackBerry os
# print(mobileOS.keys()) # output : dict_keys(['Google', 'Apple', 'Xiaomi', 'Huawei', 'BlackBerry'])
# print(mobileOS.values()) # output : dict_values(['android', 'ios', 'hyper os', 'Harmony OS', 'BlackBerry os'])
# print(mobileOS.items()) # output : dict_items([('Google', 'android'), ('Apple', 'ios'), ('Xiaomi', 'hyper os'), ('Huawei', 'Harmony OS'), ('BlackBerry', 'BlackBerry os')])

#-------------------------------------------------------------------------------#
#                           Looping in Dictionary
#-------------------------------------------------------------------------------#

# mobileOS = { "Google" : "android", "Apple" : "ios", "Xiaomi" : "hyper os", "Huawei" : "Harmony OS", "BlackBerry" : "BlackBerry os" }

# # below for loop will print all the keys of the given dictionary
# for thing in mobileOS:
#     print(thing)

# # # below for loop will print all the keys with it's values
# # for thing in mobileOS:
# #     print(thing, mobileOS[thing])

# # we can individually print key-value using two variable in loop for this we can't directly write dictionary,
# # we have to write like this,
# for key, value in mobileOS.items():
#     print(key,value)


#-------------------------------------------------------------------------------#
#                             adding in Dictionary
#-------------------------------------------------------------------------------#

# mobileOS = { "Google" : "android", "Apple" : "ios", "Xiaomi" : "hyper os", "Huawei" : "Harmony OS", "BlackBerry" : "BlackBerry os" }

# inserting key and value in dictionary
# mobileOS["newKey"] = "newValue"
# print(mobileOS) # output : {'Google': 'android', 'Apple': 'ios', 'Xiaomi': 'hyper os', 'Huawei': 'Harmony OS', 'BlackBerry': 'BlackBerry os', 'newKey': 'newValue'}

#-------------------------------------------------------------------------------#
#                           removeing in Dictionary
#-------------------------------------------------------------------------------#
# dict_name.pop("key_name")
# dict_name.popitem()
# del dict_name["key_name"]
# dict_name.clear() : used to remove all items from dictionary


# removing items in dictionary
# # for that we use pop() method in this method we have to pass key as argument 
# # because in List, pop() method removes last element but here we don't know which is the last element because List has indexing but,
# # Dictionary don't have indexing instead of it has keys 
# mobileOS.pop("Huawei")
# print(mobileOS) # output : {'Google': 'android', 'Apple': 'ios', 'Xiaomi': 'hyper os', 'BlackBerry': 'BlackBerry os'}

# # dict_name.popitem() : used for removing last item of the dictionary
# mobileOS.popitem()
# print(mobileOS) # output : {'Google': 'android', 'Apple': 'ios', 'Xiaomi': 'hyper os', 'Huawei': 'Harmony OS'}

# # del keyword : it remove reference from the memory
# del mobileOS["Google"]
# print(mobileOS) # output : {'Apple': 'ios', 'Xiaomi': 'hyper os', 'Huawei': 'Harmony OS', 'BlackBerry': 'BlackBerry os'}


#-------------------------------------------------------------------------------#
#                           making copy of Dictionary
#-------------------------------------------------------------------------------#

# mobileOS = { "Google" : "android", "Apple" : "ios", "Xiaomi" : "hyper os", "Huawei" : "Harmony OS", "BlackBerry" : "BlackBerry os" }
# suppose if copy an dictionary in another dictionary like this,
# copy_mobileOS = mobileOS
# in above case both the mobileOS and copy_mobileOS are pointing or referencing to the same object in memory. and it is not good way or safe way to capy because it perform any operation on copy diction it will affect our original diction also.

# for making actual copy of dictionary we have to use copy() mehod.

# actualCopyMobileOS = mobileOS.copy()

#-------------------------------------------------------------------------------#
#                               Nested Dictionary
#-------------------------------------------------------------------------------#

# shop = {
#     "glossary" : {
#         "masala" : "haldi",
#         "chai" : "Tata Tea"
#     },
#     "hardware" : {
#         "ciment" : "ambuja",
#         "iron" : "Tata steal"
#     }
# }

# print(shop) # output : {'glossary': {'masala': 'haldi', 'chai': 'Tata Tea'}, 'hardware': {'ciment': 'ambuja', 'iron': 'Tata steal'}}
# print(shop["hardware"]) # output : {'ciment': 'ambuja', 'iron': 'Tata steal'}
# print(shop["glossary"]["masala"]) # output : haldi

#-------------------------------------------------------------------------------#
#                          Dynamic values in Dictionary
#-------------------------------------------------------------------------------#
# # in list we just write what values we needed but in dictionary we have to also provide keys of the values see below example
# squeredNums = {x:x**2 for x in range(10) }
# print(squeredNums) # output : {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}

# squeredNums.clear()
# print(squeredNums) # output : {} (here {} means empty dictionary)

#-------------------------------------------------------------------------------#
#                    creating Dictionary from another way
#-------------------------------------------------------------------------------#

# suppose we have List of key (which will be keys of our dictionary we creating)
keys = ["key1", "key2", "key3", "key4", "key5"]

# and here we are assigning a single or same value to all this keys (we can also make a list of value but now it can be complex we do it later)
default_value1 = "hello"
new_dict1 = dict.fromkeys(keys, default_value1)
print(new_dict1) # output : {'key1': 'hello', 'key2': 'hello', 'key3': 'hello', 'key4': 'hello', 'key5': 'hello'}

# here is a probllem we have a "default_value" list and we want that this value assign one by one to the keys but we get below output, don't worry we will solve this problem 
default_value2 = ["hello1", "hello2"]
new_dict2 = dict.fromkeys(keys, default_value2)
print(new_dict2) # output : {'key1': ['hello1', 'hello2'], 'key2': ['hello1', 'hello2'], 'key3': ['hello1', 'hello2'], 'key4': ['hello1', 'hello2'], 'key5': ['hello1', 'hello2']}
# we will solve this above problem using loops.


