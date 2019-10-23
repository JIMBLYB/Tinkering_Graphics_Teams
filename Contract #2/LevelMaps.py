import pygame

background_colour = (178, 216, 230)

brick = 0
water = 1
well = 2
shrine = 3
air = 4
grass = 5
wood = 6

textures = {
    brick: pygame.image.load('Stone.png'),
    water: pygame.image.load('Water.png'),
    well: pygame.image.load('Well.png'),
    air: pygame.image.load('Air.png'),
    shrine: pygame.image.load('Shrine.png'),
    grass: pygame.image.load('Grass.png'),
    wood: pygame.image.load('Wood.png')
}

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
    [brick, brick, brick, brick, brick],
    [brick, brick, brick, brick, brick],
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
    [brick, brick, water, water, brick]
]
