from skimage.io import imread, imshow, imsave
import numpy as np

image = imread('img.png')


def remove_the_borders(img):
    border = [0, 0, 0, 0]
    color = img[0, 0]
    left, top, right, bottom = 0, 0, 0, 0

    for i in reversed(range(img.shape[0])):
        for j in reversed(range(img.shape[1])):
            if not np.array_equal(img[i, j], color):
                right, bottom = i, j

    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            if not np.array_equal(img[i, j], color):
                left, top = img.shape[0] - 1 - i, img.shape[1] - 1 - j

    border = list(reversed([left, top, right, bottom]))
    for i in border:
        print(i, end=' ')


remove_the_borders(image)
