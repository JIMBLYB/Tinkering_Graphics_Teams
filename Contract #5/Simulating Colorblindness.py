import matplotlib
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from skimage import data
from skimage import exposure

# Converts image into a numpy array
img = mpimg.imread("pic.jpg")
gamma_corrected = exposure.adjust_gamma(img, 1)
img_plot = plt.imshow(gamma_corrected)
plt.show()



