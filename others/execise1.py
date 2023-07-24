import turtle

COLORS = ["red", "green", "blue", "cyan"]
turtle1 = turtle.Turtle()

for j in range(4):
    turtle1.color(COLORS[j])
    turtle1.begin_fill()
    for i in range(4):
        turtle1.forward(100)
        turtle1.left(90)
    turtle1.end_fill()
    turtle1.right(90)

turtle1.ht()
turtle.done()
