import cv2
import numpy as np
import matplotlib as plt

#Đọc ảnh gốc
img = cv2.imread('test.jpg', cv2.IMREAD_GRAYSCALE)

#Ảnh phân ngưỡng với ngưỡng T = 50
ret, img1 = cv2.threshold(img, 50, 255, cv2.THRESH_BINARY)

#Ảnh phân ngưỡng với ngưỡng T = 75
ret, img2 = cv2.threshold(img, 75, 255, cv2.THRESH_BINARY)

#Ảnh phân ngưỡng với ngưỡng T = 100
ret, img3 = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY)

#Ảnh phân ngưỡng với ngưỡng T = 150
ret, img4 = cv2.threshold(img, 150, 255, cv2.THRESH_BINARY)

#Hiển thị các ảnh
cv2.imshow('Anh goc', img)
cv2.imshow('Anh co nguong 50', img1)
cv2.imshow('Anh co nguong 75', img2)
cv2.imshow('Anh co nguong 100', img3)
cv2.imshow('Anh co nguong 150', img4)

cv2.waitKey()

cv2.destroyAllWindows()

