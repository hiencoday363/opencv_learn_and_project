import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread("images/tier.jpeg")
# cv.imshow('Image', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

# simple thresholding
threshold, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
cv.imshow('simple thresholded', thresh)

threshold, thresh_inv = cv.threshold(gray, 125, 255, cv.THRESH_BINARY_INV)
# cv.imshow('simple thresholded INVERSE', thresh_inv)


# adaptive thresholding
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 9)
cv.imshow('adaptive thresholding', adaptive_thresh)



cv.waitKey(0)