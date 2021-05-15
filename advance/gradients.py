import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread("../images/tier.jpeg")
# cv.imshow('Image', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)


# laplacian 
lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow('laplacian', lap)


# sobel 
sobelx = cv.Sobel(gray, cv.CV_64F, 1,0)
sobely = cv.Sobel(gray, cv.CV_64F, 0,1)
combine_sobel = cv.bitwise_or(sobelx, sobely)

# cv.imshow('sobel x', sobelx)
# cv.imshow('sobel y', sobely)
cv.imshow('combine_sobel', combine_sobel)


canny = cv.Canny(gray, 125, 175)
cv.imshow('Canny edge', canny)



cv.waitKey(0)
