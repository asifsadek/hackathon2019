#!/usr/bin/env python3
import numpy as np
from cv2 import *
cap = VideoCapture(0)
import pygame
pygame.mixer.init()

print("Code Run Successfully .... ")

faceDetactor = CascadeClassifier('haarcascade_frontalface_default.xml')
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("recognizerModel.yml")

previous = 0

while(True):
	ret, im = cap.read()
	gray = cvtColor(im,COLOR_BGR2GRAY)
	faces = faceDetactor.detectMultiScale(gray,1.3,5)
	for x,y,w,h in faces:
		rectangle(im,(x,y),(x+w,y+h),(0,0,255),2)
		ids,conf = recognizer.predict(gray[y:y+h,x:x+w])
		
		if ids != previous:
			print(ids)
			previous = ids
			if ids == 1:
				pygame.mixer.music.load("s.mp3")
			elif ids == 2:
				pygame.mixer.music.load("m.mp3")
			elif ids == 2:
				pygame.mixer.music.load("i.mp3")
			pygame.mixer.music.play()
