import numpy as np
from cv2 import *
cap = VideoCapture(0)
import pygame
pygame.mixer.init()

faceDetactor = CascadeClassifier('haarcascade_frontalface_default.xml')
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("recognizerModel.yml")


while(True):	
	ret, im = cap.read()
	gray = cvtColor(im,COLOR_BGR2GRAY)
	
	faces = faceDetactor.detectMultiScale(gray,1.3,5)

	# For Face Detection
	for x,y,w,h in faces:
		rectangle(im,(x,y),(x+w,y+h),(0,0,255),2)
		ids,conf = recognizer.predict(gray[y:y+h,x:x+w])
		
		#print(ids)
		
		if ids == 1:
			ids = "S"
		elif ids == 2:
			ids = "m"
		elif ids == 3:
			ids = "i"
		putText(im,str(ids), (x,y-10), FONT_HERSHEY_SIMPLEX, 1, (0,0,255))
		
	imshow('frame',im)
	
	if waitKey(1) & 0xFF == ord('q'):
		break


cap.release()
destroyAllWindows()