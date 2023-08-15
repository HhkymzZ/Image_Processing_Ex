import cv2 as cv
import numpy as np
import time


               
               
flag  = 1

video = cv.VideoCapture(1)


ret,frame = video.read()

   
frame = cv.flip(frame,1)

h,w,_= frame.shape

x1, y1 = w - 100, 0
x2, y2 = w - 1, 200

while 1:

    
    ret,frame = video.read()

   
    frame = cv.flip(frame,1)

    h,w,_= frame.shape
    

   
    hsv_frame = cv.cvtColor(frame,cv.COLOR_BGR2HSV)
    ycbcr_frame = cv.cvtColor(frame, cv.COLOR_BGR2YCrCb)


    hsv_low=np.array([9, 0, 0])
    hsv_high=np.array([13, 255, 255])

    hsv_mask = cv.inRange(hsv_frame,hsv_low,hsv_high)

   
    
    ycbcr_low = np.array([0, 44, 60])
    ycbcr_max = np.array([255, 150 , 130])

    ycbcr_mask = cv.inRange(ycbcr_frame, ycbcr_low, ycbcr_max)


    combined = cv.bitwise_and(ycbcr_mask,hsv_mask)

    cv.imshow("combined",combined)

    sifir_olmayanlar = cv.findNonZero(combined)

    if sifir_olmayanlar is not None:
        
        for pt in sifir_olmayanlar:
            x, y = pt[0]
            
            
            
            cv.circle(frame, (x, y), 10, (180, 142, 25), -1)
            cv.imshow("daireli",frame)
            
            if x1 <= x < x2 and y1 <= y < y2:
                if flag == 1: # flaga başta 1 değerini atadığımız için her türlü bu ife girecek
                    baslangic = time.time() # dikdörtgenin içine girdikren sonra zamanı tutmaya başladık
                    flag = 0 # tekrar ife girmemesi için flag ın değerini 0 olarak değiştirdik
                gecen_sure = time.time() - baslangic # gecen sureyi aldık
                

                if gecen_sure > 1.0: # sure 1 den buyukse olacakları yazdık
                    
                    cv.circle(frame, (x, y), 5, (180, 142, 25), -1)
                    
            else:
                 
                 flag = 1 # eğer daire dikdörtgenin içinde değilse her seferinde araması için flagı ı tekrar 1 yaptık    
                

            cv.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv.imshow("Webcam", frame)
                
                
                    
            break

    if cv.waitKey(1) & 0xFF == ord("q"):
            break

video.release()
cv.destroyAllWindows()