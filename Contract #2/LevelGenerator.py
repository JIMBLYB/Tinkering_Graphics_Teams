import pygame
import LevelMaps as LM

cell_width = 5
cell_height = 5
cell_size = 32
cellChunk_size = 160

pygame.init()
map_display = pygame.display.set_mode((1080, 720))
map_display.fill(LM.background_colour)

map_show = True
while map_show:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            map_show = False

    for row in range(cell_height):
        for column in range(cell_width):
            map_display.blit(LM.textures[LM.tilemap_shrine[row][column]], (column * cell_size, row * cell_size))
    pygame.display.update()

pygame.quit()
