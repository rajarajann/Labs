import math

"""Area of a square"""

a = int (input("Enter the side for square's area:"))
b = int (input("Enter the radius for circle's area:"))
c = int (input("Enter the radius for sphere's area:"))
def area_square(side):
    area_square = side * side
    return area_square
"""Area of a circle"""
def area_circle(radius):
    area_circle = (2*math.pi*radius)
    return area_circle
"""Area of a sphere"""
def area_sphere(radius):
    area_sphere = ((4/3)*math.pi*(radius**2))
    return area_sphere
print ("Square :",area_square(a))
print ("Circle :",area_circle(b))
print ("Sphere :",area_sphere(c))



