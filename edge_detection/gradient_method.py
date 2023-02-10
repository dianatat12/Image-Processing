
#gradient method

import math
from skimage import io,color
import matplotlib.pyplot as plt
import numpy as np

#read the image
img_orig = io.imread('lena.png')

#create a new image that is the original rgb converted to gray
img = color.rgb2gray(img_orig)

img = (img*255).astype(int) #convert the matrix from values from 0 to 1 to from 0 to 255, thus multiplying with 255
plt.figure(),plt.imshow(img,cmap='gray'), plt.colorbar() #plot the new 255 values image

l, c = img.shape #take the shape of the image in lines and columns

def get_gradient(img):
    
    mask_x = np.array([[0,0,0],[-1,0,1],[0,0,0]])
    mask_y = np.array([[0,-1,0],[0,0,0],[0,1,0]])
    img_fx = img.copy()
    img_fy = img.copy()
    img_fgrad= img.copy()
    
    for i in range(1, l-1):
        for j in range(1, c- 1):
            V = img[i-1:i+2, j-1:j+2]
            Vx = V * mask_x
            Vy = V * mask_y   
            img_fx[i,j] = np.sum(Vx) #min value -255 ; max value 255
            img_fy[i,j] = np.sum(Vy) #min value -255 ; max value 255
            img_fgrad[i,j] = math.sqrt(img_fx[i,j] * img_fx[i,j] + img_fy[i,j]* img_fy[i,j]) #min value 0 ; max value 255*1.41
        
    plt.figure(),plt.imshow(img_fx,cmap='gray', vmin=-255 , vmax = 255), plt.colorbar() #vertical contour
    plt.title('Vertical contour')
    plt.figure(),plt.imshow(img_fy,cmap='gray',vmin=-255 , vmax = 255), plt.colorbar() #horizontal contour
    plt.title('Horizontal contour')
    plt.figure(),plt.imshow(img_fgrad,cmap='gray',vmin=0, vmax=255*1.41), plt.colorbar() #combined contours
    plt.title('Combined contours')
    
get_gradient(img)