import math
class point(object):   #user defined type is called class
    """represents a point in space"""
blank = point()

print (point)
print (blank) #The return value is a reference to a Point object, which we assign to blank.Creating a new object is called instantiation, and the object is an instance of the class."""
blank.x = 3.0
blank.y = 4.0
            #we are assigning values to named elements of an object. These elements are called attributes"""
print (blank.y)
x = blank.x
print (x)

print ("%g,%g" %(blank.x,blank.y))
distance = math.sqrt(blank.x**2 + blank.y**2)
print (distance)

#passing instance - in this case - blank as an argument

def print_point(p):
    print("%g,%g" % (p.x,p.y))

print_point(blank)

"""Exercise 1  
Write a function called distance_between_points that takes two Points as arguments and returns the distance between them."""
print("Exercise : 1")

def distance_between_points(p1, p2):
    """Computes the distance between two Point objects."""
    dx = p1.x - p2.x
    dy = p1.y - p2.y
    dist = math.sqrt(dx**2 + dy**2)
    return dist

p1 = point()
p2 = point()
p1.x = 1
p2.x = 10
p1.y = 1
p2.y = 10

print (distance_between_points(p1,p2))

class rectangle(): """text"""

box = rectangle ()
box.width = 100.0
box.height = 200.0
box.corner = point()
box.corner.x = 0.0
box.corner.y = 0.0

#Instances as return values

def find_center(rect):
    p = point()
    p.x = rect.corner.x + rect.width/2.0
    p.y = rect.corner.y + rect.height/2.0
    return p

center = find_center(box)
print_point(center)

#Objects are mutable

box.width = box.width + 50
box.height = box.width + 100

def grow_rectangle(rect, dwidth, dheight):
    rect.width += dwidth
    rect.height += dheight
    return rect.width,rect.height

grow_rectangle(box, 50,100)
print (box.width, box.height)
"""Exercise 2  
Write a function named move_rectangle that takes a Rectangle and two numbers named dx and dy. 
It should change the location of the rectangle by adding dx to the x coordinate of corner and adding dy to the y coordinate of corner."""


#Copying

a1 = point()
a1.x = 3.0
a1.y = 4.0

import copy

b1 = copy.copy(a1)

print_point(a1)
print_point(b1)

print(a1 is b1)
print(a1 == b1)

box1 = copy.copy(box)
print(box1 is box)
print(box1.width == box.width) #This operation is called a shallow copy

#deep copy

box2 = copy.deepcopy(box)
print (box2 is box)
print (box2.corner.x is box.corner)




