from turtle import Screen, Turtle
from random import randint


def make_screen():
    window = Screen()
    window.bgcolor('black')
    window.title("Snake Game")
    window.setup(width=600, height=600)
    return window


main_surface = make_screen()


def make_turtle(tshape, tcolor):
    my_turtle = Turtle()
    my_turtle.shape(tshape)
    my_turtle.color(tcolor)
    my_turtle.penup()
    my_turtle.speed("fastest")
    return my_turtle


def change_food_position():
    x = randint(-270, 270)
    y = randint(-270, 270)
    snake_food.goto(x,y)


snake_head = make_turtle("square", "blue")

snake_food = make_turtle("circle", "red")
change_food_position()


running = True
while running:
    main_surface.update()

