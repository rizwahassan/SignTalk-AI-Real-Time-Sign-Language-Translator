import cv2
import mediapipe as mp
import csv
import os
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=1, min_detection_confidence=0.7)
label = input("Enter the name of the sign you are recording (e.g., Hello): ")
cap = cv2.VideoCapture(0)
print(f"Recording {label}. Press 's' to SAVE a frame, or 'q' to QUIT.")

file_exists = os.path.isfile('hand_data.csv')
while cap.isOpened():
    success, frame = cap.read()    
    if not success: 
        break
    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb)
    if results.multi_hand_landmarks:   
        for hand_landmarks in results.multi_hand_landmarks:
            mp.solutions.drawing_utils.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            if cv2.waitKey(1) & 0xFF == ord('s'):  
                data = []
                for lm in hand_landmarks.landmark:
                    data.extend([lm.x, lm.y, lm.z])  # Takes x,y,z position of each dot
                data.append(label) 
                
                with open('hand_data.csv', mode='a', newline='') as f:
                    writer = csv.writer(f)
                    writer.writerow(data)
                print(f"Saved one frame for {label}!")

    cv2.imshow("Data Collector - Press 's' to capture", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break

cap.release()
cv2.destroyAllWindows()