#-------------------------------------------------------------------------------#
#                              7. Validate Input
#-------------------------------------------------------------------------------#
# Problem: Keep asking the user for input until they enter a number between 1 and 10.

while True:
    user_input = int(input("enter number b/w 1 to 10 to stop input : "))
    # below both syntax are same
    # if user_input >= 1 and user_input <= 10:
    if 1<= user_input <= 10:
        print("Well done! you got it.")
        break
    else:
        print("Try again.")