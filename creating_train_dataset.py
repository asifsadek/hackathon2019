# Generating the Train Data

import os
from cv2 import *
import numpy as np 
from PIL import Image

# Detator
faceDetactor = CascadeClassifier('haarcascade_frontalface_default.xml')

# Take the input image
path = 'input_images/'
train = 'train/'
folder_name = 1

for folder_name in range(1,5):
	sample_number = 0
	for sample_number in range(0,10):
		img = imread(path+'/'+str(folder_name)+'/'+str(sample_number)+'.jpg')
		# Convert it  into gray scale
		gray = cvtColor(img,COLOR_BGR2GRAY)
		# Detact the faces and cunt them
		faces = faceDetactor.detectMultiScale(gray,1.3,5)
		# print len(faces)
		# Cut the face off from the image
		for x,y,w,h in faces:
			rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
		# Save the cut image into a folder with 
		# the name of the folder as id of the user
			imwrite(train  + str(folder_name)+ '.' + str(sample_number) + '.jpg',gray[y:y+h,x:x+w])
		sample_number += 1
		# imshow('Main Image',img)
waitKey(0)
destroyAllWindows()

