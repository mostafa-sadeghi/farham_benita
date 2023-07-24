from snake_game_objects import create_screen, create_turtle
from snake_game_actions import move, change_position
from time import sleep

main_surface = create_screen("black", (600, 600), "snake Game")
snake_head = create_turtle("square", "cyan")
snake_head.direction = ""

snake_food = create_turtle("circle", "red")
change_position(snake_food)


def change_dir_to_up():
    snake_head.direction = "up"


def change_dir_to_down():
    snake_head.direction = "down"


# TODO
"""
تمرین
اضافه کردن حرکت به سمت چپ و راست

"""


main_surface.listen()
main_surface.onkeypress(change_dir_to_up, "Up")
main_surface.onkeypress(change_dir_to_down, "Down")

running = True
while running:
    main_surface.update()
    move(snake_head)
    sleep(0.2)
