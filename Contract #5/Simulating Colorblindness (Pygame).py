import pygame
pygame.init()

running = True
main_window = pygame.display.set_mode((369, 193))
img = pygame.image.load("pic.jpg").convert()

# Initialises all the variables for the processed images
img_protanopia = pygame.image

# Non-colorblind value
NORMAL = [[100, 0, 0], [0, 100, 0], [0, 0, 100]]

# Red weakness
PROTANOPIA = [[56.667, 43.333, 0], [55.833, 44.167, 0], [0, 24.167, 75.833]]
# Red blind
PROTANOMALY = [[81.667, 18.333, 0], [33.333, 66.667, 0], [0, 12.5, 87.5]]

# Green weakness
DEUTERANOPIA = [[62.5, 37.5, 0], [70, 30, 0], [0, 14.167, 85.833]]
# Green blind
DEUTERANOMALY = [[80, 20, 0], [25.883, 74.167, 0], [0, 14.167, 85.833]]

# Blue weakness
TRITANOPIA = [[95, 5, 0], [0, 43.333, 56.667], [0, 47.5, 52.5]]
# Blue blind
TRITANOMALY = [[96.667, 3.333, 0],[0, 73.333, 26.667], [0, 18.333, 81.667]]

# Full Color weakness
ACHROMATOPSIA = [[29.9, 58.7, 11.4], [29.9, 58.7, 11.4], [29.9, 58.7, 11.4]]
# Full color blindness (monochrome)
ACHROMATANOMALY = [[61.8, 32,    6.2], [16.3, 77.5,  6.2], [16.3, 32.0, 51.6]]


# TODO
# Adjust colour values by appropriate matrix (PROTANOPIA)
def protanopia():
    for x in range(img.get_width()):
        for y in range(img.get_height()):
            pixel_input = img.get_at((x, y))

            # Gives the RGB values of the pixel their own variables for readability
            pixel_r = pixel_input[0]
            pixel_g = pixel_input[1]
            pixel_b = pixel_input[2]

            pixel_r = int((pixel_r * PROTANOPIA[0][0] / 100) +
                          (pixel_g * PROTANOPIA[0][1] / 100) +
                          (pixel_b * PROTANOPIA[0][2] / 100))

            pixel_g = int((pixel_r * PROTANOPIA[1][0] / 100) +
                          (pixel_g * PROTANOPIA[1][1] / 100) +
                          (pixel_b * PROTANOPIA[1][2] / 100))

            pixel_b = int((pixel_r * PROTANOPIA[2][0] / 100) +
                          (pixel_g * PROTANOPIA[2][1] / 100) +
                          (pixel_b * PROTANOPIA[2][2] / 100))

            img_protanopia.set_at((x, y), (pixel_r, pixel_g, pixel_b))



# TODO
# Adjust color values by appropriate matrix (PROTANOMALY)
def protanomaly():
    for x in range(img.get_width()):
        for y in range(img.get_height()):
            pixel_input = img.get_at((x, y))


# TODO
# Adjust color values by appropriate matrix (DEUTARANOPIA)
def deutaranopia():
    for x in range(img.get_width()):
        for y in range(img.get_height()):
            pixel_input = img.get_at((x, y))


# TODO
# Adjust color values by appropriate matrix (DEUTARANOMALY)
def deutaranomaly():
    for x in range(img.get_width()):
        for y in range(img.get_height()):
            pixel_input = img.get_at((x, y))


# TODO
# Adjust color values by appropriate matrix (TRITANOPIA)
def tritanopia():
    for x in range(img.get_width()):
        for y in range(img.get_height()):
            pixel_input = img.get_at((x, y))


# TODO
# Adjust color values by appropriate matrix (TRITANOMALY)
def tritanomaly():
    for x in range(img.get_width()):
        for y in range(img.get_height()):
            pixel_input = img.get_at((x, y))


# TODO
# Adjust color values by appropriate matrix (ACHROMATOPSIA)
def achromatopsia():
    for x in range(img.get_width()):
        for y in range(img.get_height()):
            pixel_input = img.get_at((x, y))


# TODO
# Adjust color values by appropriate matrix (ACHROMATANOMALY)
def achromatanomaly():
    for x in range(img.get_width()):
        for y in range(img.get_height()):
            pixel_input = img.get_at((x, y))


# TODO
# Run image through each colorblindness adjustment
# Save each return as a new image
def image_processing():
    protanopia()
    pygame.image.save(img_protanopia, "protanopia.jpg")
    protanomaly()
    pygame.image.save(img_protanomaly, "protanomaly.jpg")
    deutaranopia()
    pygame.image.save(img_deutaranopia, "deutaranopia.jpg")
    deutaranomaly()
    pygame.image.save(img_deutaranomaly, "deutaranomaly.jpg")
    tritanopia()
    pygame.image.save(img_tritanopia, "tritanopia.jpg")
    tritanomaly()
    pygame.image.save(img_tritanomaly, "tritanomaly.jpg")
    achromatopsia()
    pygame.image.save(img_achromatopsia, "achromatopsia.jpg")
    achromatanomaly()
    pygame.image.save(img_achromatanomaly, "achromatanomaly.jpg")


# Copies image onto display
main_window.blit(img, (0, 0))
image_processing()

# Basic loop for exiting program
# Also updates display every frame
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
    pygame.display.update()
