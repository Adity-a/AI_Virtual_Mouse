import cv2
import numpy as np
import HandTrackingModule as htm
import time
import autopy

##########################
wCam, hCam = 640, 480
frameR = 100  # Frame Reduction
smoothening = 8
#########################

pTime = 0
plocX, plocY = 0, 0
clocX, clocY = 0, 0

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)
detector = htm.handDetector(maxHands=1)
wScr, hScr = autopy.screen.size()
# print(wScr, hScr)

prevThumpUp = 0
lastClickTime = 0

while True:
    # Find hand Landmarks
    success, img = cap.read()
    img = detector.findHands(img)
    lmList, bbox = detector.findPosition(img)
    # Get the tip of the index and middle fingers
    if len(lmList) != 0:
        x1, y1 = lmList[8][1:]
        x2, y2 = lmList[12][1:]
        # print(x1, y1, x2, y2)

    # Check which fingers are up
    fingers = detector.fingersUp()
    # print(fingers)
    cv2.rectangle(img, (frameR, frameR), (wCam - frameR, hCam - frameR),
                  (255, 0, 255), 2)
    # Only Index Finger : Moving Mode
    if len(fingers) >= 3 and fingers[1] == 1 and fingers[2] == 0:
        # Convert Coordinates
        x3 = np.interp(x1, (frameR, wCam - frameR), (0, wScr))
        y3 = np.interp(y1, (frameR, hCam - frameR), (0, hScr))
        # Smoothen Values
        clocX = plocX + (x3 - plocX) / smoothening
        clocY = plocY + (y3 - plocY) / smoothening

        # Move Mouse
        autopy.mouse.move(wScr - clocX, clocY)
        cv2.circle(img, (x1, y1), 15, (255, 0, 255), cv2.FILLED)
        plocX, plocY = clocX, clocY

    # Both Index and middle fingers are up : Clicking Mode
    if len(fingers) >= 3 and fingers[1] == 1 and fingers[2] == 1:
        # Find distance between fingers
        length, img, lineInfo = detector.findDistance(8, 12, img)
        print(length)
        # Click mouse if distance short
        if length < 40 and (time.time() - lastClickTime) > 1:  # Increase the delay to 1 second
            cv2.circle(img, (lineInfo[4], lineInfo[5]),
                       15, (0, 255, 0), cv2.FILLED)
            autopy.mouse.click()
            lastClickTime = time.time()

            # Introduce a delay after the click (e.g., 2 seconds)
            time.sleep(0.2)

        # Thumb is up: Right-click Mode
        """
        if len(fingers) >= 5 and fingers[0] == 1:
            # Perform right-click only if the thumb was down in the previous frame
            if not prevThumbUp:
                autopy.mouse.click(autopy.mouse.Button.RIGHT)
                lastClickTime = time.time()

                # Introduce a delay after the right-click (e.g., 2 seconds)
                time.sleep(0.2)

            prevThumbUp = True
        else:
            prevThumbUp = False
        """
    # Frame Rate
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, f'FPS:{int(fps)}', (20, 50), cv2.FONT_HERSHEY_PLAIN, 2,
                (153, 51, 255), 2)
    # Display
    cv2.imshow("Image", img)

    # If 'q' is pressed, exit the loop and close the window
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
