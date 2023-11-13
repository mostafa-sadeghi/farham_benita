import random
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
wolf_image = pygame.transform.scale(wolf_image, (96, 96))
wolf_rect = wolf_image.get_rect()
wolf_rect.bottom = WINDOW_HEIGHT
wolf_rect.right = WINDOW_WIDTH

meat_image = pygame.image.load("m.png")
meat_rect = meat_image.get_rect()
meat_rect.center = (24, random.randint(124, WINDOW_HEIGHT-24))
# loading font and text
myfont = pygame.font.Font("font.ttf", 62)
title = myfont.render(f'Wolf game', True, (255, 0, 255))
title_rect = title.get_rect()
title_rect.top = 0
title_rect.centerx = WINDOW_WIDTH/2

bg_music = pygame.mixer.Sound("Eggs.wav")
bg_music.play(-1)

catch_sound = pygame.mixer.Sound("Chomp.wav")


score = 0
score_text = myfont.render(f'Score: {score}', True, (255, 0, 255))
score_rect = score_text.get_rect(topleft=(0,0))




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
    # check if up arrow key pressed and wolf not exited from the above of the screen
    if keys[pygame.K_UP] and wolf_rect.top > 0:
        wolf_rect.y -= 5
    if keys[pygame.K_DOWN] and wolf_rect.bottom < WINDOW_HEIGHT:
        wolf_rect.y += 5

    meat_rect.x += 5
    if meat_rect.x > WINDOW_WIDTH:
        meat_rect.center = (24, random.randint(124, WINDOW_HEIGHT-24))

    if wolf_rect.colliderect(meat_rect):
        meat_rect.center = (24, random.randint(124, WINDOW_HEIGHT-24))
        score += 1
        catch_sound.play()
        
    score_text = myfont.render(f'Score: {score}', True, (255, 0, 255))

    # draw images on the screen
    main_screen.fill((0, 0, 0))
    main_screen.blit(wolf_image, wolf_rect)
    main_screen.blit(meat_image, meat_rect)
    main_screen.blit(title, title_rect)
    main_screen.blit(score_text, score_rect)
    pygame.display.update()
    clock.tick(FPS)
