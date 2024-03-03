#-------------------------------------------------------------------------------#
#                           7. Coffee Customization
#-------------------------------------------------------------------------------#
# Problem: Customize a coffee order: "Small", "Medium", or "Large" with an option for "Extra shot" of espresso.

coffee_size = input("Coffee size 1.Small 2.Meadium 3.Large : ")
extra_short = input("Extra short yes or no : ").lower()

if extra_short == "yes":
    coffee = coffee_size + " coffee with an extra short"
elif extra_short == "no":
    coffee = coffee_size + " coffee" 
else:
    print("please enter only Yes or No")
    exit()

print("Order :", coffee)