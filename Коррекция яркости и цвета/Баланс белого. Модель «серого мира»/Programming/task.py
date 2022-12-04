import numpy as np
from skimage.io import imread, imsave
from skimage import img_as_float

img = imread('img.png')
img = img_as_float(img)

r = img[:, :, 0]
g = img[:, :, 1]
b = img[:, :, 2]

avg_r = np.average(r)
avg_g = np.average(g)
avg_b = np.average(b)

gray = (avg_r + avg_g + avg_b) / 3

avg_r /= gray
avg_g /= gray
avg_b /= gray

r /= avg_r
g /= avg_g
b /= avg_b

img_new = np.dstack((r, g, b))
img_new = np.clip(img_new, 0, 1)
imsave('out_img.png', img_new)
