
ac = int(input("Please enter the Arc length (in degrees):    "))
import turtle
import math
raj = turtle.Turtle()
window = turtle.Screen()
window.bgcolor("yellow")
raj.shape("turtle")
raj.pencolor("red")
raj.pensize(10)
                           #Task1: calling function with no arguments, just to draw a square is called encapsulation
                           #Task2: calling by passing t as parameter and raj as argument is called genralization
                           #calling for function to ease our program
                           #Task3: added l as a parameter for length
"""def square (t,l):
    for i in range (4):
        t.fd(l)
        t.lt(90)"""         #Task5: adding parameter n for angle to be used inside the program
                            #also name the modify the function to draw polygons

def polygon (t,l,n,arc_length):
    angle = (360/n)
    arc_length = int (arc_length)

    for i in range (arc_length):
        t.fd(l)
        t.lt(angle)
                           #Task6: function for circle
def circle(t,radius,n,arc_angle):
    circumference = (2*math.pi*radius)
    arc_length = (arc_angle / 360) * circumference
    length = (circumference / n)
    polygon (t,length,n,arc_length)



circle (raj,75,500,ac)
window.exitonclick()