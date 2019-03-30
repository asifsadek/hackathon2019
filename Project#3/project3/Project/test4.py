import numpy as np
import cv2
classifier = cv2.CascadeClassifier('cascade.xml')
cap = cv2.VideoCapture('2.mp4')
i = 0
while(cap.isOpened()):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    # bomb = classifier.detectMultiScale(gray,1.01,6) #Slow but effective
    bomb = classifier.detectMultiScale(gray,1.3,4) # Fast But Detection Slow
    
    for (x,y,w,h) in bomb:
        frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
    cv2.imshow('frame' , frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()