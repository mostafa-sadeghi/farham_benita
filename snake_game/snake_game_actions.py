from random import randint


def move(snake_head):
    if snake_head.direction == "up":
        ypos = snake_head.ycor()
        ypos += 20
        snake_head.sety(ypos)

    if snake_head.direction == "down":
        ypos = snake_head.ycor()
        ypos -= 20
        snake_head.sety(ypos)


def change_position(food):
    x = randint(-240, 240)
    y = randint(-240, 240)
    food.goto(x, y)
