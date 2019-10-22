import pygame

running = True
img = pygame.image.load("pic.jpg").convert()
main_window = pygame.display.set_mode((369, 193))

# Non-colorblind value
NORMAL = [[100, 0, 0], [0, 100, 0], [0, 0, 100]]

# Red weakness
PROTANOPIA = [[81.667, 18.333, 0], [55.833, 44.167, 0], [0, 24.167, 75.833]]
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
# Multiply color values by appropriate matrix (PROTANOPIA)
def protanopia():
    for x in range(img.get_width()):
        for y in range(img.get_height()):
            pixel_input = img.get_at((x, y))


# TODO
# Multiply color values by appropriate matrix (PROTANOMALY)
def protanomaly():
    for x in range(img.get_width()):
        for y in range(img.get_height()):
            pixel_input = img.get_at((x, y))
            print(pixel_input)


# TODO
# Multiply color values by appropriate matrix (DEUTARANOPIA)
def deutaranopia():
    for x in range(img.get_width()):
        for y in range(img.get_height()):
            pixel_input = img.get_at((x, y))


# TODO
# Multiply color values by appropriate matrix (DEUTARANOMALY)
def deutaranomaly():
    for x in range(img.get_width()):
        for y in range(img.get_height()):
            pixel_input = img.get_at((x, y))


# TODO
# Multiply color values by appropriate matrix (TRITANOPIA)
def tritanopia():
    for x in range(img.get_width()):
        for y in range(img.get_height()):
            pixel_input = img.get_at((x, y))


# TODO
# Multiply color values by appropriate matrix (TRITANOMALY)
def tritanomaly():
    for x in range(img.get_width()):
        for y in range(img.get_height()):
            pixel_input = img.get_at((x, y))


# TODO
# Multiply color values by appropriate matrix (ACHROMATOPSIA)
def achromatopsia():
    for x in range(img.get_width()):
        for y in range(img.get_height()):
            pixel_input = img.get_at((x, y))


# TODO
# Multiply color values by appropriate matrix (ACHROMATANOMALY)
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
protanopia(img)


# Basic loop for exiting program
# Also updates display every frame
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
    pygame.display.update()