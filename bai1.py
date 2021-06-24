import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

# Load and blur image
img = cv.imread('rose_gauss.jpg')
blur = cv.blur(img,(5,5))

# Convert color from bgr (OpenCV default) to rgb
img_rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
blur_rgb = cv.cvtColor(blur, cv.COLOR_BGR2RGB)

# Display
plt.subplot(221),plt.imshow(img_rgb),plt.title('Anh ban dau')
plt.xticks([]), plt.yticks([])
plt.subplot(222),plt.imshow(blur_rgb),plt.title('Su dung bo loc Gauss')
plt.xticks([]), plt.yticks([])
plt.show()
