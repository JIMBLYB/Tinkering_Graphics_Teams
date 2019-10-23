import pygame
import Contract2ModulesLibrary as c2ml

# Change to Player input in future.
map_width = 16
map_height = 16
cell_size = 32

pygame.init()
map_display = pygame.display.set_mode((map_width, map_height))

map_show = True
while map_show:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            map_show = False

    for row in range(map_height):
        for column in range(map_width):
            pygame.draw.rect(map_display, c2ml.testBlocks[c2ml.tilemap[row][column]], (column * cell_size, row * cell_size, cell_size, cell_size))
    pygame.display.update()

pygame.quit()

