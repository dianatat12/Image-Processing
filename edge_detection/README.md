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
    
> ![sobel](https://github.com/dianatat12/Image-Processing/blob/main/images/sobel.jpg)
>Neighbourhood operation on a 3x3 neighbourhood.
> ![sobel_example](https://github.com/dianatat12/Image-Processing/blob/main/images/sobel_example.jpg)
>Neighbourhood operation on a 3x3 neighbourhood.
 
 ## Laplacian operator 
    Laplacian operator is a differential operator used in image processing and computer vision to detect edges in an image.
    It is used to find the second derivatives of an image, which represent the rate of change of the image intensity.

## Gradient method
    Gradient techniques are methods that are used to find the intensity changes (edges) in an image. 
    They work by computing the gradient or the rate of change of intensity values in the image. 
    The gradient is then used to identify areas in the image where there is a rapid change in 
    intensity values, which correspond to edges in the image.
    
### How to implement it?
    Compute vertical and horizontal derivative for each pixel and then compute the maximal variation for each pixel.
    If the maximal variation for a pixel is stronger enough, that pixel is a contour pixel.
    
    
## Compass operator
    Compass operator enhances the gradient information in an image to produce a better representation of the edges.
    The basic idea behind the compass operator is to combine gradient information from different directions in order 
    to get a more robust representation of the edges.
        
    It looks at the differences on vertical (pixel above - pixel below), on horizontal (pixel to the left-
    pixel to the right) and the 2 diagonals. It makes 4 absolute differences or 8 normal differences. 
    We consider as being a contour where we have the biggest difference. 
    The magnitude is the intensity of the contour.
