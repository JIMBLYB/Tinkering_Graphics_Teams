import pygame
pygame.init()

main_window = pygame.display.set_mode((1120, 630))

DECREASE_RED_BY = 255


def decreased_red():
    for x in range(0, pic.get_width()):
        for y in range(0, pic.get_height()):
            colour_to_change = pic.get_at((x, y))
            if colour_to_change[0] < DECREASE_RED_BY:
                colour_to_change[0] = 0
            elif colour_to_change[0] >= DECREASE_RED_BY:
                colour_to_change[0] -= DECREASE_RED_BY
            pic.set_at((x, y), colour_to_change)


pic = pygame.image.load("pic.jpg").convert()
decreased_red()

main_window.fill((255, 255, 255))
main_window.blit(pic, (0, 0))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    pygame.display.update()