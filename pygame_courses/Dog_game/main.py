import pygame
pygame.init()
screen = pygame.display.set_mode()
SCREEN_WIDTH = screen.get_width()
SCREEN_HEIGHT = screen.get_height()
FPS = 60
clock = pygame.time.Clock()
start_time = pygame.time.get_ticks()

my_font = pygame.font.Font('assets/font.ttf',64)
welcome_text = my_font.render('Welcome To My Game', True, (255,20,170))
welcome_rect = welcome_text.get_rect(center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2))


dog_img = pygame.image.load("assets/dog.png")
dog_rect = dog_img.get_rect(bottom = SCREEN_HEIGHT, centerx = SCREEN_WIDTH/2)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
    screen.fill((0,0,0))
    if pygame.time.get_ticks() - start_time < 3000:
        screen.blit(welcome_text, welcome_rect)
    else:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            dog_rect.x -= 5
        screen.blit(dog_img, dog_rect)
    pygame.display.update()
    clock.tick(FPS)