from snake_game_objects import create_screen, create_turtle

main_surface = create_screen("black", (600, 600), "snake Game")
snake_head = create_turtle("square", "cyan")
snake_head.direction = ""
def change_dir_to_up():
    snake_head.direction = "up"
# TODO  نوشتن سه تابع دیگر برای سایر جهت ها

main_surface.listen()
main_surface.onkeypress(change_dir_to_up,"w")
# نوشتن onkeypress برای سایر جهت ها

running = True
while running:
    main_surface.update()