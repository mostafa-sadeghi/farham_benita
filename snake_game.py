from turtle import Screen, Turtle
from random import randint
# TODO یک تابع بسازید که کارش ایجاد صفحه می باشد
def make_screen():
    pass
main_surface = Screen()
main_surface.bgcolor('black')
main_surface.title("Snake Game")
main_surface.setup(width=600, height=600)
def make_turtle(tshape, tcolor):
    my_turtle = Turtle()
    my_turtle.shape(tshape)
    my_turtle.color(tcolor)
    my_turtle.penup()
    my_turtle.speed("fastest")
    return my_turtle
def change_food_position():
    pass
snake_head = make_turtle("square", "blue")

snake_food = make_turtle("circle", "red")

running = True
while running:
    main_surface.update()
