from turtle import Screen, Turtle
def create_screen(back_color, size, window_title):
    my_screen = Screen()
    my_screen.bgcolor(back_color)
    my_screen.setup(size[0], size[1])
    my_screen.title(window_title)
    return  my_screen

def create_turtle(turtle_shape, turtle_color):
    my_turtle = Turtle()
    my_turtle.shape(turtle_shape)
    my_turtle.color(turtle_color)
    my_turtle.speed("fastest")
    my_turtle.penup()
    return  my_turtle

