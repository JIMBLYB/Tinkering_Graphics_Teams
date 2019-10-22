
# Includes all textures.
#brick = pygame.image.load('Stone.png')
#water = pygame.image.load('Water.png')
#well = pygame.image.load('Well.png')
#shrine = pygame.image.load('Shrine.png')

# Testing out colours instead of images to begin with.
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

# Includes a range of different tile maps that can be modularly put together to create a randomly generated level.
tilemap = [
    [red, blue, green],
]

#
# All of this should be fine if it was in the main script, I don't see why it isn't
#