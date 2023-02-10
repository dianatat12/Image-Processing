import numpy as np
from skimage import io,color,util
import matplotlib.pyplot as plt
import math

# Image loading
img_orig = io.imread('tst1.bmp')

# Grayscale conversion
img_gray = color.rgb2gray(img_orig)  #indexed image with float values - 1 value between [0,1] in each 

# what if we add noise to the image
# to change the intensity of the noise change the var argument.
img_noise = util.random_noise(img_gray, mean=0, var=(8/255)**2)

# We still want to scale the values to 0...255 for both of them
img_gray = (img_gray*255).astype(int)
img_noise = (img_noise*255).astype(int)

# View the image
plt.figure(),plt.imshow(img_gray,cmap='gray'), plt.colorbar()
plt.title("Grayscaled image")
plt.figure(),plt.imshow(img_noise,cmap='gray'), plt.colorbar()
plt.title("Noisy image")

# Compute the histogram for noisy image
hist,_ = np.histogram(img_noise,range(0,256))
# View the histogram
plt.figure(figsize=(10,10)),plt.plot(hist)
plt.title("Histrogram for noisy image")

# Decide the thresholds
Ta = 25
Tb = 75
Tc = 125
Td = 175

# Create a blank image
out = np.zeros(img_gray.shape)

# Separate between objects and background
# pixels with values lower than  𝑇𝑎  belong to the background and are 
# given the value 0 for this part, use numpy indexing to go faster
out[img_noise<Ta] = 0
# pixels between thresholds  𝑇𝑎  and  𝑇𝑏  belong to object "A" and are
# given the value 1, etc. for multiple conditions, use np.logical_and(X,Y)
out[np.logical_and(img_noise>=Ta, img_noise<Tb)] = 1
# samne for the next interval, Tb-Tc
out[np.logical_and(img_noise>=Tb, img_noise<Tc)] = 2
# last interval Tc-Td
out[np.logical_and(img_noise>=Tc, img_noise<Td)] = 3
# for last interval, >Td
out[img_noise>Td] = 4

# cmap = jet, not gray anymore !!
plt.figure(figsize=(10,10)),plt.imshow(out, cmap='jet', vmin=0, vmax=4), plt.colorbar()
plt.title("After segmentation")

dims = img_noise.shape

#initialize the output images, transforms will be applied to them
# DON'T WRITE img_filtered = img_noise !! always create copies
img_filtered_median = out.copy()
# another copy for the original one

#median filtering 3x3      
for i in range(1, dims[0]-1):
    for j in range(1, dims[1]-1):
        V = out[i-1:i+2, j-1:j+2]   #apply on this image
        V = np.sort(V, axis = None)
        img_filtered_median[i,j] = V[4]   #middle of 9 is position 4 (5th element) 
        
plt.figure(), plt.imshow(img_filtered_median, cmap='jet', vmin=0, vmax=4), plt.colorbar()
plt.title("median filter on out image")        
