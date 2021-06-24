import cv2 
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('test.jpg', cv2.IMREAD_GRAYSCALE) #Đọc ảnh gốc

#Hàm tìm ngưỡng Otsu
def OTSU(img_gray):  
    max_g = 0
    suitable_th = 0
    th_begin = 0
    th_end = 256
    
    for threshold in range(th_begin, th_end):
        bin_img = img_gray > threshold
        bin_img_inv = img_gray <= threshold
        fore_pix = np.sum(bin_img)
        back_pix = np.sum(bin_img_inv)
        if 0 == fore_pix:
            break
        if 0 == back_pix:
            continue
 
        w0 = float(fore_pix) / img_gray.size
        u0 = float(np.sum(img_gray * bin_img)) / fore_pix
        w1 = float(back_pix) / img_gray.size
        u1 = float(np.sum(img_gray * bin_img_inv)) / back_pix

        g = w0 * w1 * (u0 - u1) * (u0 - u1)
        if g > max_g:
            max_g = g
            suitable_th = threshold
 
    return suitable_th

otsu_threshold = OTSU(img) #Ngưỡng Otsu

#Phân ngưỡng bằng ngưỡng Otsu
ret, img1 = cv2.threshold(img, otsu_threshold, 255, cv2.THRESH_BINARY) 

#Hiển thị kết quả
cv2.imshow('Anh goc', img)
his1 = plt.hist(img.ravel(), 256)
plt.show()
cv2.imshow('Anh phan nguong otsu', img1)
his2 = plt.hist(img1.ravel(), 256)
plt.show()

cv2.waitKey()

cv2.destroyAllWindows()
