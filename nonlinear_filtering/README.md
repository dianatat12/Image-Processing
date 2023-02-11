# Non-linear filters
    A non-linear filter is a filter that applies a mathematical operation to each pixel of an image that is not a linear combination
    of the original pixel values. Unlike linear filters, non-linear filters are not limited to simple operations such as scaling, 
    summing, and averaging. Instead, non-linear filters can apply more complex mathematical operations such as thresholding, 
    morphological operations, and edge detection.

    Examples of non-linear filters include median filters, which replace each pixel with the median value in its surrounding 
    neighborhood, and morphological filters, which use shapes to transform the image, such as dilation and erosion.

    The use of non-linear filters can help preserve important features in an image, such as edges, while reducing noise 
    and smoothing the image. Non-linear filters are commonly used in many image processing tasks, such as image denoising, 
    edge detection, and object recognition.
    
    Non-linear filter types correspond to:
    - increasing region uniformity : smoothing
    - increasing contrast across region borders : sharpening 
  
## Median filter
     A median filter replaces the intensity of each pixel in an image with the median intensity value of a set of 
     surrounding pixels. The set of surrounding pixels is called the neighborhood of the pixel, and the size of the 
     neighborhood is specified by the user.

    The median filter works by computing the median value of the intensities of the pixels in the neighborhood and 
    using that value to replace the intensity of the center pixel. This process is repeated for every pixel in the 
    image, resulting in a smoothed image. Median filter is not linear and it communtes with any monotonic function. 

    One of the main benefits of the median filter is its ability to effectively remove salt-and-pepper noise, which 
    is a type of random noise that consists of isolated pixels with high or low intensity values. The median filter
    can also be used to remove other types of noise, such as impulse noise, and to smooth images, as it preserves 
    edges and other important features of the image.
> ![median_filter](https://github.com/dianatat12/Image-Processing/blob/main/images/median_filter.jpg)
    
 ## Weighted rank-order filter
    The weighted rank-order filter works by multiplying the intensities of each pixel in the neighborhood by its weight,
    and then sorting the weighted intensities. The intensity value of the pixel with the specified weighted rank is used
    to replace the intensity of the center pixel. This process is repeated for every pixel in the image, resulting in a 
    filtered image.
    The weighted rank-order filter is a useful tool in image processing, as it provides a way to preserve important features 
    in the image while removing noise. By assigning different weights to different pixels in the neighborhood, the filter 
    can be adjusted to enhance specific features or remove specific types of noise, making it a versatile tool in many 
    image processing tasks.
 > ![weighted_rank](https://github.com/dianatat12/Image-Processing/blob/main/images/weighted_filter.jpg)
