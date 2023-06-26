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


"""
TODO
یک تابع بنویسید که لیستی از اعداد را به عنوان پارامتر بگیرد
و 
مجموع اعداد زوج موجود در آن را محاسبه کند و برگرداند
numbers = [102,109,2,55,67,88]
"""

"""
یک تابع بنویسید که لیستی از اعداد را از ورودی دریافت نماید و 
در صورت صعودی بودن لیست 
True 
و در صورت نزولی بودن لیست
False
را برگرداند

صعودی بودن یعنی هر عدد موجود در لیست از عدد قبلی بزرگتر باشد
مثال
[1,2,3,4,8]   نمونه از لیست صعودی


نزولی:
هر عدد از بعدی کوچکتر باشد

[5,3,1,0]  نمونه یک لیست نزولی


در تابع از 
for   و   if
استفاده کنید
"""