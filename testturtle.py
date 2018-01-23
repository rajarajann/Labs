import turtle
import math

bob = turtle.Turtle()


def circle(t, length, angle, number_of_sides):
    for i in range(number_of_sides):
        t.down()
        t.fd(length)
        t.lt(angle)


circle(bob, 5, math.pi, 115)

print(bob)

turtle.mainloop()