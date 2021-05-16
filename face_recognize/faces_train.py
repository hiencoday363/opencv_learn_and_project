import os
import cv2 as cv
import numpy as np


path = '../Faces/train/'
 
haar_cascade = cv.CascadeClassifier('./haar_face.xml')

features = []
labels = []

def create_train(base_path):
	for i, name in enumerate(os.listdir(base_path)):

		for img in os.listdir(base_path+name):

			img = cv.imread(base_path+name+'/'+img)
			gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
			faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)

			for (x,y,w,h) in faces_rect:
				face_roi = gray[y:y+h, x:x+w]
				features.append(face_roi)
				labels.append(i)



create_train(path)

print('--------train done--------')

features = np.array(features, dtype='object')
labels = np.array(labels)

# CREATE MODEL
face_recognizer = cv.face.LBPHFaceRecognizer_create()

# fit MODEL
face_recognizer.train(features, labels)

# save model and data
face_recognizer.save('face_trained.yml')
np.save('features.npy', features)
np.save('labels.npy', labels)
