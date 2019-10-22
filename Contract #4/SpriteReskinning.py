import pygame
from pygame.tests.test_utils import png

pygame.init()

# This will create the display that is the same size as my sprite i'm editing.
main = pygame.display.set_mode((400, 200))

# This surface is the one that actually loads th image.
my_sprite = pygame.image.load('Platform.png').convert()

# colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
ORANGE = (255, 165, 0)


# This function will get the x and y pixels and then set them to a different colour.
def entity_colour_change(surface=pygame.Surface((1, 1))):
    pixel = pygame.Color(0, 0, 0)
    for x in range(surface.get_width()):
        for y in range(surface.get_height()):
            pixel = surface.get_at((x, y))
            surface.set_at(
                (x, y),
                pygame.Color(int(pixel.r), int(pixel.g * 0.10), int(pixel.b))
            )


# I actually call the function here and put in the sprite surface.
entity_colour_change(my_sprite)
# Next i save the new sprite as a png to the project folder
pygame.image.save(my_sprite, 'main.png')

# This simple game loop will be checking for if the player tries to quit the game and will close the app.
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    main.fill(WHITE)
    # Overlays the new sprite over the main background surface.
    main.blit(my_sprite, (0, 0))
    # Now it will update the display.
    pygame.display.update()

pygame.quit()
