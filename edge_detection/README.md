# Edge detection
    Edge detection is a technique used to identify and locate the boundaries between regions with distinct visual properties in 
    an image.It is often used as a pre-processing step for further image analysis tasks such as image segmentation, 
    pattern recognition, and feature extraction. The goal of edge detection is to find the edges, or boundaries,
    between objects in an image by looking for sudden changes in intensity or color.
  
  There are several methods used in edge detection, like the Sobel operator and the Laplacian. 
  
 ## Sobel operator
    Sobel works by computing the gradient magnitude of an image, which measures how quickly the intensity of an image changes
    in a particular direction. It uses 3x3 kernels, for finding the gradient in the horizontal and vertical direction. 
    Starting from a basic kernel, other kernels are obtained by a circular shift of the kernel marnings around its center.
 
 ## Laplacian operator 
    Laplacian operator is a differential operator used in image processing and computer vision to detect edges in an image.
    It is used to find the second derivatives of an image, which represent the rate of change of the image intensity.
