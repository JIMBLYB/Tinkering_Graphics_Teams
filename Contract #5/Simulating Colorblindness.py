import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from skimage import data, img_as_float
from skimage import exposure

img = data.moon()
gamma_corrected = exposure.adjust_gamma(img,  0, 1)
plt.imshow(img)

