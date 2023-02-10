import numpy as np
from skimage import io,color
import matplotlib.pyplot as plt

img_orig = io.imread('lena.png') #read the original image
img_gray = color.rgb2gray(img_orig)  #grayscale conversion
plt.figure(),plt.imshow(img_gray,cmap='gray', vmin=0, vmax=1), plt.colorbar() #plot the grayscale image
plt.title('Grayscale conversion')  
 
img_gray = (img_gray*255).astype(int) #convert the matrix from values from 0 to 1 to from 0 to 255, thus multiplying with 255

#make copies of the grayscale image so it won't be affected
img_filtered = img_gray.copy()
img_smoothed = img_gray.copy()
img_details = img_gray.copy() 
img_sharpened = img_gray.copy() 

mask_original = np.array([[0,0,0],[0,1,0],[0,0,0]])  #the mask of the original image
# mask_smoothed = np.array([[1,1,1],[1,1,1],[1,1,1]])/9 #a given mask
mask_details=np.array([[-1,-1,-1], [-1,8,-1], [-1,-1,-1]]) #the one given as a kernel in the exercise
mask_sharpened= mask_original + mask_details # original + details = sharpened

l,c = img_gray.shape #get the rows and the columns of the picture

for i in range(1, l-1):
    for j in range(1, c-1):
        V = img_filtered[i-1:i+2, j-1:j+2]
        
        V_details = V * mask_details
        V_sharpened = V * mask_sharpened
        
        img_details[i, j] = np.sum(V_details)
        img_sharpened[i,j] = np.sum(V_sharpened)
        
plt.figure(), plt.imshow(img_smoothed, cmap='gray', vmin=0, vmax=255), plt.colorbar()
plt.title('Image smoothed')        
plt.figure(), plt.imshow(img_details, cmap='gray', vmin=-255, vmax=255), plt.colorbar()
plt.title('Details of the image')
plt.figure(), plt.imshow(img_sharpened, cmap='gray', vmin=0, vmax=255), plt.colorbar()
plt.title('Image sharpened')