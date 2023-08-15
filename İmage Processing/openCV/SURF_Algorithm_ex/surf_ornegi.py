import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

bergen_tam = cv.imread("bergen.jpeg",cv.IMREAD_GRAYSCALE)
bergen_yarim = cv.imread("güllü.jpeg",cv.IMREAD_GRAYSCALE)

orb = cv.ORB_create()

kp1, des1 = orb.detectAndCompute(bergen_tam,None)
kp2, des2 = orb.detectAndCompute(bergen_yarim,None)

bf = cv.BFMatcher(cv.NORM_HAMMING, crossCheck=True)

matches = bf.match(des1,des2)


img3 =cv.drawMatches(bergen_tam,kp1,bergen_yarim,kp2,matches[:50],None,flags=cv.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
plt.imshow(img3),plt.show()
