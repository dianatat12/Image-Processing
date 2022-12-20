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

#convert the matrix from values from 0 to 1 to from 0 to 255, thu multiplying with 255
for i in range(h):
    for j in range(w):
        img_gray[i, j] = img_gray[i, j] * 255
        
#add the noise to the matrix, as N is already a matrix, we just sum the matrixes up
img_noise = img_gray + N

#check if any value is higher than 255 or smaller than 0, if so, we will convert them to the maximum values
for i in range(h):
    for j in range(w):
        if img_noise[i, j] > 255:
            img_noise[i,j] = 255
        elif img_noise[i,j] < 0:
            img_noise[i,j] = 0
            
#show the noise applied image
plt.figure(),plt.imshow(img_noise,cmap='gray'), plt.colorbar()
plt.title('Noise image')

#we make a copy of the original image so if we make change it won't affect the original
img_filtered1 = img_noise.copy()
img_filtered2 = img_noise.copy()
img_filtered3 = img_noise.copy()
h1, w1 = img_noise.shape

#take some array-type masks
mask1 =  np.array([[0, 0, 0], [-1, 0, 1], [0, 0, 0] ])
mask2= np.array([[[0, 1, 0], [0, 0, 0], [0, -1, 0] ]])
mask3= np.array([[[0, 1/4, 0], [1/4, -1, 1/4], [0, 1/4, 0]]])

for i in range(1, h1-1):
    for j in range(1, w1- 1):
        
        V = img_noise[i-1:i+2, j-1:j+2]
        
        V1 = V * mask1
        V2 = V * mask2
        V3 = V * mask3
        
        img_filtered1[i, j] = np.sum(V)
        img_filtered2[i, j] = np.sum(V)
        img_filtered3[i, j] = np.sum(V)

plt.figure(),plt.imshow(img_filtered1,cmap='gray'), plt.colorbar()
plt.title('Average filter with mask1')
plt.figure(),plt.imshow(img_filtered2,cmap='gray'), plt.colorbar()
plt.title('Average filter with mask2')
plt.figure(),plt.imshow(img_filtered3,cmap='gray'), plt.colorbar()
plt.title('Average filter with mask3')