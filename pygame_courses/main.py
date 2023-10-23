import pygame
from pygame.locals import *
pygame.init()
# screen width and height
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 700
# create main window
main_screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
# loading image
wolf_image = pygame.image.load("w.png")
wolf_image = pygame.transform.scale(wolf_image,(96,96))
wolf_rect = wolf_image.get_rect()
wolf_rect.bottom = WINDOW_HEIGHT
wolf_rect.right = WINDOW_WIDTH
# loading font and text
myfont = pygame.font.Font("font.ttf",62)
title = myfont.render(f'Wolf game', True, (255,0,255))
title_rect = title.get_rect()
title_rect.top = 0
title_rect.centerx = WINDOW_WIDTH/2
FPS = 60
clock = pygame.time.Clock()

running = True
# main loop
while running:
    # event loop
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        wolf_rect.y -= 5
    
    main_screen.fill((0,0,0))
    main_screen.blit(wolf_image, wolf_rect)
    main_screen.blit(title,title_rect)
    pygame.display.update()
    clock.tick(FPS)
    
