from snake_game_objects import create_screen, create_turtle
from snake_game_actions import move, change_position
from time import sleep

main_surface = create_screen("black", (600, 600), "snake Game")
snake_head = create_turtle("square", "cyan")
snake_head.direction = ""

score = 0
high_score = 0

snake_food = create_turtle("circle", "red")
change_position(snake_food)


score_board = create_turtle("square", "orange")
score_board.ht()
score_board.goto(0, 260)


def change_dir_to_up():
    snake_head.direction = "up"


def change_dir_to_down():
    snake_head.direction = "down"


def change_dir_to_right():
    snake_head.direction = "right"


def change_dir_to_left():
    snake_head.direction = "left"


main_surface.listen()
main_surface.onkeypress(change_dir_to_up, "Up")
main_surface.onkeypress(change_dir_to_down, "Down")
main_surface.onkeypress(change_dir_to_left, "Left")
main_surface.onkeypress(change_dir_to_right, "Right")

def close():
    global running
    running = False


root = main_surface._root
root.protocol("WM_DELETE_WINDOW", close)


snake_tails = list()
running = True
while running:
    score_board.clear()
    score_board.write(f"Score: {score}, HighScore: {high_score}", align="center", font=("arial", 22))
    main_surface.update()
    # collision detection
    if snake_head.distance(snake_food) < 20:
        score += 1
        if score > high_score:
            high_score = score
        change_position(snake_food)
        new_tail = create_turtle("square", "cyan")
        snake_tails.append(new_tail)

    for i in range(len(snake_tails) - 1, 0, -1):
        x = snake_tails[i-1].xcor()
        y = snake_tails[i-1].ycor()
        snake_tails[i].goto(x, y)

    if len(snake_tails) > 0:
        snake_tails[0].goto(snake_head.xcor(), snake_head.ycor())

    if snake_head.xcor() > 290 or snake_head.xcor() < -290 or snake_head.ycor() > 290 or snake_head.ycor() < -290:
        snake_head.goto(0, 0)
        snake_head.direction = ""
        for body in snake_tails:
            body.hideturtle()
        snake_tails.clear()
        score = 0

    move(snake_head)
    sleep(0.2)
