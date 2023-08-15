import cv2 as cv
import mediapipe as mp

flag = 1
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands

cap = cv.VideoCapture(1)

# Çizim rengini ve kalınlığını belirleyin
draw_color = (255, 0, 243)
draw_thickness = 4

with mp_hands.Hands(
    model_complexity=0,
    min_tracking_confidence=0.5,
    min_detection_confidence=0.5,
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
                

                # Elin işaret parmağı ucuna göre çizim yapın
                while flag == 1:
                    landmark8_pos = (int(landmarks_to_draw[0].x * frame.shape[1]), int(landmarks_to_draw[0].y * frame.shape[0]))
                    landmark12_pos = (int(landmarks_to_draw[1].x * frame.shape[1]), int(landmarks_to_draw[1].y * frame.shape[0]))

                # Görüntü üzerine belirli landmark'ları çizdirin
                    mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS,
                                          mp_drawing_styles.get_default_hand_landmarks_style(),
                                          mp_drawing_styles.get_default_hand_connections_style())
                    fark = landmark12_pos[1] - landmark8_pos[1]
                    
                    if fark > 200:
                        if flag == 1:
                            while fark > 200:       
                                cv.circle(frame, landmark8_pos, draw_thickness, draw_color, -1)

        cv.imshow("result", frame)

        if cv.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv.destroyAllWindows()
