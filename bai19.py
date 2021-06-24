import numpy as np
import matplotlib.pyplot as plt
from skimage.io import imread, imshow
from skimage.color import rgb2gray, rgb2hsv
from skimage.morphology import area_opening
from skimage.exposure import histogram
from skimage.filters import threshold_otsu

img = imread('rose_gauss.jpg', 0)
imshow(img);
th_values = np.linspace(0, 1, 11)
fig, axis = plt.subplots(2, 5, figsize=(15,8))
img_gray = rgb2gray(img)
for th, ax in zip(th_values, axis.flatten()):
    
    img_binarized = img_gray < th
    ax.imshow(img_binarized)
    ax.set_title('$Threshold = %.2f$' % th)
freq, bins = histogram(img_gray)
plt.step(bins, freq*1.0/freq.sum())
plt.xlabel('Intensity value')
plt.ylabel('Fraction of pixels');

plt.show()

