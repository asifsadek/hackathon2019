
import numpy as np
from cv2 import *
cap = VideoCapture(0)

faceDetactor = CascadeClassifier('haarcascade_frontalface_default.xml')
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("recognizerModel.yml")


while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    faces = faceDetactor.detectMultiScale(frame,1.3,5)
    gray = cvtColor(frame,COLOR_BGR2GRAY)
    for x,y,w,h in faces:
	    rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
	    ids,conf = recognizer.predict(gray[y:y+h,x:x+w])
	    print(ids)
	    putText(frame,str(ids), (x,y-10), FONT_HERSHEY_SIMPLEX, 1, (0,0,255))
    imshow('frame',frame)
    if waitKey(1) & 0xFF == ord('q'):
        break
# When everything done, release the capture
cap.release()
destroyAllWindows()
