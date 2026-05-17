import cv2
import mediapipe as mp
import pyautogui
import math
import time

cam = cv2.VideoCapture(0)

hands_detector = mp.solutions.hands.Hands(
    max_num_hands=1,
    min_detection_confidence=0.7
)

draw = mp.solutions.drawing_utils

screen_w, screen_h = pyautogui.size()

pinch_frames = 0
exit_frames = 0

while True:
    success, frame = cam.read()
    if not success:
        break

    frame = cv2.flip(frame, 1)

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands_detector.process(rgb)

    if result.multi_hand_landmarks:
        for hand in result.multi_hand_landmarks:

            draw.draw_landmarks(
                frame,
                hand,
                mp.solutions.hands.HAND_CONNECTIONS
            )

            lm = hand.landmark

            # Mouse movement with index finger
            index_x = lm[8].x
            index_y = lm[8].y

            screen_x = screen_w * index_x
            screen_y = screen_h * index_y

            pyautogui.moveTo(screen_x, screen_y)

            # Click gesture
            thumb_x = lm[4].x
            thumb_y = lm[4].y
                #pinch se click karne k liye distance nikalna h thumb aur index finger ke bich ka
                #distance = math.hypot(
                #    thumb_x - index_x,
                #   thumb_y - index_y
                #)

            #if distance < 0.05:
            # Distance between thumb and index finger
            distance = math.hypot(thumb_x - index_x, thumb_y - index_y)

                # Require stable pinch for multiple frames
            cv2.putText(
                frame,
                f"distance:{round(distance,3)}",
                (20,50),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (255,0,0),
                2
            )
            if distance < 0.09:
                    pinch_frames += 1
                    if pinch_frames>5:
                       pyautogui.click()     
                 #  pyautogui.sleep(0.5)  # prevent multiple clicks
                       print("Click")
                       pinch_frames = 0
            else:
                    pinch_frames = 0
            
            
                
                

            # -------- EXIT GESTURE --------
            # Detect open palm (all fingers up)

            fingers_up = 0

            tips = [8, 12, 16, 20]

            for tip in tips:
                if lm[tip].y < lm[tip - 2].y:# compare tip with pip joint to check if finger is up
                    fingers_up += 1

            # Thumb
            cv2.putText(
                frame,
                f"Fingers: {fingers_up}",
                (20, 100),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (255, 0, 0),
                2
            )
            

            # If all 5 fingers up
            if fingers_up == 5:
                exit_frames+= 1
                if exit_frames > 15: # stable for 15 frames
                    #    exit_start = time.time()

                #elapsed = time.time() - exit_start

               # cv2.putText(
                #    frame,
                #    f"EXIT IN {int(2 - elapsed) + 1}",
                 #   (50, 100),
                  #  cv2.FONT_HERSHEY_SIMPLEX,
                   # 1,
                  #  (0, 0, 255),
                  #  3
                #)

                #if elapsed > 2:
                    print("Exit gesture detected")
                    cam.release()
                    cv2.destroyAllWindows()
                    exit()

            else:
                exit_start = None

    cv2.imshow("Virtual Touchscreen", frame)

    if cv2.waitKey(1) == 27:
        break

cam.release()
cv2.destroyAllWindows()