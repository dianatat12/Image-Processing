#convert an image to grayscale

# Import skimage and matplotlib
from skimage import io,color
import matplotlib.pyplot as plt

# Image loading
img_orig = io.imread('lena.png')

# Data type of the original image
print('The original image type is:', img_orig.dtype)
print('The shape of the original image is:', img_orig.shape, '\n')

# Displaying the original image
plt.figure(), plt.imshow(img_orig)
plt.title("Original image of lena")

# Grayscale conversion
img = color.rgb2gray(img_orig)

# Data type of the grayscale image
print('The grayscale image type us:',img.dtype)
print('The shape of the grayscale image is:', img.shape)

# Displaying the grayscale image
plt.figure(),plt.imshow(img,cmap='gray',vmin=0,vmax=1), plt.colorbar()
plt.title("Grayscale conversion of lena")

print(img.max())
print(img.min())

