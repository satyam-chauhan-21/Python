#-------------------------------------------------------------------------------#
#                         1. Age Group Categorization
#-------------------------------------------------------------------------------#
# Classify a person's age group: Child (< 13), Teenager (13-19), Adult (20-59), Senior (60+).

while 1:
    print("\nEnter 0 for exit from the Program.")
    age = int(input("enter age : "))
    # print(age)
    # print(type(age))
    if age == 0:
        exit()
    else :
        if age < 13 :
            print("Child")
        elif age >= 13 and age <= 19 :
            print("Teenager")
        elif age >= 20 and age <= 59 :
            print("Adult")
        else :
            print("Senior")