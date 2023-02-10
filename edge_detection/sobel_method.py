
#sobel method

import math
from skimage import io,color
import matplotlib.pyplot as plt
import numpy as np
from skimage import util

#read the image
img_orig = io.imread('lena.png')

#create a new image that is the original rgb converted to gray
img = color.rgb2gray(img_orig)
img = (img*255).astype(int) #convert the matrix from values from 0 to 1 to from 0 to 255, thus multiplying with 255
plt.figure(),plt.imshow(img,cmap='gray'), plt.colorbar() #plot the new 255 values image

l, c = img.shape #take the shape of the image in lines and columns

def get_sobel(img):
    
    mask_1 = np.array([[-1,0,1], [-2,0,2], [-1,0,1]]) #horizontal diag
    mask_2 = np.array([[-1,-2,-1],[0,0,0],[1,2,1]])   #vertical diag
    mask_3 = np.array([[0,1,2], [-1,0,1], [-2,-1,0]]) #45 degrees
    mask_4 = np.array([[2,1,0], [1,0,-1], [0,-1,-2]]) #135 degrees
    
    img_1 = img.copy()
    img_2 = img.copy()
    img_3 = img.copy()
    img_4 = img.copy()
    img_fgrad= img.copy()
    
    for i in range(1, l-1):
        for j in range(1, c- 1):
            V = img[i-1:i+2, j-1:j+2]
            
            V_1 = V * mask_1
            V_2 = V * mask_2
            V_3 = V * mask_3
            V_4=  V * mask_4
            
            img_1[i,j] = abs(np.sum(V_1)) #min value -255 ; max value 255
            img_2[i,j] = abs(np.sum(V_2)) #min value -255 ; max value 255
            img_3[i,j] = abs(np.sum(V_3))
            img_4[i,j] = abs(np.sum(V_4))
            
            img_fgrad[i,j] = np.max([img_1[i,j], img_2[i,j],img_3[i,j],img_4[i,j]]) #min value 0 ; max value 255*1.41
        
    plt.figure(),plt.imshow(img_1,cmap='gray', vmin=0 , vmax = 255), plt.colorbar() #vertical contour
    plt.title('Compas method on vertical contour')
    plt.figure(),plt.imshow(img_2,cmap='gray',vmin= 0 , vmax = 255), plt.colorbar() #horizontal contour
    plt.title('Compas method on horizontal contour')
    plt.figure(),plt.imshow(img_3,cmap='gray',vmin= 0, vmax = 255), plt.colorbar()
    plt.title('Compas method on 45 degrees contour')
    plt.figure(),plt.imshow(img_4,cmap='gray',vmin= 0 , vmax = 255), plt.colorbar()
    plt.title('Compas method on 135 degrees contour')
    plt.figure(),plt.imshow(img_fgrad,cmap='gray',vmin=0, vmax=255), plt.colorbar() #combined contours
    plt.title('Combined contours')
    
get_sobel(img)