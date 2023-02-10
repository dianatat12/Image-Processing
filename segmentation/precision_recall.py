#compute precision and recall

#make the test image and the noisy images
#test image that contains a square with a gray level of 100 on a uniform background with a gray level of 180
import numpy as np
import matplotlib.pyplot as plt
from skimage import io,color,util

plt.close('all')
Mask = np.zeros([200,200])
Mask = Mask + 180  #make the 180 gray level of the background
Mask[40:95,40:95] = 100  #make the 100 gray level of the swuare
plt.figure(), plt.imshow(Mask, cmap='gray', vmin=0, vmax=255), plt.colorbar(), plt.show()

def gaussianNoise(std_dev):
    img_noise = Mask.copy()
    N = np.random.normal(0,std_dev, [200,200])

    img_noise = Mask + N
    img_noise[img_noise<0] = 0
    img_noise[img_noise>255] = 255
    img_noise=np.floor(img_noise)

    return img_noise

img_noise_10 = gaussianNoise(10)
img_noise_30 = gaussianNoise(30)

plt.figure(), plt.imshow(img_noise_10, cmap='gray', vmin=0, vmax=255), plt.colorbar(), plt.show()
plt.figure(), plt.imshow(img_noise_30, cmap='gray', vmin=0, vmax=255), plt.colorbar(), plt.show()

# Compute the histogram for mask image
hist_mask,_ = np.histogram(Mask,range(0,256))
hist_noise_10,_ = np.histogram(img_noise_10,range(0,256))
hist_noise_30,_ = np.histogram(img_noise_30,range(0,256))

def make_histogram(hist,color):
    
    # Compute the histogram for mask image
    plt.figure(figsize=(5,5)) #create a 10x10 image
    plt.plot(hist,color=color) #plot the histogram
    
make_histogram(hist_mask,'b')
plt.title("Histrogram for mask image")
make_histogram(hist_noise_10,'r') #make the histogram for noise=10
plt.title("Histrogram for noise image with standard variation=10")
make_histogram(hist_noise_30,'c') #make the histogram for noise=30
plt.title("Histrogram for noise image with standard variation=30")

def segmentation_quality_noisy(Mask, Noisy):
    
    true_positive = 0 #set the true_positive contor to start from 0
    false_positive = 0 #set the false_positive contor to start from 0
    false_negative = 0 #set the false_negative contor to start from 0
    
    for i in range(0, len(Mask)):
        for j in range(0, len(Noisy)):
            if Mask[i][j] == Noisy[i][j] == 100: #if predicted positive = actual positive
                true_positive += 1 #increment the contor with 1
               
            if Noisy[i][j] == 100:  #if predicted positive = actual negative
                false_positive += 1 #increment the contor with 1
                
            elif Mask[i][j] == 180 : #if predicted negative = actual positive
                false_negative += 1 #increment the contor with 1
               
    return true_positive, false_positive, false_negative

def computeQuality(Mask,Noisy):
    
    true_positive,false_positive,false_negative= segmentation_quality_noisy(Mask,Noisy)
    
    print("True Positive =", true_positive)
    print("False Positive =", false_positive)
    print("False Negative =", false_negative)

    precision = true_positive / (true_positive + false_positive)
    recall = true_positive / (true_positive + false_negative)
    
    print("Precision =", precision)
    print("Recall=", recall)

computeQuality(Mask, img_noise_10)
print ('________________________________________________')
computeQuality(Mask, img_noise_30)
