
#  Read the image 'lena.png'. Convert it to grayscale (note the resulting type of data). 
# Generate white, Gaussian noise, 0 mean and different standard deviations. 
# Add the noise to the image. Observe the effects.

from skimage import io,color
import matplotlib.pyplot as plt
import numpy as np

#read the image
img = io.imread('lena.png')

#grayscale conversion
img_gray = color.rgb2gray(img)

plt.figure(),plt.imshow(img_gray,cmap='gray'), plt.colorbar()
plt.title('Grayscale image')

#take the shape of the image in height and width
h, w = img_gray.shape

# function used to create Gaussian noise : N = np.random.normal(0,standard_deviation,(rows,columns))
N = np.random.normal(0, 100, (h,w))

# When applying color.rgb2gray(img) the output image is scaled in [0,1] so we need to scale it back to [0,255].
for i in range(h):
    for j in range(w):
        img_gray[i, j] = img_gray[i, j] * 255
        
#plot the new 255 values image
plt.figure(),plt.imshow(img_gray,cmap='gray'), plt.colorbar()

#add the noise to the matrix, as N is already a matrix, we just sum the matrixes up
img_gray = img_gray + N

#check if any value is higher than 255 or smaller than 0, if so, we will convert them to the maximum values
for i in range(h):
    for j in range(w):
        if img_gray[i, j] > 255:
            img_gray[i,j] = 255
        elif img_gray[i,j] < 0:
            img_gray[i,j] = 0
            
#show the noise applied image
plt.figure(),plt.imshow(img_gray,cmap='gray'), plt.colorbar()
plt.title('Noise image')