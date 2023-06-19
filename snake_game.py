import turtle
import random
import time

snake_bodies = []
score = 0
high_score = 0


def make_turtle(tshape, tcolor):
    my_turtle = turtle.Turtle()
    my_turtle.shape(tshape)
    my_turtle.color(tcolor)
    my_turtle.penup()
    my_turtle.speed("fastest")
    return my_turtle


def change_food_position():
    random_x = random.randint(-270, 270)
    random_y = random.randint(-270, 270)
    food.goto(random_x, random_y)


def move_snake():
    if snake_head.direction == "up":
        yposition = snake_head.ycor()
        yposition += 20
        snake_head.sety(yposition)
    if snake_head.direction == "down":
        yposition = snake_head.ycor()
        yposition -= 20
        snake_head.sety(yposition)
    if snake_head.direction == "left":
        xposition = snake_head.xcor()
        xposition -= 20
        snake_head.setx(xposition)
    if snake_head.direction == "right":
        xposition = snake_head.xcor()
        xposition += 20
        snake_head.setx(xposition)


def go_up():
    if snake_head.direction != "down":
        snake_head.direction = "up"


def go_down():
    if snake_head.direction != "up":
        snake_head.direction = "down"


def go_left():
    if snake_head.direction != "right":
        snake_head.direction = "left"


def go_right():
    if snake_head.direction != "left":
        snake_head.direction = "right"


def reset():
    global score, high_score
    high_score = score
    score = 0
    score_pen.clear()
    score_pen.write(
        f"Score: {score}\tHighScore: {high_score}", align="center", font=48)

    snake_head.goto(0, 0)
    snake_head.direction = "none"
    for body in snake_bodies:
        body.hideturtle()

    snake_bodies.clear()


main_surface = turtle.Screen()
main_surface.bgcolor('black')
main_surface.setup(width=600, height=600)
main_surface.title('Snake Game')
main_surface.tracer(0)

snake_head = make_turtle("square", "blue")
snake_head.direction = "none"

food = make_turtle("circle", "red")
change_food_position()

score_pen = make_turtle("square", "white")
score_pen.hideturtle()
score_pen.goto(0, 260)
score_pen.write(
    f"Score: {score}\tHighScore: {high_score}", align="center", font=48)


main_surface.listen()
main_surface.onkeypress(go_up, "Up")
main_surface.onkeypress(go_down, "Down")
main_surface.onkeypress(go_left, "Left")
main_surface.onkeypress(go_right, "Right")

running = True
while running:
    main_surface.update()

    if snake_head.distance(food) < 20:
        score += 1
        score_pen.clear()
        score_pen.write(
            f"Score: {score}\tHighScore: {high_score}", align="center", font=48)

        change_food_position()
        new_tail = make_turtle("square", "cyan")
        snake_bodies.append(new_tail)

    for i in range(len(snake_bodies) - 1, 0, -1):
        prev_x = snake_bodies[i-1].xcor()
        prev_y = snake_bodies[i-1].ycor()
        snake_bodies[i].goto(prev_x, prev_y)
    if len(snake_bodies) > 0:
        x_head = snake_head.xcor()
        y_head = snake_head.ycor()
        snake_bodies[0].goto(x_head, y_head)

    if snake_head.xcor() > 290 or snake_head.xcor() < -290 or snake_head.ycor() > 290 or snake_head.ycor() < -290:
        reset()

    move_snake()

    for body in snake_bodies:
        if body.distance(snake_head) < 20:
            reset()

    time.sleep(0.2)
