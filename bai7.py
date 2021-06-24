import cv2
import numpy as np
import matplotlib.pyplot as plt

#Đọc và hiển thị ảnh và lược đồ xám của ảnh gốc
img = cv2.imread('test.jpg', cv2.IMREAD_GRAYSCALE)
cv2.imshow('Anh goc', img)
his1 = plt.hist(img.ravel(), 256)
plt.show()

#Thực hiện biến đổi log
c = 255 / np.log(1 + np.max(img))
log_img = c * (np.log(img + 1))
log_img = np.array(log_img, dtype=np.uint8)
cv2.imshow('Anh bien doi ham log', log_img)
his2 = plt.hist(log_img.ravel(), 256)
plt.show()

#Thực hiện biến đổi inverse log
inv_log_img = np.exp(img ** 1/c) - 1
inv_log_img = np.array(inv_log_img, dtype=np.uint8)
cv2.imshow('Anh bien doi ham inverse log', inv_log_img)
his3 = plt.hist(inv_log_img.ravel(), 256)
plt.show()

cv2.waitKey(0)

cv2.destroyAllWindows()
