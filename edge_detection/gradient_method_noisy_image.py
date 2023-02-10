import math
from skimage import io,color
import matplotlib.pyplot as plt
import numpy as np
from skimage import util

#Read an image and convert it to grayscale

#read the image
img_orig = io.imread('lena.png')
img_gray= color.rgb2gray(img_orig)#grayscale conversion

#Add Gaussian noise to the image
img_noise = util.random_noise(img_gray, mode='gaussian' , mean=0, var=0.02) #add gaussian noise
img_gray = (img_gray*255).astype(int) #convert the matrix from values from 0 to 1 to from 0 to 255, thus multiplying with 255
img_noise = (img_noise*255).astype(int)

plt.figure(),plt.imshow(img_gray,cmap='gray'), plt.colorbar() #plot the new 255 values image
plt.title("Grayscaled image")
plt.figure(),plt.imshow(img_noise,cmap='gray'), plt.colorbar()
plt.title("Noisy image")

l, c = img_gray.shape #take the shape of the image in lines and columns


def get_gradient (img):
    
    #make copies of the original image so it won't be affected
    img_x = img.copy()
    img_y = img.copy()
    img_grad = img.copy()
    
    #initialize the masks
    mask_x = np.array([[0,0,0], [-1,0,1], [0,0,0]])
    mask_y = np.array([[0,-1,0], [0,0,0], [0,1,0]])

    for i in range(1, l-1):
        for j in range(1, c-1):
            V = img[i-1:i+2, j-1:j+2]
            
            Vx = V * mask_x
            Vy = V * mask_y  
            
            img_x[i,j] = np.sum(Vx) #min value -255 ; max value 255
            img_y[i,j] = np.sum(Vy) #min value -255 ; max value 255  
            img_grad[i,j] = math.sqrt(img_x[i,j]*img_x[i,j] + (img_y[i,j]*img_y[i,j])) #min value 0 ; max value 255*1.41
   
    plt.figure(), plt.imshow(img_grad, cmap='gray', vmin=0, vmax=255*1.41), plt.colorbar() #horizontal and vertical contours combined
    
    
get_gradient(img_gray)
plt.title("Gradient method on grayscale image")
get_gradient(img_noise)
plt.title("Gradient method on noisy image")
