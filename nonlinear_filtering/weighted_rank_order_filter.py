import numpy as np
from skimage import io,color
import matplotlib.pyplot as plt

#read the image
img = io.imread('lena.png')

#create a new image that is the original rgb converted to gray
img_gray = color.rgb2gray(img)
dims = img.shape# get the shape of the image

plt.figure(),plt.imshow(img_gray,cmap='gray'), plt.colorbar()

#convert the matrix from values from 0 to 1 to from 0 to 255, thu multiplying with 255
for i in range(dims[0]):
    for j in range(dims[1]):
        img_gray[i, j] = img_gray[i, j] * 255
        

#select an array weighted mask; this example was given in course
weighted_mask=np.array([1,2,1,2,3,2,1,2,1])
image_values= np.array([1,3,3,2,2,1,4,3,5])

print('The lenght of the mask is: ' + str(len(weighted_mask))) #print the lenght of the weighted mask
rank_values=np.array([])

#make the operation of multiplying the image_values with weighted_mask and display the elements of the image_values
#as many time as the weight is (example: 2*3 = 3 3 )
for i in range(len(weighted_mask)): #take a variable in range of the mask's length
    for j in range(weighted_mask[i]):
        rank_values=np.append(rank_values,image_values[i]).astype(int) #rank_values is the result of the operation
        #display it as an int
      
print('The extracted values are: '+ str(rank_values)) 
    
#sorting the rank values array    
print('The sorted extracted values are: ' + str(sorted(rank_values)))

median_value=rank_values[int(len(rank_values)/2)] #get the middle of the sorted extracted values
print('The median value of the ordered extracted values is: ' + str(median_value))

def get_median_value(V): #make a function that will do the operation of multiplying the image_values with weighted_mask
#as before, but this time applied to V; V is defined in max_rank_filter function
#we do this so the function will get a median value for each 3x3 neighbourhood in the picture
    
    mask=np.array([1,2,1,2,3,2,1,2,1]) #get our weighted mask
    rank_values=np.array([]) # make an empty array
    
    #for each value of the mask, 
    for i in range(len(mask)):
        for j in range(mask[i]):
            rank_values=np.append(rank_values, V[i])#merge the rank_values array with the V[i]
        
    rank_values=sorted(rank_values) # sort the ranked values 
    median_value=rank_values[int(len(rank_values)/2)]
    
    return int(median_value)

def max_rank_filter(img, size_input):#function that calculates the max rank filter for neighbourhood
    
    img_rank=img.copy()
    
    for i in range(int(size_input/2), dims[0]-int(size_input/2)):#general formula for a neighbourhood
        for j in range(int(size_input/2), dims[1]-int(size_input/2)):
            V = img_rank[i-int(size_input/2):i+int(size_input/2)+1, j-int(size_input/2):j+int(size_input/2)+1]
            V = V.flatten() #returns a copy of the array collapsed into one dimension
            img_rank[i, j] = get_median_value(V)
       
    plt.figure(), plt.imshow(img_rank, cmap='gray',vmin=0, vmax=255), plt.colorbar() 
    plt.title('Weighted rank order filter ' + str(size_input) + 'x' + str(size_input))
    

max_rank_filter(img_gray, 3)   