import cv2 as cv
import numpy as np

img = cv.imread('images/house.jpg')
# cv.imshow('house', img)

blank = np.zeros(img.shape[:2], dtype='uint8')

# split chanel color
b, g, r = cv.split(img)

# cv.imshow('blue', b)
# cv.imshow('green', g)
# cv.imshow('red', r)

# print(img.shape)
# print(b.shape)
# print(g.shape)
# print(r.shape)

blue = cv.merge([b, blank, blank])
green = cv.merge([blank, g, blank])
red = cv.merge([blank, blank, r])

cv.imshow('blue', blue)
cv.imshow('green', green)
cv.imshow('red', red)


# merge chanel color
img_merge = cv.merge([b,g,r])
cv.imshow('img_merge', img_merge)



cv.waitKey(0)