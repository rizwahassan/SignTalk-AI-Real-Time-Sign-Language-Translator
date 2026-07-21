import cv2
import mediapipe as mp
import pickle
import numpy as np
import pyttsx3
import time
model = pickle.load(open('model.p', 'rb'))['model']
engine = pyttsx3.init()
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=1,
    min_detection_confidence=0.7
)
draw = mp.solutions.drawing_utils
last_sign = ""
last_time = 0
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    if not ret:
        break
    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb)
    if results.multi_hand_landmarks:
        for hand in results.multi_hand_landmarks:
            draw.draw_landmarks(
                frame,
                hand,
                mp_hands.HAND_CONNECTIONS
            )
            data = []
            for lm in hand.landmark:
                data.extend([lm.x, lm.y, lm.z])
            sign = str(model.predict([np.asarray(data)])[0]).upper()
            if sign != last_sign and time.time() - last_time > 2:
                try:
                    engine.say(sign)
                    engine.runAndWait()
                except:
                    pass
                last_sign = sign
                last_time = time.time()
            cv2.rectangle(frame, (20, 20), (280, 90), (0, 0, 0), -1)
            cv2.putText(
                frame,
                sign,
                (35, 70),
                cv2.FONT_HERSHEY_SIMPLEX,
                1.5,
                (255, 255, 255),
                3
            )
    cv2.imshow("SignTalk Translator", frame)
    key = cv2.waitKey(1) & 0xFF
    if key == ord('c'):
        last_sign = ""
        print("Speech Reset")
    elif key == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()