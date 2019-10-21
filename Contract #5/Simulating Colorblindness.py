import pygame
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from skimage import data, img_as_float
from skimage import exposure

main_window = pygame.display.set_mode((738, 193))
pic = pygame.image.load("pic.jpg").convert()
main_window.blit(pic, (0, 0))

img = data.moon()
gamma_corrected = exposure.adjust_gamma(img,  0, 1)
main_window.blit(pic, (369, 0))
