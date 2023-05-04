import pygame


def init_screen():
    pygame.init()
    width, height = 600, 400
    screen = pygame.display.set_mode((width, height))
    return screen


def create_text():
    font_size = 50
    font_file = None
    antialias = True
    font = pygame.font.Font(font_file, font_size)
    text_image = font.render("hello, pygame", antialias, pygame.Color("green"))
    return text_image


def create_player():
    player_images = [
        pygame.image.load("/home/yamaguchi/pygame/GDevelop-Examples/animation-speed-scale/p1_walk04.png").convert(),
        pygame.image.load("/home/yamaguchi/pygame/GDevelop-Examples/animation-speed-scale/p1_walk05.png").convert(),
        pygame.image.load("/home/yamaguchi/pygame/GDevelop-Examples/animation-speed-scale/p1_walk06.png").convert(),
        pygame.image.load("/home/yamaguchi/pygame/GDevelop-Examples/animation-speed-scale/p1_walk07.png").convert()

    ]
    return player_images

def draw(screen, player_image, text_image, mouse_pos):
    screen.fill(pygame.Color("black"))
    screen.blit(player_image, mouse_pos)
    mouse_x, mouse_y = mouse_pos
    text_offset_x = 100
    screen.blit(text_image, (mouse_x + text_offset_x, mouse_y))
    pygame.display.update()


def main():
    screen = init_screen()
    text_image = create_text()
    player_images = create_player()
    frame_index = 0

    while True:
        should_quit = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                should_quit = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    should_quit = True
                elif event.key == pygame.K_b:
                    pass
        if should_quit:
            break
        mouse_pos = pygame.mouse.get_pos()

        frame_index += 1
        animation_index = frame_index % len(player_images)
        draw(screen, player_images[animation_index], text_image, mouse_pos)

    pygame.quit()


if __name__ == "__main__":
    main()