from skimage.io import imread, imsave
from skimage import img_as_float, img_as_ubyte
import numpy as np

img = imread('img.png')
img_f = img_as_float(img)

img_y = 0.2126 * img_f[:, :, 0] + 0.7152 * img_f[:, :, 1] + 0.0722 * img_f[:, :, 2]
img_u = -0.0999 * img_f[:, :, 0] - 0.3360 * img_f[:, :, 1] + 0.4360 * img_f[:, :, 2]
img_v = 0.6150 * img_f[:, :, 0] - 0.5586 * img_f[:, :, 1] - 0.0563 * img_f[:, :, 2]

img_sort_list = np.sort(img_y, axis=None)
k = round(img_sort_list.size*0.05)
x_min, x_max = img_sort_list[k], img_sort_list[-k - 1]

img_y = np.clip((img_y - x_min)/(x_max - x_min), 0, 1)

img_r = np.clip(img_y + 1.2803 * img_v, 0, 1)
img_g = np.clip(img_y - 0.2148 * img_u - 0.3805 * img_v, 0, 1)
img_b = np.clip(img_y + 2.1279 * img_u, 0, 1)

img_combined = img_as_ubyte(np.dstack((img_r, img_g, img_b)))

imsave('out_img.png', img_combined)
