import cv2
import mediapipe as mp


mp_hands = mp.solutions.hands.Hands(max_num_hands=2)
drawing_util = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)
finger_counter = 0
finger_tip = [8, 12, 16, 20]

while True:
    mosht = ''
    finger_counter = 0
    success , frame = cap.read()

    if not success:
        break

    frameRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = mp_hands.process(frameRGB)
    if result.multi_hand_landmarks:
        for hand in result.multi_hand_landmarks:
            drawing_util.draw_landmarks(frame, hand,mp.solutions.hands.HAND_CONNECTIONS)
            landmark = hand.landmark

            for tip in finger_tip:
                if landmark[tip].y < landmark[tip-2].y:
                    finger_counter +=1
                
                
            if landmark[4].x > landmark[3].x:
                finger_counter +=1
            if finger_counter ==5:
                mosht = 'dast buz ast'
            elif landmark[8].y < landmark[8-2].y and landmark[12].y < landmark[12-2].y :
                mosht = 'victory'
                cv2.imwrite('./images/test.png', frame)


            else:
                mosht = 'mosht'
            
    cv2.putText(frame, str(finger_counter), (600, 40), cv2.FONT_HERSHEY_COMPLEX, 1, (255,0,0),1)
    cv2.putText(frame, mosht, (1, 40), cv2.FONT_HERSHEY_COMPLEX, 1, (255,0,0),1)

    cv2.imshow('webcame',frame)
    if cv2.waitKey(1) & 0xFF ==ord("q"):
        break
cap.release()
cv2.destroyAllWindows()