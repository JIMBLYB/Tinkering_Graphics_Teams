import matplotlib
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from skimage import data
from skimage import exposure

NEW_GAMMA = 1

# Converts image into an ndarray to allow matplotlib methods
img = mpimg.imread("pic.jpg")
print(img)
colour_value = img[[0]]

# Only needed on pictures taken with a camera
# Changes the gamma in the "img" ndarray
gamma_corrected = exposure.adjust_gamma(img, NEW_GAMMA)

# Shows the image as a plot
img_plot = plt.imshow(gamma_corrected)
plt.show()

# TODO
# Lower values



'''
Matrix values for various cases of colorblindness


Normal:    
    R:[100,      0,     0],
    G:  [0,    100,      0],
    B:  [0,      0, 100],
Protanopia:
    R:[56.667, 43.333,  0],
    G:[55.833, 44.167,  0],
    B: [0,     24.167, 75.833],
Protanomaly:
    R:[81.667, 18.333,  0],
    G:[33.333, 66.667,  0],
    B: [0,     12.5,   87.5],
Deuteranopia:
    R:[62.5, 37.5,  0],
    G:[70,   30,    0],
    B: [0,   30,   70],
Deuteranomaly:
    R:[80,     20,      0],
    G:[25.833, 74.167,  0],
    B: [0,     14.167, 85.833],
Tritanopia:
    R:[95,  5,      0],
    G: [0, 43.333, 56.667],
    B: [0, 47.5,   52.5],
Tritanomaly:
    R:[96.667, 3.333,   0],
    G: [0,     73.333, 26.667],
    B: [0,     18.333, 81.667],
Achromatopsia:
    R:[29.9, 58.7, 11.4],
    G:[29.9, 58.7, 11.4],
    B:[29.9, 58.7, 11.4],
Achromatomaly:
    R:[61.8, 32,    6.2],
    G:[16.3, 77.5,  6.2],
    B:[16.3, 32.0, 51.6]
};
'''
