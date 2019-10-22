import pygame
import Contract2ModulesLibrary

# Change to Player input in future.
map_width = 32
map_height = 16
cell_size = 32

pygame.init()
map_display = pygame.display.set_mode((map_width, map_height))

# Looping the game running while drawing the map.
# Current error: IndexError - list index out of range.
def map_running():
    map_show = True
    while map_show:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                map_show = False

        for row in range(map_height):
            for column in range(map_width):
                pygame.draw.rect(map_display, Contract2ModulesLibrary.testBlocks[Contract2ModulesLibrary.tilemap[row]\
                    [column]], (column * cell_size, row * cell_size, cell_size, cell_size))
        pygame.display.update()

    pygame.quit()


map_running()
