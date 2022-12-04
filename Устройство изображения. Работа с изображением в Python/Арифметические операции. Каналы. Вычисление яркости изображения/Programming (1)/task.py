from skimage.io import imread, imsave
from skimage import img_as_float
import numpy as np

img = imread('img.png')
img_f = img_as_float(img)
r, g, b = np.dsplit(img_f, 3)
image_combined = np.dstack((b, r, g))
imsave('out_img.png', image_combined)
