# opencv numpy
import cv2 as cv
# 读取图片
img = cv.imread('1.jpg')
# h w c 456 367 3
# BGR(0,0,255)   RGB  GRAY
# BGR---> GRAY

# h w c   456 367 1
img = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
print(img.shape)
print(img)

cv.imshow("cv",img)
cv.waitKey(0)