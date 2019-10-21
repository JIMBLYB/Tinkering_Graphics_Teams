import pygame
from pygame.tests.test_utils import png

pygame.init()

main = pygame.display.set_mode((400, 200))

my_sprite = pygame.image.load('Platform.png').convert()

# colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
ORANGE = (255, 165, 0)


def entity_colour_change(surface=pygame.Surface((1, 1))):
    pixel = pygame.Color(0, 0, 0)
    for x in range(surface.get_width()):
        for y in range(surface.get_height()):
            pixel = surface.get_at((x, y))
            surface.set_at(
                (x, y),
                pygame.Color(int(pixel.r), int(pixel.g * 0.10), int(pixel.b))
            )


entity_colour_change(my_sprite)
pygame.image.save(my_sprite, 'main.png')

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    main.fill(WHITE)
    main.blit(my_sprite, (0, 0))
    pygame.display.update()

pygame.quit()
