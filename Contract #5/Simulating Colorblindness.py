import pygame
pygame.init()

running = True
main_window = pygame.display.set_mode((369, 193))
img = pygame.image.load("pic.jpg").convert()

# Initialises all the variables for the processed images with the unedited image
img_protanopia = img
img_protanomaly = img
img_deutaranopia = img
img_deutaranomaly = img
img_tritanopia = img
img_tritanomaly = img
img_achromatopsia = img
img_achromatanomaly = img

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

            # Adjusts the RGB values of each individual pixel to the RGB values of the correct impairment
            pixel_r = int((pixel_r * PROTANOPIA[0][0] / 100) +
                          (pixel_g * PROTANOPIA[0][1] / 100) +
                          (pixel_b * PROTANOPIA[0][2] / 100))

            pixel_g = int((pixel_r * PROTANOPIA[1][0] / 100) +
                          (pixel_g * PROTANOPIA[1][1] / 100) +
                          (pixel_b * PROTANOPIA[1][2] / 100))

            pixel_b = int((pixel_r * PROTANOPIA[2][0] / 100) +
                          (pixel_g * PROTANOPIA[2][1] / 100) +
                          (pixel_b * PROTANOPIA[2][2] / 100))

            # Adds the color-adjusted pixel to the output surface
            img_protanopia.set_at((x, y), (pixel_r, pixel_g, pixel_b))


# TODO
# Adjust color values by appropriate matrix (PROTANOMALY)
def protanomaly():
    for x in range(img.get_width()):
        for y in range(img.get_height()):
            pixel_input = img.get_at((x, y))

            # Gives the RGB values of the pixel their own variables for readability
            pixel_r = pixel_input[0]
            pixel_g = pixel_input[1]
            pixel_b = pixel_input[2]

            # Adjusts the RGB values of each individual pixel to the RGB values of the correct impairment
            pixel_r = int((pixel_r * PROTANOMALY[0][0] / 100) +
                          (pixel_g * PROTANOMALY[0][1] / 100) +
                          (pixel_b * PROTANOMALY[0][2] / 100))

            pixel_g = int((pixel_r * PROTANOMALY[1][0] / 100) +
                          (pixel_g * PROTANOMALY[1][1] / 100) +
                          (pixel_b * PROTANOMALY[1][2] / 100))

            pixel_b = int((pixel_r * PROTANOMALY[2][0] / 100) +
                          (pixel_g * PROTANOMALY[2][1] / 100) +
                          (pixel_b * PROTANOMALY[2][2] / 100))

            # Adds the color-adjusted pixel to the output surface
            img_protanomaly.set_at((x, y), (pixel_r, pixel_g, pixel_b))


# TODO
# Adjust color values by appropriate matrix (DEUTARANOPIA)
def deutaranopia():
    for x in range(img.get_width()):
        for y in range(img.get_height()):
            pixel_input = img.get_at((x, y))
            
            # Gives the RGB values of the pixel their own variables for readability
            pixel_r = pixel_input[0]
            pixel_g = pixel_input[1]
            pixel_b = pixel_input[2]

            # Adjusts the RGB values of each individual pixel to the RGB values of the correct impairment
            pixel_r = int((pixel_r * DEUTERANOPIA[0][0] / 100) +
                          (pixel_g * DEUTERANOPIA[0][1] / 100) +
                          (pixel_b * DEUTERANOPIA[0][2] / 100))

            pixel_g = int((pixel_r * DEUTERANOPIA[1][0] / 100) +
                          (pixel_g * DEUTERANOPIA[1][1] / 100) +
                          (pixel_b * DEUTERANOPIA[1][2] / 100))

            pixel_b = int((pixel_r * DEUTERANOPIA[2][0] / 100) +
                          (pixel_g * DEUTERANOPIA[2][1] / 100) +
                          (pixel_b * DEUTERANOPIA[2][2] / 100))

            # Adds the color-adjusted pixel to the output surface
            img_deutaranopia.set_at((x, y), (pixel_r, pixel_g, pixel_b))


# TODO
# Adjust color values by appropriate matrix (DEUTARANOMALY)
def deutaranomaly():
    for x in range(img.get_width()):
        for y in range(img.get_height()):
            pixel_input = img.get_at((x, y))

            # Gives the RGB values of the pixel their own variables for readability
            pixel_r = pixel_input[0]
            pixel_g = pixel_input[1]
            pixel_b = pixel_input[2]

            # Adjusts the RGB values of each individual pixel to the RGB values of the correct impairment
            pixel_r = int((pixel_r * DEUTERANOMALY[0][0] / 100) +
                          (pixel_g * DEUTERANOMALY[0][1] / 100) +
                          (pixel_b * DEUTERANOMALY[0][2] / 100))

            pixel_g = int((pixel_r * DEUTERANOMALY[1][0] / 100) +
                          (pixel_g * DEUTERANOMALY[1][1] / 100) +
                          (pixel_b * DEUTERANOMALY[1][2] / 100))

            pixel_b = int((pixel_r * DEUTERANOMALY[2][0] / 100) +
                          (pixel_g * DEUTERANOMALY[2][1] / 100) +
                          (pixel_b * DEUTERANOMALY[2][2] / 100))

            # Adds the color-adjusted pixel to the output surface
            img_deutaranomaly.set_at((x, y), (pixel_r, pixel_g, pixel_b))


# TODO
# Adjust color values by appropriate matrix (TRITANOPIA)
def tritanopia():
    for x in range(img.get_width()):
        for y in range(img.get_height()):
            pixel_input = img.get_at((x, y))

            # Gives the RGB values of the pixel their own variables for readability
            pixel_r = pixel_input[0]
            pixel_g = pixel_input[1]
            pixel_b = pixel_input[2]

            # Adjusts the RGB values of each individual pixel to the RGB values of the correct impairment
            pixel_r = int((pixel_r * TRITANOPIA[0][0] / 100) +
                          (pixel_g * TRITANOPIA[0][1] / 100) +
                          (pixel_b * TRITANOPIA[0][2] / 100))

            pixel_g = int((pixel_r * TRITANOPIA[1][0] / 100) +
                          (pixel_g * TRITANOPIA[1][1] / 100) +
                          (pixel_b * TRITANOPIA[1][2] / 100))

            pixel_b = int((pixel_r * TRITANOPIA[2][0] / 100) +
                          (pixel_g * TRITANOPIA[2][1] / 100) +
                          (pixel_b * TRITANOPIA[2][2] / 100))

            # Adds the color-adjusted pixel to the output surface
            img_tritanopia.set_at((x, y), (pixel_r, pixel_g, pixel_b))
            


# TODO
# Adjust color values by appropriate matrix (TRITANOMALY)
def tritanomaly():
    for x in range(img.get_width()):
        for y in range(img.get_height()):
            pixel_input = img.get_at((x, y))

            # Gives the RGB values of the pixel their own variables for readability
            pixel_r = pixel_input[0]
            pixel_g = pixel_input[1]
            pixel_b = pixel_input[2]

            # Adjusts the RGB values of each individual pixel to the RGB values of the correct impairment
            pixel_r = int((pixel_r * TRITANOMALY[0][0] / 100) +
                          (pixel_g * TRITANOMALY[0][1] / 100) +
                          (pixel_b * TRITANOMALY[0][2] / 100))

            pixel_g = int((pixel_r * TRITANOMALY[1][0] / 100) +
                          (pixel_g * TRITANOMALY[1][1] / 100) +
                          (pixel_b * TRITANOMALY[1][2] / 100))

            pixel_b = int((pixel_r * TRITANOMALY[2][0] / 100) +
                          (pixel_g * TRITANOMALY[2][1] / 100) +
                          (pixel_b * TRITANOMALY[2][2] / 100))

            # Adds the color-adjusted pixel to the output surface
            img_tritanomaly.set_at((x, y), (pixel_r, pixel_g, pixel_b))


# TODO
# Adjust color values by appropriate matrix (ACHROMATOPSIA)
def achromatopsia():
    for x in range(img.get_width()):
        for y in range(img.get_height()):
            pixel_input = img.get_at((x, y))

            # Gives the RGB values of the pixel their own variables for readability
            pixel_r = pixel_input[0]
            pixel_g = pixel_input[1]
            pixel_b = pixel_input[2]

            # Adjusts the RGB values of each individual pixel to the RGB values of the correct impairment
            pixel_r = int((pixel_r * ACHROMATOPSIA[0][0] / 100) +
                          (pixel_g * ACHROMATOPSIA[0][1] / 100) +
                          (pixel_b * ACHROMATOPSIA[0][2] / 100))

            pixel_g = int((pixel_r * ACHROMATOPSIA[1][0] / 100) +
                          (pixel_g * ACHROMATOPSIA[1][1] / 100) +
                          (pixel_b * ACHROMATOPSIA[1][2] / 100))

            pixel_b = int((pixel_r * ACHROMATOPSIA[2][0] / 100) +
                          (pixel_g * ACHROMATOPSIA[2][1] / 100) +
                          (pixel_b * ACHROMATOPSIA[2][2] / 100))

            # Adds the color-adjusted pixel to the output surface
            img_achromatopsia.set_at((x, y), (pixel_r, pixel_g, pixel_b))


# TODO
# Adjust color values by appropriate matrix (ACHROMATANOMALY)
def achromatanomaly():
    for x in range(img.get_width()):
        for y in range(img.get_height()):
            pixel_input = img.get_at((x, y))

            # Gives the RGB values of the pixel their own variables for readability
            pixel_r = pixel_input[0]
            pixel_g = pixel_input[1]
            pixel_b = pixel_input[2]

            # Adjusts the RGB values of each individual pixel to the RGB values of the correct impairment
            pixel_r = int((pixel_r * ACHROMATANOMALY[0][0] / 100) +
                          (pixel_g * ACHROMATANOMALY[0][1] / 100) +
                          (pixel_b * ACHROMATANOMALY[0][2] / 100))

            pixel_g = int((pixel_r * ACHROMATANOMALY[1][0] / 100) +
                          (pixel_g * ACHROMATANOMALY[1][1] / 100) +
                          (pixel_b * ACHROMATANOMALY[1][2] / 100))

            pixel_b = int((pixel_r * ACHROMATANOMALY[2][0] / 100) +
                          (pixel_g * ACHROMATANOMALY[2][1] / 100) +
                          (pixel_b * ACHROMATANOMALY[2][2] / 100))

            # Adds the color-adjusted pixel to the output surface
            img_achromatanomaly.set_at((x, y), (pixel_r, pixel_g, pixel_b))


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
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
