import pygame

pygame.init()
width, height = 600, 400
screen = pygame.display.set_mode((width, height))
font_size = 50
font_file = None
antialias = True
font = pygame.font.Font(font_file, font_size)
text_image = font.render("hello, pygame", antialias, pygame.Color("green"))
player_image = pygame.image.load("doraemon.jpg").convert()

while True:
    pygame.event.clear()
    key_pressed = pygame.key.get_pressed()
    if key_pressed[pygame.K_ESCAPE]:
        break
    mouse_pos = pygame.mouse.get_pos()

    screen.fill(pygame.Color("black"))
    screen.blit(player_image, mouse_pos)
    mouse_x, mouse_y = mouse_pos
    text_offset_x = 100
    screen.blit(text_image, (mouse_x + text_offset_x, mouse_y))
    pygame.display.update()

pygame.quit()