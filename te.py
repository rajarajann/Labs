import turtle
umme = turtle.Turtle()
umme.color("red")
raj = turtle.Turtle()
window = turtle.Screen()
def square (t,len,n):
        angle = 360 / n
        for i in range (n):
            t.fd(len)
            t.lt(angle)

square (raj,100,3)
square (umme,50,8)

window.exitonclick()