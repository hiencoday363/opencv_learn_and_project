import cv2 as cv
import numpy as np


blank = np.zeros((500,500,3), dtype='uint8')

# cv.imshow('blank', blank) 

# 1. Paint the image a certain color

# blank[350:400, 100:150] = 0,0,255
# cv.imshow('red', blank)

# 2.draw a rectangle 

# cv.rectangle(blank, (0,0), (200,300),(0,0,255), thickness=3)
# cv.imshow('rectangle', blank)

# 3. draw circle

# blank.shape[1]: width
# blank.shape[0]: height
# cv.circle(blank, (blank.shape[1]//2,blank.shape[0]//2), 100, (0,255,0), thickness=2)
# cv.imshow('circle', blank)

# 4. draw a line

# cv.line(blank, (100,50), (400,450), (255,0,0), thickness=3)
# cv.imshow('line', blank)

# 5. write text
cv.putText(blank, 'hello, my friend', (100,50), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0), 2)
cv.imshow('text', blank)
cv.waitKey(0)