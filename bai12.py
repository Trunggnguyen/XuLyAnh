import numpy as np
import random
import cv2

#Hàm tạo nhiễu cho ảnh
def sp_noise(image,prob):
    output = np.zeros(image.shape,np.uint8)
    thres = 1 - prob 
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            rdn = random.random()
            if rdn < prob:
                output[i][j] = 0
            elif rdn > thres:
                output[i][j] = 255
            else:
                output[i][j] = image[i][j]
    return output

#Đọc ảnh gốc
image = cv2.imread('test.jpg',cv2.IMREAD_GRAYSCALE)
cv2.imshow('Anh goc', image)
cv2.waitKey()

#Làm nhiễu ảnh gốc với các mức nhiễu khác nhau
noise_img1 = sp_noise(image,0.05)
noise_img2 = sp_noise(image,0.03)
noise_img3 = sp_noise(image,0.01)
cv2.waitKey()

noise_img = [noise_img1, noise_img2, noise_img3]

#Hiển thị các ảnh nhiễu
for i in range(len(noise_img)):
    cv2.imshow('Anh nhieu muc ' + str(i + 1), noise_img[i])
    cv2.waitKey()


#Lọc ảnh nhiễu dùng bộ lọc trung vị với 3 kích cỡ 3x3, 5x5, 7x7
for i in range(len(noise_img)):
    med_img1 = cv2.medianBlur(noise_img[i], 3)
    med_img2 = cv2.medianBlur(noise_img[i], 5)
    med_img3 = cv2.medianBlur(noise_img[i], 7)
    cv2.imshow('Anh nhieu muc ' + str(i + 1) +' voi bo loc trung vi 3x3', med_img1)
    cv2.imshow('Anh nhieu muc ' + str(i + 1) +' voi bo loc trung vi 5x5', med_img1)
    cv2.imshow('Anh nhieu muc ' + str(i + 1) +' voi bo loc trung vi 7x7', med_img1)
    cv2.waitKey()

cv2.destroyAllWindows()