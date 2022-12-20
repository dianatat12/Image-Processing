#Make a 128x128 pixel image its corresponding colormap with colours which range from black to pure red

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

# How to create an array filled with zeros
img = np.zeros([128,128])
colormap = np.zeros([128,3])

# Create the image here
for i in range (128):
  img[:,i]=i
  
# Create the colormap here

for i in range(128):
  colormap[i,0]=i/127

# Display the image
colormap=mpl.colors.ListedColormap(colormap)
plt.figure(),plt.imshow(img,cmap=colormap),plt.colorbar()
plt.title("Colormap with range from black to pure red")

#Make a 256 x 256 pixel image and its corresponding colormap with colours which range from black to pure red and then to magenta (red + blue)
#Make a 256 x 256 pixel image and its corresponding colormap with colours which range from black to pure red and then to yellow (red + green)

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

img_magenta=np.zeros([256,256]) #create the empty array of the image
img_yellow=np.zeros([256,256]) 
img_blue=np.zeros([256,256])

colormap_magenta=np.zeros([256,3]) #create the empty array of the colormap
colormap_yellow=np.zeros([256,3])

# Create the image
for i in range (256):
    
    img_magenta[:,i]=i
    img_yellow[:,i]=i
    
    if i<=128:
        colormap_magenta[i,0]=i/127 #increase the values for red color
        colormap_yellow[i,0]=i/127
        
        colormap_magenta[i,2]=0 #keep the blue 0
        colormap_yellow[i,1]=0 #keep the green 0
        
    if i>=128 and i<=256: #took this range because i want to increase the blue after getting #the gradient from black to red
                        
        colormap_magenta[i,0]=1 #from the position 128 when we have pure red we maintain the value 1 so we can add and together they will make magenta
        colormap_magenta[i,2]=(i-127)/128 #increase the blue from 0 to 1 and with the already existing red it will create magenta
                      
        colormap_yellow[i,0]=1 
        colormap_yellow[i,1]=(i-127)/128 #increase the green from 0 to 1 and with the already existing red it will create yellow  

# Create the colormap 
colormap_magenta=mpl.colors.ListedColormap(colormap_magenta)
colormap_yellow=mpl.colors.ListedColormap(colormap_yellow)
   
# Display the images
plt.figure(),plt.imshow(img_magenta,cmap=colormap_magenta),plt.colorbar() 
plt.title("Colormap with range from black to magenta")

plt.figure(),plt.imshow(img_yellow,cmap=colormap_yellow),plt.colorbar() 
plt.title("Colormap with range from black to yellow")






