import cv2
import numpy as np

#Đọc ảnh gốc
img = cv2.imread('test.jpg')
cv2.imshow('Anh goc', img)
cv2.waitKey()

blur_img = cv2.GaussianBlur(img, ksize=(3,3), sigmaX=0) #Làm mờ ảnh bằng bộ lọc Gaussian 3x3
img1 = img - blur_img #Trừ ảnh gốc cho ảnh sau khi làm mờ để được ảnh chi tiết

k = 2 #Khai báo hệ số
unsharp_img = img + img1 * k #Cộng ảnh gốc với ảnh chi tiết nhân hệ số để được ảnh sắc nét 
cv2.imshow('Anh sac net', unsharp_img)
cv2.waitKey()

cv2.destroyAllWindows()

