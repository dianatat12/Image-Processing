import numpy as np
import matplotlib.pyplot as plt

plt.close('all')

Mask = np.zeros([200,200])
Mask[:,80:150] = 1
Mask=Mask*255
plt.figure(), plt.imshow(Mask, cmap='gray'), plt.colorbar(), plt.show()

Segm = np.zeros([200,200])
Segm[:,100:180] = 1
Segm=Segm*255
plt.figure(), plt.imshow(Segm, cmap='gray'), plt.colorbar(), plt.show()

#make the histograms for both mask and segmented image
hist_mask,_ = np.histogram(Mask,range(0,256))
hist_segmented,_ = np.histogram(Segm,range(0,256))

def make_histogram(hist,color):
    
    # Compute the histogram for mask image
    plt.figure(figsize=(5,5)) #create a 10x10 image
    plt.plot(hist,color=color) #plot the histogram
    
make_histogram(hist_mask,'b')
plt.title("Histrogram for mask image")
make_histogram(hist_segmented,'r')
plt.title("Histrogram for segmented image")

#Visualize the true positives
plt.figure(figsize=(5,5)) #create a 10x10 image
plt.plot(hist_mask) #plot the histogram
plt.plot(hist_segmented,color='r')#plot the histogram
plt.title("True positives with blue")

#Visualize the false negatives
plt.figure(figsize=(5,5)) #create a 10x10 image
plt.plot(hist_mask,color='r') #plot the histogram
plt.plot(hist_segmented)#plot the histogram
plt.title("False negatives with red")

#Visualize the false positives
plt.figure(figsize=(5,5)) #create a 10x10 image
plt.plot(hist_mask,color='k',linewidth=3) #plot the histogram
plt.plot(hist_segmented)#plot the histogram
plt.title("False positives with black")

def segmentation_quality(Mask, Segmented):
    
    true_positive = 0 #set the true_positive contor to start from 0
    false_positive = 0 #set the false_positive contor to start from 0
    false_negative = 0 #set the false_negative contor to start from 0
    
    for i in range(0, len(Mask)):
        for j in range(0, len(Segmented)):
            if Mask[i][j] == 255 and Segmented[i][j] == 255: #if predicted positive = actual positive
                true_positive += 1 #increment the contor with 1
               
            if Mask[i][j] == 0 and Segmented[i][j] == 255:  #if predicted positive = actual negative
                false_positive += 1 #increment the contor with 1
                
            if Mask[i][j] == 255 and Segmented[i][j] == 0: #if predicted negative = actual positive
                false_negative += 1 #increment the contor with 1
               
    return true_positive, false_positive, false_negative

true_positive,false_positive,false_negative= segmentation_quality(Mask, Segm)

print("True Positive=", true_positive)
print("False Positive=", false_positive)
print("False Negative=", false_negative)

precision = true_positive / (true_positive + false_positive)
recall = true_positive / (true_positive + false_negative)

print("Precision=", precision)
print("Recall=", recall)