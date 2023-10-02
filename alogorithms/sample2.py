# import turtle

# my_screen = turtle.Screen()
# my_turtle = turtle.Turtle()


# def draw_star(x, y, color):
#     my_turtle.penup()
#     my_turtle.pencolor(color)
#     my_turtle.goto(x, y)
#     my_turtle.pendown()
#     for i in range(5):
#         my_turtle.fd(140)
#         my_turtle.rt(144)


# star_color_1 = my_screen.textinput(
#     "color selection", "Which color do you want(example:'red'):")

# draw_star(-220, 0, star_color_1)
# draw_star(0, 0, "orange")
# draw_star(220, 0, "red")
# draw_star(220, 220, "green")

# turtle.done()


'''
1  => 1st
2  => 2nd
3  => 3rd

11 => 11th
12 => 12th
13 => 13th

otherwise  =>th

101  => 101st
111  => 111th

31 => 31st
4 => 4th
'''


def ordinalSuffix(number):

    if number % 100 in (11,12,13):
        return str(number) + "th"
        # print(number,"th")
    elif number % 10 == 1:
        return f'{number}st'
    elif number % 10 == 2:
        return f'{number}nd'
    elif number % 10 == 3:
        return f'{number}rd'
    else:
        return f'{number}th'
    

x = ordinalSuffix(113)
print(x)
x = ordinalSuffix(501)
print(x)
x = ordinalSuffix(502)
print(x)