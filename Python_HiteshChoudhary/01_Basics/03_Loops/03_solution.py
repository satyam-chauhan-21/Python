#-------------------------------------------------------------------------------#
#                        3. Multiplication Table Printer
#-------------------------------------------------------------------------------#
# Problem: Print the multiplication table for a given number up to 10, but skip the fifth iteration.

table_number = int(input("Enter number for Table Printer : "))

for i in range(1,11):
    if i == 5:
        continue
    print(table_number, "x", i, "=", i*table_number)