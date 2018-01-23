import math
import turtle
bob = turtle.Turtle()
window = turtle.Screen()

class point():
    """Represents a point in 2D space"""
p = point()

class rectangle():
    """Represents a rectangle with the attributes width,height and edges"""

rect = rectangle()
rect.width =100.0
rect.height=200.0
rect.edge = point()
rect.edge.x=-100
rect.edge.y=-100

def draw_rect(bob):
    bob.penup()
    bob.setposition(rect.edge.x,rect.edge.y)
    bob.pendown()
    for i in range (2):
        bob.fd(rect.width)
        bob.lt(90)
        bob.fd(rect.height)
        bob.lt(90)

draw_rect(bob)
window.exitonclick()




