from skimage.io import imread, imsave

img = imread('img.png')
min_im, max_im = img.min(), img.max()
img = ((img - min_im) / (max_im - min_im) * 255).astype('uint8')

imsave('out_img.png', img)
