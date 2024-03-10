# for more info see this : https://youtu.be/_VxQ5jzo37o?si=3Eq1WdzYrHxja0oA
'''
in python we can iterate normaly using loops on any object.
- so loops and some other comprehention are called "iterable tools". and object which are iterable are known as "iterable objects".
    example of "iterable object" : list, files, sequence( list, tuple, string)
'''





# important note : first, when i want to open file i am writing below statement
# f = open('exampleFile.py')
# but above line can't open this file and giving this error : FileNotFoundError: [Errno 2] No such file or directory: 'exampleFile.py'
# and then i open terminal and writing same statements in it. and get same error,
# then i noticed that, i'm openning file in files parent diractory thats why this command not working so, then i first open that directory(04_Iterable_tools) in which my file is exist.
# then i write this code "f = open('exampleFile.py')" and it work properly and I also perform realine() method in this file storing variable and guess what it also work properly.
'''
#-----------------------------------------------------------------------------------------#
#                                 open file in terminal
#-----------------------------------------------------------------------------------------#
>>> f = open('exampleFile.py')
>>> f.readline()
'print("this file is made ")\n'
>>> f.readline()
'print("because")\n'
>>> f.readline()
'print("it will be open in loopWorking file")\n'
>>> f.readline()
'print("to understand iterable object")'
>>> f.readline()
''
>>> f.readline()
''
#-----------------------------------------------------------------------------------------#
'''
# extra :.-.-.-.- # storing file in a variable is called making a referance of file. so here, f is referance of file "exampleFile.py".
# now i wanted to open file(exampleFile.py) in this "loopworking" file for that I have to give complete file path form "C drive" to that spacific location in which file is stored. 
# like below code,
# f = open("C:\\Users\\satyam chauhan\\Documents\\Programming Languages\\Python\\Python_HiteshChoudhary\\01_Basics\\04_Iterable_tools\\exampleFile.py")

# # now i want to execute this code "f.readline()" but it's not working properly because it work in terminal not in program file for that we have to write it in print method like given below,
# print(f.readline()) # this first line will give first line of file as output : print("this file is made ")
# print(f.readline()) # this second line will give second line of file as output : print("because")
# print(f.readline()) # this third line will give third line of file as output : print("it will be open in loopWorking file")
# print(f.readline()) # this fourth line will give fourth line of file as output : print("to understand iterable object")
# # now "exampleFile.py" has only four line so that below fifth line will give nothing as output.
# print(f.readline()) # this fifth line will give fifth line of file as output : 


# # we can use __next__() to make any object iterable in python means if any object in python has __next__() so it can be iterable.
# print(f.__next__()) # this first line will give first line of file as output : print("this file is made ")
# print(f.__next__()) # this second line will give second line of file as output : print("because")
# print(f.__next__()) # this third line will give third line of file as output : print("it will be open in loopWorking file")
# print(f.__next__()) # this fourth line will give fourth line of file as output : print("to understand iterable object")
# # now above, we used readline() method to read line in file but in file(exampleFile.py) we don't have any fifth line so it return empty string in terminal and return nothing when using but,
# # if we used __next__() instead of readline() (which is a row form used inner working of python) it will return "StopIteration" exception
# print(f.__next__()) # this fifth line will give fifth line of file as output : 
'''
- StopIteration is a built-in exception in Python that is raised when an iterator has no more items to produce. It is not considered an error, but rather a normal part of the iteration process.
- Python StopIteration is an exception that is raised when an iteration is stopped. It is generally raised by built-in functions that have reached the end of their sequence. For example, when a for loop tries to iterate over an empty sequence, it will raise a StopIteration Exception in Python.
- StopIteration is typically raised by the built-in function next() and an iterator's __next__() method. When an iterator reaches the end of its sequence, it raises StopIteration to signal that there are no further items to iterate over.
'''



# # now see we are reapeting same line again & again so we can do it using loops,
# # using foor loop
# # for line in open("C:\\Users\\satyam chauhan\\Documents\\Programming Languages\\Python\\Python_HiteshChoudhary\\01_Basics\\04_Iterable_tools\\exampleFile.py"):
# #     print(line, end="")

# # using while loop
# f = open("C:\\Users\\satyam chauhan\\Documents\\Programming Languages\\Python\\Python_HiteshChoudhary\\01_Basics\\04_Iterable_tools\\exampleFile.py")

# while True:
#     line = f.readline()
#     # below both if statements are working same 
#     # if not line : break
#     if not line :
#         break
#     print(line, end="")


#-------------------------------------------------------------------------------#
#                                   iter()
#-------------------------------------------------------------------------------#
# must see more about iter(): https://www.geeksforgeeks.org/python-iter-method/  😎😋😊😉 


#-------------------------------------------------------------------------------#
#                          Iterable object : List
#-------------------------------------------------------------------------------#

myList = [ 1, 2, 3, 4, 5]
# print(iter(myList)) # output : <list_iterator object at 0x000001A6249C9690>
#----------------- below two line just for knowledage .-.-.-.-.-.-.-.-.-.-.-.-.-.-
# print("The list is of type : " + type(myList)) # output : TypeError: can only concatenate str (not "type") to str
# print("The list is of type : " + str(type(myList))) # output : The list is of type : <class 'list'>
'''
iter(iterable) : used to convert iterable to the iterator
now here "iter(myList)" convert "myList" into an "list_iterator" and this iterator is pointing to the first element of "myList".
so the output of above print(iter(myList)) is <list_iterator object at 0x000001A6249C9690> means
    list_iterator object is pointing to this memory address( 0x000001A6249C9690 )

    and we can store this memory address in a variable, like below code.
'''
# note : every time we run the program memory adderss can be change.
# print(iter(myList)) # output : <list_iterator object at 0x00000241C0619930>
i = iter(myList) # so think i can say that here i is an "pointer"  🧧🟥🟧🛑✅
# here we can also say that "i" is iterable object of myList
# print(i) # output : <list_iterator object at 0x00000241C0619930>

# print(i.__next__()) # output : 1
# print(i.__next__()) # output : 2
# print(i.__next__()) # output : 3
# print(i.__next__()) # output : 4
# print(i.__next__()) # output : 5
# print(i.__next__()) # output : StopIteration

# # now we can loop through i, ab jo bhi kalakari hogi means internal count variable ko increment karna, pointer ki value aage puch karna and many more work vo sab python internally manage kar leta hai. 
# for elements in i:
#     print(elements)


#-------------------------------------------------------------------------------#
#                          Iterable object : File
#-------------------------------------------------------------------------------#
'''
# by seeing below print stetements we can say that List is not it's iterable object but file is it's iterable object.
'''
# storing file in a variable is called making a referance of file. so here, f is referance of file "exampleFile.py".
# because variable are referance of object stored in memory in python 😅😁
# f = open("C:\\Users\\satyam chauhan\\Documents\\Programming Languages\\Python\\Python_HiteshChoudhary\\01_Basics\\04_Iterable_tools\\exampleFile.py")
# print(iter(f) is f) # output : True

# myList = [1,2,3,4,5]
# print(iter(myList) is myList) # output : False

# #-------------------------------------------------------------------------------#
# # file autometically do this itself,
# f = iter(f) # means python internally does like this.

# # below both line are same.
# print(iter(f) is f) # output : True
# print(iter(f) is f.__iter__()) # output : True

# # see this first,
# # at time point 24:49 https://youtu.be/_VxQ5jzo37o?si=3Eq1WdzYrHxja0oA


#-------------------------------------------------------------------------------#
#                          Iterable object : Dictionary
#-------------------------------------------------------------------------------#
# # dictionary is also an iterable object
# D = {'a' : 1, 'b' : 2}
# # # printting key using loop
# # for key in D:
# #     print(key)

# # now printting it manually for that, first we store memoery address using iter()
# I = iter(D) # here "I" is iterator object of dictionary "D",
# #(after the output of below line) here "I" is keyiterator object of dictionary "D".
# # print(type(I)) # output : <class 'dict_keyiterator'>

# # below both are same, means dono ka kaam same hai internally bhi same chij ko reference kar rahe hai
# print(I.__next__()) # hamne ye line execute huyi and prints key : a ; then pointer update ho gaya 
# print(next(I)) # aur iss line ne key "b" ko print kiya & pointer ko increase kar diya
# print(next(I)) # and ab koi bhi key nahi hone ki vajah se is line ne "StopIteration" exception return kiya.

#-------------------------------------------------------------------------------#
#                   Iterable object : range(start, end, step)
#-------------------------------------------------------------------------------#
# range() is also iterable object.
# print(range(5)) # output : range(0, 5)

R = range(5)
# print(type(R)) # output : <class 'range'>
# next(R) # output : TypeError: 'range' object is not an iterator
# above error means range is not an iterator but it's iterable and if we make it's iterator using iter() then what we get is iteretor.

I = iter(R)
# print(type(I)) # output : <class 'range_iterator'>
print(next(I)) # output : 0
print(next(I)) # output : 1
print(next(I)) # output : 2
print(next(I)) # output : 3
print(next(I)) # output : 4
print(next(I)) # output : "StopIteration" exception