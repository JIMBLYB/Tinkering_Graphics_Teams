import pygame
pygame.init()

# Creating the window
window = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("EthanJones - Tile Generator")
clock = pygame.time.Clock()

Tiles = ("water", "snow", "soil", "sand", "rock")

# tile position and size
tile_x = 0
tile_y = 600
tile_width = 1280
tile_height = 150

# Colors for tile textures
black = 0,0,0
white = 255, 255, 255
Soil_color = 155, 118, 83
Snow_color = 255, 250, 250
Sand_color = 194, 178, 128
Water_color = 0, 119, 190
Rock_color = 58.4, 58, 54.5

# string for the input on console for which texture
tile = str(input("What texture would you like to generate: rock, snow, water, sand, soil: "))

# using a while checker for when the program is running it will
# go through each tile type and check if the input is the same
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            window.fill(black)

        if tile == "water":
            # drawing the actual tile on the screen
            pygame.draw.rect(window, Water_color, (tile_x, tile_y, tile_width, tile_height))
        elif tile == "snow":
            pygame.draw.rect(window, Snow_color, (tile_x, tile_y, tile_width, tile_height))
        elif tile == "soil":
            pygame.draw.rect(window, Soil_color, (tile_x, tile_y, tile_width, tile_height))
        elif tile == "sand":
            pygame.draw.rect(window, Sand_color, (tile_x, tile_y, tile_width, tile_height))
        elif tile == "rock":
            pygame.draw.rect(window, Rock_color, (tile_x, tile_y, tile_width, tile_height))
        else:
            # if the input is incorrect this will be printed in the console
            print("Please type one of the textures listed.")

    pygame.display.flip()

# end program
pygame.quit()
