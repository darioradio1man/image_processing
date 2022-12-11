from collections import Counter

from skimage.io import imread, imsave
import numpy as np

img = imread('img.png')
values, _ = np.histogram(img, bins=range(257))
cdf = [sum(values[i] for i in range(x + 1)) for x in range(256)]
cdfmin = min(x for x in cdf if x > 0)
imsave('out_img.png', np.vectorize(
    lambda x: (cdf[x] - cdfmin) / (img.size - 1) * 255)(img).round().astype('uint8'))




