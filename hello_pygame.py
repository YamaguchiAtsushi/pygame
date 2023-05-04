import pygame

pygame.init()
screen = pygame.display.set_mode((600, 400))
image = pygame.image.load("doraemon.jpg").convert()

while True:
    pygame.event.clear()
    key_pressed = pygame.key.get_pressed()
    if key_pressed[pygame.K_ESCAPE]:
        break

    screen.fill(pygame.Color("black"))
    screen.blit(image, pygame.mouse.get_pos())
    pygame.display.update()

pygame.quit()