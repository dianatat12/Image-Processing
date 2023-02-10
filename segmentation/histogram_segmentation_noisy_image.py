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
img_noise = util.random_noise(img_gray, mean=0, var=(3/255)**2)

# We still want to scale the values to 0...255 for both of them
img_gray = (img_gray*255).astype(int)
img_noise = (img_noise*255).astype(int)

# View the image
plt.figure(),plt.imshow(img_gray,cmap='gray'), plt.colorbar()
plt.title("Grayscaled image")
plt.figure(),plt.imshow(img_noise,cmap='gray'), plt.colorbar()
plt.title("Noisy image")

# Compute the histogram
hist,_ = np.histogram(img_noise,range(0,256))
# View the histogram
plt.figure(figsize=(10,10)),plt.plot(hist)

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
out[img_gray<Ta] = 0
# pixels between thresholds  𝑇𝑎  and  𝑇𝑏  belong to object "A" and are
# given the value 1, etc. for multiple conditions, use np.logical_and(X,Y)
out[np.logical_and(img_gray>=Ta, img_gray<Tb)] = 1
# samne for the next interval, Tb-Tc
out[np.logical_and(img_gray>=Tb, img_gray<Tc)] = 2
# last interval Tc-Td
out[np.logical_and(img_gray>=Tc, img_gray<Td)] = 3
# for last interval, >Td
out[img_gray>Td] = 4

# cmap = jet, not gray anymore !!
plt.figure(figsize=(10,10)),plt.imshow(out,cmap='jet'), plt.colorbar()
plt.title("New image")
