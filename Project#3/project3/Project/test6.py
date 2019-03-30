import os
paths = os.listdir('p')

import cv2

for path in paths:
    print(path)
    gray = cv2.cvtColor(cv2.imread('p/'+path), cv2.COLOR_BGR2GRAY)
    cv2.imwrite('p/'+path,gray)

print('Finish')