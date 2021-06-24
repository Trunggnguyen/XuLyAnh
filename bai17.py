import cv2
import numpy as np

img = cv2.imread('binaryfinger.jpg') #Đọc ảnh gốc

kernel = np.array([[0, 1, 0], [1, 1, 1], [0, 1, 0]], dtype=np.uint8) #Tạo phần tử cấu trúc 3x3

erosion_img = cv2.erode(img, kernel, iterations=1) #Thực hiện phép co ảnh
cv2.imshow('Buoc 1', erosion_img)

opening_img = cv2.dilate(erosion_img, kernel, iterations=1) #Thực hiện phép mở ảnh
cv2.imshow('Buoc 2', opening_img)
img1 = cv2.dilate(opening_img, kernel, iterations=1) #Thực hiện phép mở ảnh
cv2.imshow('Buoc 3', img1)
img2 = cv2.erode(img1, kernel, iterations=1) #Thực hiện phép đóng ảnh

cv2.imshow('Anh goc', img)
cv2.imshow('Anh ket qua', img2)

cv2.waitKey()

cv2.destroyAllWindows()




