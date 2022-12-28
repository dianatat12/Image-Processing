import numpy as np
from skimage import io,color
import matplotlib.pyplot as plt
from skimage import util

# Image reading
img_orig = io.imread('lena.png')

# Grayscale conversion
img = color.rgb2gray(img_orig)  #indexed image with float values - 1 value between [0,1] in each 
plt.figure(),plt.imshow(img,cmap='gray', vmin=0, vmax=1), plt.colorbar()
plt.title("Grayscaled image")

dims = img.shape
img_noise = util.random_noise(img,'s&p', amount=0.15)
img_noise = (img_noise*255).astype(int) # We still want to scale the values to 0...255

plt.figure(),plt.imshow(img_noise,cmap='gray', vmin=0, vmax=255), plt.colorbar()
plt.title("Salt and pepper noisy image")

#initialize the output images, transforms will be applied to them
img_filtered = img_noise.copy() #copy the image so the original one won't be affected

#3x3 neighourhood
for i in range(1, dims[0]-1):
    for j in range(1, dims[1]-1):
        V = img_noise[i-1:i+2, j-1:j+2]
        V = np.sort(V,axis=None)
        img_filtered[i,j] = V[4] #take the middle of the array-in our case is 4
        
plt.figure(), plt.imshow(img_filtered, cmap='gray',vmin=0,vmax=255), plt.colorbar()
plt.title('Sorting on 3x3 neighbourhood')     
#we still have noise after doing this

img_filtered1 = img_noise.copy()
#make a 5x5 neigbourhood to get rid of the noise
for i in range(2, dims[0]-2):
    for j in range(2, dims[1]-2):
        V = img_noise[i-2:i+3, j-2:j+3]
        V = np.sort(V,axis=None)
        img_filtered1[i,j] = V[12] #take the middle of the array-in our case is 12
      
plt.figure(), plt.imshow(img_filtered1, cmap='gray',vmin=0,vmax=255), plt.colorbar()
plt.title('Sorting on 5x5 neighbourhood')

#make V[max]-V[min] for the original image for 3x3 neighbourhood
img3 = img.copy()
for i in range(1, dims[0]-1):
    for j in range(1, dims[1]-1):
        V = img[i-1:i+2, j-1:j+2]
        V = np.sort(V,axis=None)
        img3[i,j] = V[8]-V[0]
        
plt.figure(), plt.imshow(img3, cmap='gray',vmin=0, vmax=1), plt.colorbar()
plt.title('V[max]-V[min] on 3x3 neighbourhood')

#make V[max]-V[min] for the original image for 5x5 neighbourhood
img4 = img.copy()
for i in range(2, dims[0]-2):
    for j in range(2, dims[1]-2):
        V = img[i-2:i+3, j-2:j+3]
        V = np.sort(V,axis=None)
        img4[i,j] = V[24]-V[8]
        
plt.figure(), plt.imshow(img4, cmap='gray',vmin=0, vmax=1), plt.colorbar()
plt.title('V[max]-V[min] on 5x5 neighbourhood')

