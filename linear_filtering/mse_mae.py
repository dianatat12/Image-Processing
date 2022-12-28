
import matplotlib.pyplot as plt
import numpy as np
from skimage import io,color

img = io.imread('lena.png')#read the image
img_gray = color.rgb2gray(img) #create a new image that is the original rgb converted to gray
img_gray= img_gray* 255
plt.figure(),plt.imshow(img_gray,cmap='gray'), plt.colorbar() #plot the gray image
plt.title('Grayscale image')

h, w = img_gray.shape #take the rows and the columns of the image 

# generate noise and add it to the image
N = np.random.normal(0, 100, (h,w))#the formula for Gaussian noise, 0 is the mean and 100 is standard deviation
img_noise = img_gray + N

#check if any value is higher than 255 or smaller than 0, if so, we will convert them to the maximum values
for i in range(h):
    for j in range(w):
        if img_noise[i, j] > 255:
            img_noise[i,j] = 255
        elif img_noise[i,j] < 0:
            img_noise[i,j] = 0
            
plt.figure(),plt.imshow(img_noise,cmap='gray'), plt.colorbar()#show the noise applied to the image
plt.title('Noise image')

img_filtered = img_noise.copy() #copy the noise image so it won't be affected
h1, w1 = img_noise.shape #take the rows and columns of the image

kernel_aritmetic_mean=np.ones([3,3])/9# initialize the kernel

def filt_artimetic_mean():
    
   for i in range(1, h1-1):
       for j in range(1, w1- 1):
           V = img_noise[i-1:i+2, j-1:j+2]
           V = V * kernel_aritmetic_mean
           img_filtered[i, j] = np.sum(V)  

   plt.figure(),plt.imshow(img_filtered,cmap='gray'), plt.colorbar()
   plt.title('Filtered image')

def MSE_MAE():
    
    r,c = img_filtered.shape #take the rows and columns of the image
    
    mse=0
    mae=0
    
    for i in range(r):
        for j in range(c):
            
            mse= np.sum(img_filtered[i,j] - img[i,j])**2
            mse= mse* 1/(r*c)
            
            mae= abs(np.sum(img_filtered[i,j] - img[i,j]))
            mae=mse* 1/(r*c)
            
    print('The MSE value is:' + str(mse))
    print('The MAE value is:' + str(mae))

filt_artimetic_mean()

MSE_MAE()


