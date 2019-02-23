import os
from cv2 import *
import numpy as np 
from PIL import Image

# Creating the recognizer
# Local Binary Patterns Histograms 
recognizer = face.LBPHFaceRecognizer_create()
path = 'train'
def getImagesWithID(path):
	imagePaths = [os.path.join(path,f) for f in os.listdir(path)]
	print (imagePaths)
	faces = []
	IDs = []
	for imagePath in imagePaths:
		faceImg = Image.open(imagePath).convert('L')
		faceNp = np.array(faceImg,'uint8')
		ID = int(os.path.split(imagePath)[-1].split('.')[0])
		# print os.path.split(imagePath)[-1].split('.')[0]
		faces.append(faceNp)
		IDs.append(ID)
		# imshow("training",faceNp)
		# waitKey(10)
	return np.array(IDs), faces
# getImagesWithID(path)
Ids, faces = getImagesWithID(path)
recognizer.train(faces,Ids)
recognizer.save('recognizerModel.yml')
cv2.destroyAllWindows()
