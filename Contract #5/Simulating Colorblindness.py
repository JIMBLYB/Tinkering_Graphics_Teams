import matplotlib
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from skimage import data
from skimage import exposure

NEW_GAMMA = 1

# Converts image into an ndarray
img = mpimg.imread("pic.jpg")
print(img)

# Changes the gamma in the "img" ndarray
gamma_corrected = exposure.adjust_gamma(img, NEW_GAMMA)
img_plot = plt.imshow(img)
plt.show()



