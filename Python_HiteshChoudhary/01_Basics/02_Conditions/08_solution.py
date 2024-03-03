#-------------------------------------------------------------------------------#
#                           8. Password Strength Checker
#-------------------------------------------------------------------------------#
# Problem: Check if a password is "Weak", "Medium", or "Strong". Criteria: < 6 chars (Weak), 6-10 chars (Medium), >10 chars (Strong).

password = input("Enter password : ")
pswd_length = len(password)


if pswd_length < 6:
    strength = "Weak"
elif pswd_length <= 10:
    strength = "Meadium"
else:
    strength = "Strong"

print("Strength of Password :", strength)