# The user needs to import pygame and then run the LevelGeneration script. They will be asked to give a value for
# the width and height of the level and then a level will generate.
import pygame
import LevelMaps as LM
import random
# Variables determining the size of the chunks that wil be randomised and also the space between each one.
cell_width = 5
cell_height = 5
cell_size = 32
current_dist_apart = 0
y_dist_apart = 0
# The size of the screen determines how big the level shall be.
SCREEN_X = int(input("Enter the width of the level."))
SCREEN_Y = int(input("Enter the height of the level."))
# Initialises pygame and sets the screen size that was determined by the player input.
pygame.init()
map_display = pygame.display.set_mode((SCREEN_X, SCREEN_Y))
map_display.fill(LM.background_colour)
map_show = True
# Keeps the window open and allows the player to close it.
while map_show:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            map_show = False
# Chooses a random tilemap and pastes an image every 32 pixels until it pastes 5 images. It then does the same 4 more
# times (depending on the cell height and width).
    random_tilemap = random.randrange(0, 6)
    if current_dist_apart <= SCREEN_X:
        for row in range(cell_height):
            for column in range(cell_width):
                map_display.blit(LM.textures[LM.all_tilemaps[random_tilemap][row][column]],
                                 ((column * cell_size) + current_dist_apart, (row * cell_size)+y_dist_apart))
        pygame.display.update()
        current_dist_apart += 160
    elif y_dist_apart <= SCREEN_Y:
        current_dist_apart = 0
        y_dist_apart += 320

pygame.quit()
