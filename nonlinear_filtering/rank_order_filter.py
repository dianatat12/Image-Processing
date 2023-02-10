import numpy as np
from skimage import io,color
import matplotlib.pyplot as plt
from skimage import util

# Image reading
img= io.imread('lena.png')

# Grayscale conversion
img_gray = color.rgb2gray(img)  #indexed image with float values - 1 value between [0,1] in each 

plt.figure(),plt.imshow(img_gray,cmap='gray', vmin=0, vmax=1), plt.colorbar()#vmin=o and vmax=1 because my original image is between 0 and 1. 
plt.title("grayscaled image")

dims = img.shape # get the shape of the image

img_noise = util.random_noise(img_gray,'s&p', amount=0.15) # apply salt and pepper filter with 0.15 amount
img_noise = (img_noise*255).astype(int) #if we want vmin=0 and vmax=255 multiply the image with 255

plt.figure(),plt.imshow(img_noise,cmap='gray', vmin=0, vmax=255), plt.colorbar()
plt.title("Salt and pepper noisy image")

def median_filter(img_noise, input_variable): #function of median filter
    #initialize the output images, transforms will be applied to them
    
    img_filtered = img_noise.copy() # make a copy of the noisy image so it won't be affected
    
    for i in range(int(input_variable/2), dims[0]-int(input_variable/2)):#writea general formula that applies for any neighbourhood
        for j in range(int(input_variable/2), dims[1]-int(input_variable/2)):
            V = img_noise[i-int(input_variable/2):i+int(input_variable/2)+1, j-int(input_variable/2):j+int(input_variable/2)+1]
            V = np.sort(V,axis=None)
            img_filtered[i,j] = V[input_variable] #take the middle of the array

    plt.figure(), plt.imshow(img_filtered, cmap='gray',vmin=0,vmax=255), plt.colorbar()
    plt.title('Median filter '+ str(input_variable) + 'x' + str(input_variable))

            
#Apply the maximum rank order filter on the original image
def max_rank_filter(img, size_input, output_rank):

    img_rank=img.copy()# make a copy of the orginal image so it won't be affected
    
    for i in range(int(size_input/2), dims[0]-int(size_input/2)):
        for j in range(int(size_input/2), dims[1]-int(size_input/2)):
            V = img[i-int(size_input/2):i+int(size_input/2)+1, j-int(size_input/2):j+int(size_input/2)+1]
            V = np.sort(V,axis=None)
            img_rank[i,j] = V[output_rank] 
            
    plt.figure(), plt.imshow(img_rank, cmap='gray',vmin=0, vmax=1), plt.colorbar() 
    plt.title('Max rank order filter ' + str(size_input) + 'x' + str(size_input)+ 'with rank ' + str(output_rank))

median_filter(img_noise, 3)
median_filter(img_noise, 5)
max_rank_filter(img_gray, 3, 0)
max_rank_filter(img_gray, 5, 0)
max_rank_filter(img_gray, 3, 8)
max_rank_filter(img_gray, 5, 24)