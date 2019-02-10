import numpy as np
from cv2 import *
cap = VideoCapture(0)
import pygame
pygame.mixer.init()

faceDetactor = CascadeClassifier('haarcascade_frontalface_default.xml')
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("recognizerModel.yml")
car_cascade = cv2.CascadeClassifier('cars.xml')

def yeal(id):
	if id == 1: pygame.mixer.music.load("sajjad.mp3")
	elif id == 2: pygame.mixer.music.load("sajjad.mp3")
	elif id == 100: pygame.mixer.music.load("car.mp3")
	pygame.mixer.music.play()
	while pygame.mixer.music.get_busy() == True:
		continue


while(True):	
	ret, im = cap.read()
	gray = cvtColor(im,COLOR_BGR2GRAY)
	
	faces = faceDetactor.detectMultiScale(gray,1.3,5)
	cars = car_cascade.detectMultiScale(gray, 1.1, 1)
	
	# For Car Detection
	ncars = 0
	for (x, y, w, h) in cars:
		cv2.rectangle(im, (x,y), (x+w,y+h), (0,0,0), 2)
		ncars = ncars + 1
	
	print(ncars)
	
	# For Face Detection
	for x,y,w,h in faces:
		rectangle(im,(x,y),(x+w,y+h),(0,0,255),2)
		ids,conf = recognizer.predict(gray[y:y+h,x:x+w])
		
		#print(ids)
		
		if ids == 1:
			ids = "Sajjad"
		elif ids == 2:
			ids = "Mortuza"
		putText(im,str(ids), (x,y-10), FONT_HERSHEY_SIMPLEX, 1, (0,0,255))
		
	imshow('frame',im)
	
	if waitKey(1) & 0xFF == ord('q'):
		break


cap.release()
destroyAllWindows()
