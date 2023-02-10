#compas method

import math
from skimage import io,color
import matplotlib.pyplot as plt
import numpy as np
from skimage import util

#read the image
img_orig = io.imread('lena.png')

#create a new image that is the original rgb converted to gray
img = color.rgb2gray(img_orig)
img = util.random_noise(img, mode='gaussian' , mean=0, var=0.01) #add gaussian noise
img = (img*255).astype(int) #convert the matrix from values from 0 to 1 to from 0 to 255, thus multiplying with 255
plt.figure(),plt.imshow(img,cmap='gray'), plt.colorbar() #plot the new 255 values image

l, c = img.shape #take the shape of the image in lines and columns

def get_diagonals(img):
    l, c = img.shape
    
    mask_diag_1 = np.array([[0,0,0], [-1,0,1], [0,0,0]])
    mask_diag_2 = np.array([[0,-1,0],[0,0,0],[0,1,0]]) #vertical diag
    mask_diag_3 = np.array([[0,0,1], [0,0,0], [-1,0,0]]) #45 degrees
    mask_diag_4 = np.array([[1,0,0], [0,0,0], [0,0,-1]]) #135 degrees
    
    img_diag_1 = img.copy()
    img_diag_2 = img.copy()
    img_diag_3 = img.copy()
    img_diag_4 = img.copy()
    img_fgrad = img.copy()
    
    for i in range(1, l-1):
        for j in range(1, c- 1):
            V = img[i-1:i+2, j-1:j+2]
            
            V_diag_1 = V * mask_diag_1
            V_diag_2 = V * mask_diag_2 
            V_diag_3 = V * mask_diag_3
            V_diag_4 = V * mask_diag_4
            
            img_diag_1[i,j] = abs(np.sum(V_diag_1)) #min value -255 ; max value 255
            img_diag_2[i,j] = abs(np.sum(V_diag_2)) #min value -255 ; max value 255
            img_diag_3[i,j] = abs(np.sum(V_diag_3))
            img_diag_4[i,j] = abs(np.sum(V_diag_4))
            
            img_fgrad[i,j] = np.max([img_diag_1[i,j], img_diag_2[i,j],img_diag_3[i,j],img_diag_4[i,j]]) #min value 0 ; max value 255*1.41
        
    plt.figure(), plt.imshow(img_diag_1,cmap='gray', vmin=0 , vmax = 255), plt.colorbar() #vertical contour
    plt.title('Compas method on vertical contour')
    plt.figure(), plt.imshow(img_diag_2,cmap='gray',vmin= 0 , vmax = 255), plt.colorbar() #horizontal contour
    plt.title('Compas method on horizontal contour')
    plt.figure(), plt.imshow(img_diag_3,cmap='gray',vmin= 0, vmax = 255), plt.colorbar()
    plt.title('Compas method on 45 degrees')
              
get_diagonals(img)