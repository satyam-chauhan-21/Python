#-------------------------------------------------------------------------------#
#                         Array means List in Python
#-------------------------------------------------------------------------------#
# we can do slicing in List
# myList = ["ele1", "ele2", "ele3", "ele4", "ele5"]
# print(myList[1:3]) # output : ['ele2', 'ele3']


'''
by doing slicing we can add values in the List. but if we insert them using only ""(quotes) then it will add latter by latter of that
values of the string.
'''
# myList[1:3] = "helo"
# print(myList) # output : ['ele1', 'h', 'e', 'l', 'o', 'ele4', 'ele5']

'''
to get rid of this problem we use brackets[] then write values in these brackets using "" quotes for string
'''
# myList[1:3] = ["helo"]
# print(myList) # output : ['ele1', 'helo', 'ele4', 'ele5']
# myList[1:3] = ["helo", "bello"]
# print(myList) # output : ['ele1', 'helo', 'bello', 'ele4', 'ele5']
# myList[1:3] = ["helo", "bello", "chello"]
# print(myList) # output : ['ele1', 'helo', 'bello', 'chello', 'ele4', 'ele5']


# myList[1:3] = 23
# print(myList) # output => TypeError: can only assign an iterable
# myList[1:3] = "23"
# print(myList) # output => ['ele1', '2', '3', 'ele4', 'ele5']
# myList[1:3] = ["23"]
# print(myList) # output => ['ele1', '23', 'ele4', 'ele5']

#-------------------------------------------------------------------------------#
# print(myList[1:1]) # output : []
#-------------------------------------------------------------------------------#

# # now suppos if we insert some values or elements in above slicing position like
# myList[1:1] = ["hello1", "hello2"]
# # print(myList)
# # so it will return same as above slicing's dycing => ['ele1', 'hello1', 'hello2', 'ele2', 'ele3', 'ele4', 'ele5']
# # but if assign some empty like 
# myList[1:3] = [] # here we want to say that assign nothing([] means nothing or empty array or empty) at index 1 and 2
# print(myList) # we can also called it delete operation

#-------------------------------------------------------------------------------#
#                         Iterating through the loop
#-------------------------------------------------------------------------------#

# Things = ["phone", "mouse", "keyboard", "moniter", "cpu", "speaker", "earbuds"]

# this below for loop automaticlly prints all elements in new line
# for thing in Things:
#     print(thing)

# this loop will not print element with new line but with a space we give in 'end = "values" '
# for thing in Things:
#     print(thing, end = " ") # output : phone mouse keyboard moniter cpu speaker earbuds

# for thing in Things:
#     print(thing, end = "-") # output : phone-mouse-keyboard-moniter-cpu-speaker-earbuds-

#-------------------------------------------------------------------------------#
#                         checking conditions in List
#-------------------------------------------------------------------------------#

# Things = ["phone", "mouse", "keyboard", "moniter", "cpu", "speaker", "earbuds"]

# if "cpu" in Things:
#     print("yes, it present")
# else:
#     print("no, it's not present")

#-------------------------------------------------------------------------------#
#                             some methods in List
#-------------------------------------------------------------------------------#
# append("value")
# pop()
# remove("value_which_removed")
# insert(position, "value") => build this insert function your own in python 🟥🧇 like mysirji.com build ARRAY in C++ at chai or code channel

# Things = ["phone", "mouse", "keyboard", "moniter", "cpu", "speaker", "earbuds"]
# append("value") : value of append is inserted in at the end of the List.
# print(Things.append("computer")) # output : None
# Things.append("computer")
# print(Things) # output : ['phone', 'mouse', 'keyboard', 'moniter', 'cpu', 'speaker', 'earbuds', 'computer']

# pop() ke baare me kuch bhi description nahi milega. khud dhundh lo. thodi information, pop() will return the last value in python shell.
# Things.pop()
# Things.pop()
# print(Things) # output : ['phone', 'mouse', 'keyboard', 'moniter', 'cpu', 'speaker']

# remove("value_which_removed") : removed desired value from list and does not returns like pop() mathod.
# Things.remove("keyboard")
# print(Things) # output : ['phone', 'mouse', 'moniter', 'cpu', 'speaker', 'earbuds']

# insert(position, "value") : used to insert value at desired position.
# Things.insert(2, "INSERT_value")
# print(Things) # output : ['phone', 'mouse', 'INSERT_value', 'keyboard', 'moniter', 'cpu', 'speaker', 'earbuds']

#-------------------------------------------------------------------------------#
#                             Making Copy of List
#-------------------------------------------------------------------------------#

# Things = ["phone", "mouse", "keyboard", "moniter", "cpu", "speaker", "earbuds"]
# suppose we have above List named "Things" and we want to make it's copy, now if do it like below

# copyThings = Things
# in this both "Things" and "copyThings" are pointing to the same object or refference in memory in python and if we do any operation on "copyThings" it will
# affetc our original List because List in python are immutable.
# copyThings.pop()
# print(copyThings) # output : ['phone', 'mouse', 'keyboard', 'moniter', 'cpu', 'speaker']
# print(Things) # output : ['phone', 'mouse', 'keyboard', 'moniter', 'cpu', 'speaker']
# # so that this is not good way to copy List in python.

# to solve above problem there is a method called copy() which make actual copy of List.
# and operation on copied list does not affect real List.
# actualCopyOfThings = Things.copy()

# # actualCopyOfThings.pop()
# # print(actualCopyOfThings) # output : ['phone', 'mouse', 'keyboard', 'moniter', 'cpu', 'speaker']
# # print(Things) # output : ['phone', 'mouse', 'keyboard', 'moniter', 'cpu', 'speaker', 'earbuds']

#-------------------------------------------------------------------------------#
#                         assigning Dynamic values List
#-------------------------------------------------------------------------------#

squareList = [x**2 for x in range(10)]
print(squareList) # output : [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

cubesList = [x**3 for x in range(10)]
print(cubesList) # output : [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]