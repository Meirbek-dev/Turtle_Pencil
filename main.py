import turtle as t
from turtle import Screen


def draw(left_or_right, angle, length):
    if left_or_right == "right":
        t.right(angle)
    else:
        t.left(angle)

    t.forward(length)


screen = Screen()
screen.setup(400, 270)
t.colormode(255)
t.getscreen().bgcolor("white")
t.speed(10)
t.pensize(5)

t.penup()
t.goto(135, -30)
t.pendown()

# t.right(180)
t.backward(20)
draw('left', 155, 270)
t.color('grey')

t.fillcolor('red')
t.begin_fill()
t.forward(20)
t.circle(-10, 180)
t.forward(20)
t.circle(-10, -180)
t.end_fill()

t.pensize(3)
t.fillcolor('blue')
t.begin_fill()
t.backward(10)
t.circle(-10, 180)
t.backward(10)
t.circle(-10, -180)
t.end_fill()

t.fillcolor('yellow')
t.begin_fill()
t.backward(10)
t.circle(-10, 180)
t.forward(10)
t.circle(-10, -180)
t.end_fill()

t.fillcolor('blue')
t.begin_fill()
t.backward(10)
t.circle(-10, 180)
t.backward(10)
t.circle(-10, -180)
t.end_fill()

t.circle(-10, 180)
t.pensize(5)
t.forward(250)

t.circle(-10, -180)
draw('right', 155, 20)
draw('left', 120, 20)

t.fillcolor('yellow')
t.begin_fill()
draw('left', 35, 240)
t.pensize(3)
t.circle(10, 180)
t.pensize(4)
t.forward(240)
t.circle(10, -180)
t.end_fill()

t.circle(10, 180)
t.backward(5)
t.color('black')
t.backward(290)

t.hideturtle()
t.done()
