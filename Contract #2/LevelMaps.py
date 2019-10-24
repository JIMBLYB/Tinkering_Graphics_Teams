import pygame
# Colour of the background which represents the sky.
background_colour = (178, 216, 230)

brick = 0
water = 1
well = 2
shrine = 3
air = 4
grass = 5
wood = 6
# Loads all images that are currently in the program folder.
textures = {
    brick: pygame.image.load('Stone.png'),
    water: pygame.image.load('Water.png'),
    well: pygame.image.load('Well.png'),
    air: pygame.image.load('Air.png'),
    shrine: pygame.image.load('Shrine.png'),
    grass: pygame.image.load('Grass.png'),
    wood: pygame.image.load('Wood.png')
}
# A variety of different tile maps that give the level random generation.
tilemap_normal = [
    [air, air, air, air, air],
    [air, air, air, air, air],
    [grass, grass, grass, grass, grass],
    [brick, brick, brick, brick, brick],
    [brick, brick, brick, brick, brick]
]

tilemap_pit = [
    [air, air, air, air, air],
    [air, air, air, air, air],
    [grass, air, air, air, grass],
    [brick, air, air, brick, brick],
    [brick, brick, air, brick, brick]
]

tilemap_solid = [
    [air, grass, grass, grass, air],
    [grass, brick, brick, brick, grass],
    [brick, brick, brick, brick, brick],
    [brick, brick, brick, brick, brick],
    [brick, brick, brick, brick, brick]
]

tilemap_shrine = [
    [air, air, shrine, air, air],
    [air, air, air, air, air],
    [grass, grass, grass, grass, grass],
    [brick, brick, brick, brick, brick],
    [brick, brick, brick, brick, brick]
]

tilemap_platform = [
    [air, air, air, air, air],
    [air, air, air, air, air],
    [wood, wood, wood, wood, wood],
    [air, air, air, air, air],
    [air, air, air, air, air]
]

tilemap_well = [
    [air, air, well, air, air],
    [air, air, air, air, air],
    [grass, grass, water, water, grass],
    [brick, brick, water, water, brick],
    [brick, brick, brick, brick, brick]
]
# Puts the tilemaps into another array so it can be randomised in the other script.
all_tilemaps = [tilemap_normal, tilemap_pit, tilemap_platform, tilemap_shrine, tilemap_solid, tilemap_well]
