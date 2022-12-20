# Neighbourhood operations

The neighborhood is a window (opening) within an opaque material placed in front of the image; from the image it can be seen only the part corresponding to the current position of the window.
Neighborhood operations are image operations when each pixel in an output image is determined by the corresponding input pixel and pixels in one of its neighborhoods.

>Let f (l,c) be the initial input image, g (l, c) be the output, processed image and T a transform (an operation) on f, defined for a neighbourhood of a pixel at position (l, c). The new value of any pixel from the output image is obtained by combining the values of the pixels from the initial image, placed around the processed pixel (in the neighbourhood of the processed pixel). The origin of the filterring window is moved from pixel to pixel within the image until all the pixels are processed. The transform T is a function that combines the values extracted from the input image. T is applied at each location (l, c) in order to obtain the result g (l, c), in that particular location. 

> ![neighbourhood_operations](https://github.com/dianatat12/Image-Processing/blob/main/images/neighbourhood_operations.jpg)
>Neighbourhood operation on a 3x3 neighbourhood.

 How to avoid border effects of a neighborhood?
- Ignore the lines/columns which are corresponding to problematic locations
- Extending the image by sufficient lines/ columns

## Linear filtering(Convolution)

Linearity means that the superposition principle holds.
What is the superposition principle?
Given a transform T, applied to some elements f and g. T is linear if, for any constant scalars α and β:

T(αf + βg) = αT(f) + βT(g)

In our case, f and g are images having the same size, α and β and real scalars and T is the neighborhood transform. 

>Any linear filter is defined as:
> - Use neighborhood, V
> - Weights associated to points within the neighborhood, w_mn

Linear filtering is the filtering method in which linear combinations of the nearby input pixels to determine the value of the output pixel. In order to achieve it, we can use convolution. Gaussian filtering or mean/average filters are two examples. Mathematically, linear filtering can be expressed as:

![linear_filtering](https://github.com/dianatat12/Image-Processing/blob/main/images/convolution_formula.jpg)

- where w_mn are weights. These weights are constant scalars associated with each position in the filtering window.

>For each image pixel, located at (l,c):
> - The neighborhood V is placed with the origin in the current pixel
> - Extract the values of pixels within the neighborhood
> - According to T, extracted pixel values are combined
> - The new values are stored in the output location at location (l,c)
> - Go to next location (next pixel)

![convolution](https://github.com/dianatat12/Image-Processing/blob/main/images/convolution.jpg)
The mathematical operation is always applied for each neighbourhood and a new value is obtained. This new value depends on all the pixels in the neighbourhood.
![sliding](https://github.com/dianatat12/Image-Processing/blob/main/images/sliding_window.png)
The sliding window process

## Linear smoothing filters

Snoothing means increasing the uniformity within regions.

Smoothing filters are used to increase the uniformity of the pixels in a region. It decreases small variations, which can be caused by noise. Smoothing filters are used to decrease the noise in the image. 

The most common type of noise is Gaussian noise. Usually for this type of noise the mean is considered to be 0.

>I converted the 'lena' image into grayscale and add Gaussian noise on it. The function used to create Gasussian noise is:

```python
# N = np.random.normal(0,standard_deviation,(rows,columns))
N = np.random.normal(0, 100, (h,w))
```

