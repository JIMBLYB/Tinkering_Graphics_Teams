import pygame

map_width = 800
map_height = 600
cell_width = 32
cell_height = 32

brick = pygame.image.load('Stone.jpg')
water = pygame.image.load('Water.jpg')

def map_running():
    map_show = True
    while map_show:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                map_show = False
    pygame.quit()

def map_start():
    pygame.init()
    map_display = pygame.display.set_mode ((map_width, map_height))
    map_display.fill((0, 0, 0))
    pygame.display.flip()

map_start()
map_running()