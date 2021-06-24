import cv2
import numpy as np
import matplotlib.pyplot as plt

#Đọc và hiển thị ảnh và lược đồ xám của ảnh gốc
img = cv2.imread('test.jpg', cv2.IMREAD_GRAYSCALE)
cv2.imshow('Anh goc', img)
his1 = plt.hist(img.ravel(), 256)
plt.show()

#Thực hiện biến đổi n^th power
gamma = 2
power_img = np.array(255 * (img/255) ** gamma, dtype=np.uint8)
cv2.imshow('Anh bien doi ham mu (n^th power)', power_img)
his2 = plt.hist(power_img.ravel(), 256)
plt.show()

#Thực hiện biến đổi n^th root
gamma = 0.5
root_img = np.array(255 * (img/255) ** gamma, dtype=np.uint8)
cv2.imshow('Anh bien doi ham mu (n^th root)', root_img)
his3 = plt.hist(root_img.ravel(), 256)
plt.show()

cv2.waitKey()

cv2.destroyAllWindows()


