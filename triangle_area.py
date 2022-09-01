# Take three sides of a triangle. And then calculate the area of the triangle.


# To calculate the area of the triangle. First, calculate the half of the perimeter. Here perimeter is the sum of each side of the triangle.
# Let’s call it s.

# Then you have to perform square root of the formula like below-


# here we know,
# the perimeter of the triangle 

# s= (a+b+c)/2
# area of triangle area = √(s(s-a)*(s-b)*(s-c))

import math
a = float(input('Enter first side: '))
b = float(input('Enter second side: '))
c = float (input('Enter third side: '))

# calculate semi perimeter

s = (a+b+c)/2

area = math.sqrt(s*(s-a)*(s-b)*(s-c))
print('Area of the given triangle is', round(area))