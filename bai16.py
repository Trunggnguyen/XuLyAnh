import cv2
import numpy as np

img = cv2.imread('binary.jpg') #Đọc ảnh gốc nhị phân

kernel = np.array([[0, 1, 0], [1, 1, 1], [0, 1, 0]], dtype=np.uint8) #Khai báo phần tử cấu trúc

erosion_img = cv2.erode(img, kernel, iterations=1) #Co ảnh đầu vào

border_img = img - erosion_img #Trừ ảnh đầu vào cho ảnh đã co để được đường viền ảnh

cv2.imshow('Anh goc', img)
cv2.imshow('Anh duong vien', border_img)

cv2.waitKey()

cv2.destroyAllWindows()