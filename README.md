# Image-Processing

I will share here some personal projects I have done in Image Processing, following a course in my university. 

## Some basic concepts

>When thinking about image processing, first thing that pops into my head is “what is an image?”. An image is a 3D array composed of rows, columns, and channels. 
>A color image contains the red, green, and blue channels which for each individual pixel. Each pixel is made up of a red, green, and blue subpixel that lights up at different intensities to create different colors. The specific color information that a pixel describes is some blend of three components of the color spectrum -- RGB.
>A simplified version of grayscale image which I will be using has rows and columns only, where red=green=blue. These images are treated as indexed images. An indexed image consists of an array of values, where each value points to a row in a colormap.

## Colormap
>The colormap is an array with 3 columns, representing the quantities of red, green, and blue which make up the color of a pixel. 

>I have done an examples of creating images and their corresponding colormaps 

- 128x128 image with colormap which pixels range from black to pure red
![black-red](https://github.com/dianatat12/Image-Processing/blob/main/images/colormap_black_to_red.jpg)

- 256x256 image with colormap which pixels range from black to pure red and then to magenta
![black-magenta](https://github.com/dianatat12/Image-Processing/blob/main/images/colormap_black_to_magenta.jpg)

- 256x256 image with colormap which pixels range from black to pure red and then to yellow
![black-yellow](https://github.com/dianatat12/Image-Processing/blob/main/images/colormap_black_to_yellow.jpg)

## Enhancement

>Enhancing means increasing the visibility of the elements from the image.

## Point operation

>A point operation is a method that maps the input pixels into the output pixels with an one-to-one relationship. Thus, for computing the new, enhanced value of the pixel, we apply a mathematical function to the old, initial pixel. The function considers only the initial value of the pixel.

## Piecewise linear contrast stretching

>The contrast is the difference in brightness (gray level intensity) between the pixels in a region of interest. The bigger the contrast, the better the visibility of the elements from the images. Piecewise linear contrast stretching is defined as:




