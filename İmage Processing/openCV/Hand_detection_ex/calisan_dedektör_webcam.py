import cv2 as cv
import numpy as np

video = cv.VideoCapture(1)

while 1:

    #her kare kameradan kaydedildi
    ret,frame = video.read()

    #her kare x eksenine göre tersi alındı
    frame = cv.flip(frame,1)

    #her kare BGR dan HSV formatına çevrildi
    frame = cv.cvtColor(frame,cv.COLOR_BGR2HSV)
    
    
    #alınması istenen hsv değer aralığından oluşan maske değerleri girildi
    lower = np.array([5, 100, 200])  
    upper = np.array([13, 141, 240]) 
    
    #maske oluşturuldu
    mask = cv.inRange(frame, lower, upper) 

    sifir_olmayanlar = cv.findNonZero(mask)

    #find zero 0 olan değerler için none değeri döndüğünden bunu filtrelemek için if e koşul koyduk

    if sifir_olmayanlar is not None:

        ## sıfır olmayan noktaları if ile almıştık şimdi pt ye atarak kuru gürültüyle uğraşmayacağız
        for pt in sifir_olmayanlar:

            #pt tek kanallı olduğu için sadece x ve y sini aldık yani sıfırdan farklı dönen ilk değere ulaşacağız
            x, y = pt[0]
            cv.circle(frame, (x, y), 50, (0, 0, 255), -1)
            break

    cv.imshow("son", frame)          

    if cv.waitKey(0) & 0xFF == ord("q"):
            break

video.release()
cv.destroyAllWindows()