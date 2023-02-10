import numpy as np
from skimage import io,color,util
import matplotlib.pyplot as plt
import math

# Image loading
img_orig = io.imread('tst2.bmp')

# Grayscale conversion
img_gray = color.rgb2gray(img_orig)  #indexed image with float values - 1 value between [0,1] in each 

# We still want to scale the values to 0...255 for both of them
img_gray = (img_gray*255).astype(int)

# View the image
plt.figure(),plt.imshow(img_gray,cmap='gray'), plt.colorbar()
plt.title("Grayscaled image")

# Compute the histogram
hist,_ = np.histogram(img_gray,range(0,256))
# View the histogram
plt.figure(figsize=(10,10)),plt.plot(hist)
plt.title("Histogram")

# Decide the thresholds
Ta = 25
Tb = 125
Tc = 175

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
# last interval, >Tc
out[img_gray>Tc] = 3

# cmap = jet, not gray anymore !!
plt.figure(figsize=(10,10)),plt.imshow(out,cmap='jet'), plt.colorbar()
plt.title("New image image")