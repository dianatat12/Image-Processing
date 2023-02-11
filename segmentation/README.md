# Segmentation
    Image segmentation is the process of dividing an image into multiple segments or regions, each of which corresponds to
    a different object or part of the image. The goal of segmentation is to simplify and/or change the representation of 
    an image into something that is more meaningful and easier to analyze.
    
    Segmentation can be contour oriented or region oriented.

## Segmentation errors
    We can have:
    - Under segmentation: decomposing the image into fewer parts than needed
    - Over segmentation: decomposing the image into more parts than needed
 
 ## Fault segmentation 
    Fault segmentation in image processing refers to the process of identifying and separating the regions of an image that 
    contain faults or defects. This is an important step in many industrial applications, such as quality control, where the 
    goal is to detect and isolate faulty parts or products.

## Histogram segmentation
    Histogram segmentation is a method of image segmentation in which an image is divided into multiple segments 
    or regions based on the distribution of its intensity values. This technique is based on the observation that
    different regions within an image typically have different histograms, or distributions of intensity values.

    To perform histogram segmentation, the image is first converted into a histogram, which represents the distribution 
    of intensity values in the image. Based on the shape of the histogram, the image is then divided into multiple segments
    or regions. These regions are defined based on the local minima and maxima in the histogram. The local minima typically 
    correspond to the boundaries between  different regions in the image, while the local maxima correspond to the modes,
    or most common intensity values, within each region.

    Once the image has been segmented, each segment can then be processed and analyzed separately, which is useful for various
    image processing tasks, such as object recognition, feature extraction, and image classification.
    
### Precision call
    Precision, in the context of image processing, is a metric used to evaluate the performance of a 
    segmentation algorithm. It is defined as the ratio of the number of true positive pixels 
    (pixels that are correctly classified as belonging to the target region) to the total number of
    positive pixels (true positive plus false positive pixels).

    A high precision value indicates that the algorithm has a low number of false positive pixels, meaning 
    that it is not misclassifying many background pixels as belonging to the target region. However, 
    a high precision value does not guarantee that all of the target pixels have been correctly classified.
    
    
## Segmentation quality
    Segmentation quality refers to how well an image segmentation algorithm has divided an image into meaningful 
    and homogeneous regions, or segments, that accurately represent the objects or regions of interest in the image. 
    The quality of an image segmentation is typically evaluated using metrics such as accuracy, completeness, consistency, 
    and robustness.

    Accuracy measures how well the segments match the ground truth or manual segmentation, while completeness measures
    how much of the object or region of interest is captured by the segment. Consistency refers to how similar the segments
    are within the same object or region of interest, while robustness measures how well the algorithm performs under different
    imaging conditions or noise levels.


