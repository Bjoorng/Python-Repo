import turtle

window = turtle.Screen()
window.setup(1000, 1000)
side = turtle.Turtle()
side.color('red')
side.pensize(4)

side.hideturtle()
side.penup()
side.goto(-200, -400)

for i in range (4):
    side.hideturtle()
    side.pendown()
    side.speed(0)
    side.forward(300)
    side.penup()
    side.speed(1)
    side.left(90)