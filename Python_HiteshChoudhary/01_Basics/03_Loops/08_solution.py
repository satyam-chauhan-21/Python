#-------------------------------------------------------------------------------#
#                            8. Prime Number Checker
#-------------------------------------------------------------------------------#
# Problem: Check if a number is prime.

number = int(input("enter number to check prime : "))
is_prime = True

if number > 1:
     for i in range(2,number):
          if number % i == 0:
               is_prime = False
               break

if is_prime:
     print(number, "is Prime.")
else:
     print(number, "is Not Prime.")
