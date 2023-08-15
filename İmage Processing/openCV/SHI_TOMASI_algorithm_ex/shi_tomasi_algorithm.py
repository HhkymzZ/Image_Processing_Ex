import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread("satranc.png")
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

koseler = cv.goodFeaturesToTrack(gray,10,0.001,70)
koseler = np.int0(koseler)

for i in koseler:
    a,b = i.ravel()
    cv.circle(img,(a,b),5,(0,255,255),-1)
plt.imshow(img),plt.show()
