import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:

    # Take each frame
    _, frame = cap.read()

    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # boundary RED color range values; Hue (160 - 180)
    lower2 = np.array([160, 100, 150])
    upper2 = np.array([179, 255, 255])
    
    mask = cv2.inRange(hsv, lower2, upper2)

    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame, frame, mask=mask)

    if cv2.countNonZero(cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)) > 500:
        print("Red LED Detected")

    cv2.imshow("frame", frame)
    cv2.imshow("res", res)
    k = cv2.waitKey(1) & 0xFF
    if k == ord("q"):
        break

cv2.destroyAllWindows()
