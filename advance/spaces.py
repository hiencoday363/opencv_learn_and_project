import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


img = cv.imread('images/house.jpg')
cv.imshow('house', img)

plt.imshow(img)
plt.show()


# bgr to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('gray', gray)

# bgr to hsv
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
# cv.imshow('hsv', hsv)

# bgr to lab
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
# cv.imshow('hsv', lab)




# cv.waitKey(0)