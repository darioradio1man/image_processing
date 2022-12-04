import numpy as np
from skimage.io import imread

img = imread('img.png')

img_sort = np.sort(img.flatten())
k = int(np.round(img.size * 0.05))
x_min, x_max = img_sort[k], img_sort[-k - 1]
print(x_min, x_max)
