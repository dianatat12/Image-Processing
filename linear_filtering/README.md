## Linear smoothing filters

>Smoothing filters are used to increase the uniformity of the pixels in a region. It decreases small variations, which can be caused by noise. Smoothing filters are used to decrease the noise in the image. 

>The most common type of noise is Gaussian noise. Usually for this type of noise the mean is considered to be 0.

>I converted the 'lena' image into grayscale and add Gaussian noise on it. The function used to create Gasussian noise is:

```python
N = np.random.normal(0,standard_deviation,(rows,columns))
N = np.random.normal(0, 100, (h,w))
```

