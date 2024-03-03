#-------------------------------------------------------------------------------#
#                           5. Weather Activity Suggestion
#-------------------------------------------------------------------------------#
# Problem: Suggest an activity based on the weather 
# (e.g., Sunny - Go for a walk, Rainy - Read a book, Snowy - Build a snowman).

# here i use .lower() at the end in case user enter capitalized value it will converted in lower case.
# and this will usefull because in "if" constion we use lower case values to check condition.
weather = input("Enter Weather 1.Sunny 2.Rainy 3.Snowy : ").lower()

if weather == "sunny":
    activity = "Go for a walk"
elif weather == "rainy":
    activity = "Read a book"
elif weather == "snowy":
    activity = "Build a snowman"

print(activity)