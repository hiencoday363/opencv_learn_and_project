import cv2 as cv

img = cv.imread('images/house.jpg')
# cv.imshow('house', img)

# average
average = cv.blur(img, (7,7))
cv.imshow('Average Blur', average)

# gaussian blur
gauss = cv.GaussianBlur(img, (7,7), 0)
cv.imshow('Gaussian Blur', gauss)
 
 # Median Blur
median = cv.medianBlur(img, 7)
cv.imshow('Median Blur', median)

# bilaterial
bilateral = cv.bilateralFilter(img, 10, 35, 35)
cv.imshow('Bilateral Filter', bilateral)


cv.waitKey(0)