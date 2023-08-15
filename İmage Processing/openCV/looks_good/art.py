import cv2 as cv

arkaplan = cv.imread("arkaplan.jpeg",-1)
width = arkaplan.shape[1]
height = arkaplan.shape[0]
adam = cv.imread("adam_foto.jpeg")
ikinci_adam= cv.imread("ikinci_adam.jpeg")



dim = (width, height)

ikinci_adam_resized = cv.resize(ikinci_adam,dim,interpolation= cv.INTER_AREA)

resized = cv.resize(adam, dim, interpolation = cv.INTER_AREA)

toplam= cv.addWeighted(arkaplan,0.5,resized,0.5,-5)
toplam_yeni = cv.addWeighted(toplam,0.5,ikinci_adam_resized,0.5,13)

cv.imshow("bg",toplam_yeni)
cv.waitKey(0)
cv.destroyAllWindows()
cv.waitKey(0)

