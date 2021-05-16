import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread("../images/group.jpg")
img = cv.resize(img, (500,500), interpolation=cv.INTER_AREA)
# cv.imshow('Image', img)



gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)


# link haarcascades default
'''
https://github.com/opencv/opencv/tree/master/data/haarcascades
'''

## doc file xml (algorithms)
haar_cascade = cv.CascadeClassifier('../face_recognize/haar_face.xml')

faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=6)

print(f"number of faces found: {len(faces_rect)}")

features = []

for (x,y,w,h) in faces_rect:
	cv.rectangle(img, (x,y), (x+w, y+h), (0,255,0), thickness=2)
	features.append((x,y,w,h))
	
# cv.imshow('detected faces', img)
# cv.imshow('detected faces1', img[features[0][1]:features[0][1]+features[0][3], features[0][0]:features[0][0]+features[0][2]])
# cv.imshow('detected faces2', img[features[1][1]:features[1][1]+features[1][3], features[1][0]:features[1][0]+features[1][2]])
# cv.imshow('detected faces3', img[features[2][1]:features[2][1]+features[2][3], features[2][0]:features[2][0]+features[2][2]])

cv.waitKey(0)
