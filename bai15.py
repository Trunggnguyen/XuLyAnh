import cv2
import numpy as np

img = cv2.imread('binary.jpg') #Đọc ảnh gốc

kernel = np.array([[0, 1, 0], [1, 1, 1], [0, 1, 0]], dtype=np.uint8) #Tạo phần tử cấu trúc 3x3
  
erosion_img = cv2.erode(img, kernel, iterations=1) #Thực hiện phép co ảnh
dilation_img = cv2.dilate(img, kernel, iterations=1) #Thực hiện phép dãn ảnh

opening_img = cv2.dilate(erosion_img, kernel, iterations=1) #Thực hiện phép mở ảnh
closing_img = cv2.erode(dilation_img, kernel, iterations=1) #Thực hiện phép đóng ảnh

#Hiển thị ảnh gốc và các ảnh kết quả
cv2.imshow('Anh goc', img)
cv2.imshow('Ket qua phep co anh', erosion_img)
cv2.imshow('Ket qua phep gian anh', dilation_img)
cv2.imshow('Ket qua phep mo anh', opening_img)
cv2.imshow('Ket qua phep dong anh', closing_img)
  
cv2.waitKey()

cv2.destroyAllWindows()