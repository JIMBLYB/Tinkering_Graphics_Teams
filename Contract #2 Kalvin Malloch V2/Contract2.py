import pygame

map_width = 32
map_height = 16
cell_size = 32

##brick = pygame.image.load('Stone.png')
##water = pygame.image.load('Water.png')
##well = pygame.image.load('Well.png')
##shrine = pygame.image.load('Shrine.png')

testRed = (200, 0, 0)
testBlue = (0, 200, 0)
testGreen = (0, 0, 200)

red = 0
blue = 1
green = 2

testBlocks = {
    red: testRed,
    blue: testBlue,
    green: testGreen
}

tilemap = [
    [red, blue, green],
]

pygame.init()
map_display = pygame.display.set_mode ((map_width, map_height))

def map_running():
    map_show = True
    while map_show:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                map_show = False

        for row in range(map_height):
            for column in range(map_width):
                pygame.draw.rect(map_display, testBlocks[tilemap[row][column]], (column * cell_size, row * cell_size, cell_size, cell_size))
        pygame.display.update()

    pygame.quit()

map_running()