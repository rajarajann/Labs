import math
class point():
    """Represents a point in 2D space"""
p = point()

class rectangle():
    """Represents a rectangle with the attributes width,height and edges"""
rect = rectangle()

rect.width =100.0
rect.height=200.0
rect.edge = point()
rect.edge.x=10          #An object that is an attribute of another object is called embedded
rect.edge.y=10

def print_points(p):
    print ("(%d,%d)" % (p.x,p.y))

def move_rectangle(rect,dx,dy):
    newrect = rectangle()
    newrect.edge = point() #write a version of move_rect and return value of new rect instead of modifying the old one
    newrect.edge.x = rect.edge.x + dx
    newrect.edge.y = rect.edge.y + dy
    return newrect.edge            #The object rect.edge is passed to print_points

def old_rectangle(rect):
    return rect.edge

new = move_rectangle(rect,6,5)
old = old_rectangle(rect)

print_points (new)
print_points (old)
