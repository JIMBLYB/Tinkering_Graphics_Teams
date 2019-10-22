import pygame
import Contract2ModulesLibrary
#
# You can use "import (module) as (string)" to use a module with a custom string.
# For instance "import Contract2ModulesLibrary as C2ML" would let you use
# "C2ML.something" instead of "Contract2ModulesLibrary.something" to make things easier
#

# Change to Player input in future.
map_width = 32
map_height = 16
cell_size = 32

pygame.init()
map_display = pygame.display.set_mode((map_width, map_height))


# Looping the game running while drawing the map.
# Current error: IndexError - list index out of range.
#
# "def map_running():" isn't necessary, you can take it out completely along with "map_running()"
# Then un-indent everything that was in that function and it will have the same effect.
#
# I think that the error here is caused because you are searching the tilemap in Contract2ModulesLibrary
# for the row and the column values, this is because they are loops that essentially keep track
# of what row and column you are at so you are searching a list of 3 variables for indexes up to 32 in when you
# use column and 16 when you use row, hence the IndexError
#
def map_running():
    map_show = True
    while map_show:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                map_show = False

        for row in range(map_height):
            for column in range(map_width):
                #
                # There's a PEP8 violation here, just take out the "\" at the end of this line
                # To properly format the multi line code here you shouldn't use a backslash
                # because it's in brackets so it's an implied continuation just do a new line
                # after the comma at "map_display" and at the end of the "Contract2ModulesLibrary" parameter.
                #
                pygame.draw.rect(map_display, Contract2ModulesLibrary.testBlocks[Contract2ModulesLibrary.tilemap[row]\
                    [column]], (column * cell_size, row * cell_size, cell_size, cell_size))
        pygame.display.update()

    pygame.quit()


map_running()
