import os
import cv2
# Taking Input For Folder Name
print('USER ID INPUT: ')
person_id = input()
basepath = 'input_images/'
dirName  = basepath + str(person_id)

# Creating Folder
os.mkdir(dirName)
print("Directory " , dirName ,  " Created ") 

# Capturing Images -> 20 Image Capture
camera = cv2.VideoCapture(0)
i = 0
while i < 100:
    input('Press Enter to capture')
    return_value, image = camera.read()
    cv2.imwrite(dirName+'/'+str(i)+'.jpg', image)
    i += 1
del(camera)

# Saving Image Into Specific Folder
print('Finish Taking Image For USER: {}'.format(person_id))

