import cv2 as cv
import numpy as np
import time

video = cv.VideoCapture(1)

ret, frame = video.read()

frame = cv.flip(frame, 1)

h, w, _ = frame.shape

x1, y1 = w - 100, 0
x2, y2 = w - 1, 200

last_finger_pos = None
last_time_stamp = None

while True:
    ret, frame = video.read()
    frame = cv.flip(frame, 1)

    h, w, _ = frame.shape

    hsv_frame = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    ycbcr_frame = cv.cvtColor(frame, cv.COLOR_BGR2YCrCb)

    hsv_low = np.array([9, 0, 0])
    hsv_high = np.array([13, 255, 255])
    hsv_mask = cv.inRange(hsv_frame, hsv_low, hsv_high)

    ycbcr_low = np.array([0, 44, 60])
    ycbcr_max = np.array([255, 150, 130])
    ycbcr_mask = cv.inRange(ycbcr_frame, ycbcr_low, ycbcr_max)

    combined = cv.bitwise_and(ycbcr_mask, hsv_mask)
    cv.imshow("combined", combined)

    sifir_olmayanlar = cv.findNonZero(combined)

    if sifir_olmayanlar is not None:
        for pt in sifir_olmayanlar:
            x, y = pt[0]
            cv.circle(frame, (x, y), 10, (180, 142, 25), -1)
            cv.imshow("daireli", frame)

            if x1 <= x < x2 and y1 <= y < y2:
                if last_finger_pos is None:
                    last_finger_pos = (x, y)
                    last_time_stamp = time.time()
                else:
                    current_time = time.time()
                    elapsed_time = current_time - last_time_stamp

                    if elapsed_time > 2:
                        x1 = x - 100
                        y1 = y - 100
                        x2 = x + 100
                        y2 = y + 100
                        last_finger_pos = None
                        last_time_stamp = None

                

                break
    cv.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
    cv.imshow("Webcam", frame)
    if cv.waitKey(1) & 0xFF == ord("q"):
        break

video.release()
cv.destroyAllWindows()
