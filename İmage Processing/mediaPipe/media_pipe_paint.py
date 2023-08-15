import cv2 as cv
import mediapipe as mp

flag = 1
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands

cap = cv.VideoCapture(1)
liste=[]

with mp_hands.Hands(
    model_complexity=0,
    min_tracking_confidence=0.5,
    min_detection_confidence=0.5,
    max_num_hands=1,
) as hands:
    while True:
        flag, frame = cap.read()

        if not flag:
            break

        frame = cv.flip(frame, 1)
        frame_rgb = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
        results = hands.process(frame_rgb)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                # Yalnızca 8 ve 12. landmark'ları alın
                landmarks_to_draw = [hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP],
                                     hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP]]
                
                # 8. ve 12. landmark'larının konumunu alın
                landmark8_pos = (int(landmarks_to_draw[0].x * frame.shape[1]), int(landmarks_to_draw[0].y * frame.shape[0]))
                landmark12_pos = (int(landmarks_to_draw[1].x * frame.shape[1]), int(landmarks_to_draw[1].y * frame.shape[0]))

                # Görüntü üzerine belirli landmark'ları çizdirin
                mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS,
                                          mp_drawing_styles.get_default_hand_landmarks_style(),
                                          mp_drawing_styles.get_default_hand_connections_style())

                
                fark = landmark12_pos[1] - landmark8_pos[1]

                if fark > 200:
                    if flag == 1:
                        fark = landmark12_pos[1] - landmark8_pos[1]
                        flag = 0
                        liste.append(landmark8_pos[0])
                        liste.append(landmark8_pos[1])
                        #print(liste)
                        
                        for i in range(0,int(len(liste)/2)):
                            cv.circle(frame, (liste[i],liste[i+1]), 20, (255, 0, 243), -1)
                            i=i+1

                    
                        #cv.circle(frame, (la) , 20, (255, 0, 243), -1)

                        

                else:
                    flag = 1
                    liste = [0] * len(liste)

                    
                    
                    


        cv.imshow("result", frame)

        if cv.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv.destroyAllWindows()
