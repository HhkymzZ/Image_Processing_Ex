import cv2 as cv 
import numpy as np

img = cv.imread("rose.jpeg")

img_hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)


height, width, _ = img.shape

buldum = False

for y in range(height):
    for x in range(width):
        pixel_value = img[y, x]

        if pixel_value[2] > 45:
            print("buldum")
            cv.circle(img,(x,y),50,(255,255,0,25))
            buldum = True
            break  
    if buldum:
        break  


cv.imshow("deneme",img)

cv.waitKey(0)
cv.destroyAllWindows()