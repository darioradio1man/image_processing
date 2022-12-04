from skimage.io import imread, imsave

img = imread('img.png')
imsave('out_img.png', ~img)
