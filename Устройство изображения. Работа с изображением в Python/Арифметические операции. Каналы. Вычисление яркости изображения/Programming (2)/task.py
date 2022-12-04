from skimage.io import imread, imsave
from skimage import img_as_float, img_as_ubyte
import numpy as np

img = imread('img.png')
img_f = img_as_float(img)

y = img_as_ubyte(img_f[:, :, 0] * 0.2126 + img_f[:, :, 1] * 0.7152 + img_f[:, :, 2] * 0.0722)
imsave('out_img.png', y)
