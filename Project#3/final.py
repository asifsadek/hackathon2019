import numpy as np
import cv2
import serial
import time

ser = serial.Serial(
    port='/dev/ttyACM0',
    baudrate = 9600
)
time.sleep(1)

def run():
    time.sleep(0.5)
    ser.write('r'.encode())
	
def stop():
    time.sleep(0.5)
    ser.write('s'.encode())

x,y,w,h = 0,0,0,0
cap = cv2.VideoCapture(0)
classifier = cv2.CascadeClassifier('cascade.xml')

while(True):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    bomb = classifier.detectMultiScale(gray,1.2,6)

    if len(bomb) > 0:
        stop()
        
    for (x,y,w,h) in bomb:
        frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
    
    cv2.imshow('frame',frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
        
cap.release()
cv2.destroyAllWindows()
