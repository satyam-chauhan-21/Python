#-------------------------------------------------------------------------------#
#                           4. Fruit Ripeness Checker
#-------------------------------------------------------------------------------#
# Problem: Determine if a fruit is ripe, overripe, or unripe based on its color. 
# (e.g., Banana: Green - Unripe, Yellow - Ripe, Brown - Overripe)

fruit = input("Enter Fruit Name : ")
color = input("Enter Fruit Colour, \nGreen \nYellow \nBrown \n")

if fruit == "Banana":
    if color == "Green":
        print(fruit,"is Unripe")
    elif color == "Yellow":
        print(fruit,"is Ripe")
    elif color == "Brown":
        print(fruit,"is Overripe")
if fruit == "Mango":
    if color == "Green":
        print(fruit,"is Unripe")
    elif color == "Yellow":
        print(fruit,"is Ripe")
    elif color == "Brown":
        print(fruit,"is Overripe")
else:
    print("Currenlty we only have Info about Banana and Mango")