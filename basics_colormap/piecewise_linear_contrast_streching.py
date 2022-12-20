
# Implement the piecewise linear contrast stretching by using the mathematical function on every pixel in the image. 

from skimage import io,color
import matplotlib.pyplot as plt

L=256 #usually is 256 because there are 256 grey levels

# the function that applies the transform for a pixel in the image
def new_val_current_pixel(a,b,T1,T2,u,L):#function defined in the theory
    
    ### the input parameters should be (a,b,T1,T2), current value of the pixel, total number of gray levels 
    ### the output should be the new value in the current pixel

    if (u<a):
        v=T1 * u/ a
    if (u>=a and u<=b):
        v= T1 + (T2-T1)/(b-a)*(u-a)
    if (u>b):
        v= T2 + (L-1-T2)/(L-1-b)*(u-b)
            
    ### the output should be the new value in the current pixel
    return v

# function that will apply the transform on all the image
def apply_linear_contrast(a,b,T1,T2,L,img):
    
    ### the input parameters should be (a,b,T1,T2), total number of gray levels, input image and image shape
    ### the output should be the enhanced image
    height, width = img.shape
    
    for i in range (height-1): #take the pixels from all the lines
        for j in range (width-1): #take the pixels from all the columns
            img[i,j] = new_val_current_pixel(a, b, T1, T2, img[i,j], L) #apply the function
    
    
# read the image
img_orig = io.imread('lena.png')
img_gray = color.rgb2gray(img_orig)
img2 = img_gray.copy()

# show the original image
plt.figure(),plt.imshow(img_gray, cmap='gray')

# process the image
apply_linear_contrast(140, 200, 70, 230, L, img_gray) #apply linear contrast with the parameters from the first case
apply_linear_contrast(20, 220, 70, 160, L, img2) #apply linear contrast with the parameters from the second case

# show the resulting image
plt.figure(),plt.imshow(img_gray, cmap='gray') #show the image with the contrast applied in the first case
plt.figure(),plt.imshow(img2, cmap='gray') #show the image with the contrast applied in the second case