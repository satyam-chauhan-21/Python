#-------------------------------------------------------------------------------#
#                              3. Grade Calculator
#-------------------------------------------------------------------------------#
# Problem: Assign a letter grade based on a student's score: A (90-100), B (80-89), C (70-79), 
# D (60-69), F (below 60).

score = int(input("enter score (between 0 to 100) : "))

if score >= 101 or score < 0:
    print("Invalid score")
    exit()

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print("Your Grade is ", grade)