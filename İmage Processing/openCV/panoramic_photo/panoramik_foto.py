import cv2 as cv
import numpy as np


sol = cv.imread("sol_foto.jpeg")
sag = cv.imread("sag_foto.jpeg")

boyut = (1024,768)

sol  = cv.resize(sol,boyut,interpolation=cv.INTER_AREA)
sag  = cv.resize(sag,boyut,interpolation=cv.INTER_AREA)
tam_hal = []

tam_hal.append(sol)
tam_hal.append(sag)

stich = cv.Stitcher.create()

ret,pano  = stich.stitch(tam_hal)

cv.imshow("panoramik_foto",pano)
cv.waitKey(0)

cv.destroyAllWindows()