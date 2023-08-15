import numpy as np
import cv2 as cv

# resim okuma işlemleri
filename = 'satranc.png'
img = cv.imread(filename)

# resmi griye ardından gri halini float32 formatına çevirme işlemi

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
gray = np.float32(gray)


# köşeleri aldık
dst = cv.cornerHarris(gray,2,3,0.04)


dst = cv.dilate(dst,None)

cv.imshow('dsst',dst)
# Threshold for an optimal value, it may vary depending on the image.
img[dst>0.001*dst.max()]=[0,0,255]

cv.imshow('dst',img)
if cv.waitKey(0) & 0xff == 27:
 cv.destroyAllWindows()