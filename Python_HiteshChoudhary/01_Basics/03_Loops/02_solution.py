#-------------------------------------------------------------------------------#
#                             2. Sum of Even Numbers
#-------------------------------------------------------------------------------#
# Problem: Calculate the sum of even numbers up to a given number n.

n = int(input("Enter number : "))

sum_even = 0

# for i in range(2, n+1, 2):
#     print(i, end = " ")
#     sum = sum + i

for i in range(1, n+1):
    if i % 2 == 0:
        sum_even = sum_even + i

print("sum of even number upto", n, "is", sum_even,"\n")