import cv2
import numpy as np


cap = cv2.VideoCapture(0)
prevFrame = None
contourAreaThreshold = 400


while True:
    ret, frame = cap.read()
    if not ret:
        break

    grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    grayFrame = cv2.GaussianBlur(grayFrame, (5, 5), 0)

    if prevFrame is None:
        prevFrame = grayFrame
        continue

    diffFrame = cv2.absdiff(grayFrame, prevFrame)
    prevFrame = grayFrame
    threshFrame = cv2.threshold(diffFrame, 18, 255, cv2.THRESH_BINARY)[1]
    threshFrame = cv2.dilate(threshFrame, None, iterations=3)
    contours = cv2.findContours(threshFrame, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]

    if len(contours) > 0:
        contours = sorted(contours, key=cv2.contourArea, reverse=True)
        if cv2.contourArea(contours[0]) > contourAreaThreshold:
            x, y, w, h = cv2.boundingRect(contours[0])
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 4)
    

    cv2.imshow('Frame', frame)
    # cv2.imshow('Diff Frame', diffFrame)
    # cv2.imshow('Thresh Frame', threshFrame)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()