import numpy as np
import cv2

classifier = cv2.CascadeClassifier('last.xml')
cap = cv2.VideoCapture('1.mp4')
while cap.isOpened():
    ret, img = cap.read()
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    bomb = classifier.detectMultiScale(gray,1.01,7)
    for (x,y,w,h) in bomb:
        img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    cv2.imshow('image',img)

cv2.waitKey(0)
cv2.destroyAllWindows()