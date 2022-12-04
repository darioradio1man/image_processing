import numpy as np
from skimage.io import imread, imsave

img = imread('img.png').astype('float')

img_sort = np.sort(img.flatten())
k = int(np.round(img.size * 0.05))
x_min, x_max = img_sort[k], img_sort[-k]

img = np.clip(255 * (img - x_min)/(x_max - x_min), 0, 255).astype('uint8')
imsave('out_img.png', img)
