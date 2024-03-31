#-------------------------------------------------------------------------------#
#                     4. Function Returning Multiple Values
#-------------------------------------------------------------------------------#
# Problem: Create a function that returns both the area and circumference of a circle given its radius.

import math

def circle(radius):
    area = math.pi * radius ** 2
    circumference = 2 * math.pi * radius
    return area,circumference

area, circumference = circle(5)

print(f"area is {round(area,2)} and circumference is {round(circumference,2)} of circle.")