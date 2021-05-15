import cv2 as cv

img = cv.imread('../images/tier.jpeg')
cv.imshow('tiger', img)


# converting to grayscale

# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('tiger_gray', gray)

# blur

blur = cv.GaussianBlur(img, (5,5), cv.BORDER_DEFAULT)
# cv.imshow('tiger_blur', blur)

# Edge cascade : get edge
canny = cv.Canny(blur, 125, 175)
cv.imshow('tiger_canny', canny)

# dilateing the image : giãn ảnh
dilated = cv.dilate(canny, (7,7), iterations=3)
cv.imshow('tiger_dilated', dilated)

# eroding : ngược lại với giãn ảnh
eroded = cv.erode(dilated, (1,1) , iterations=1)
cv.imshow('tiger_eroded', eroded)

# resize
resized = cv.resize(img, (500,500), interpolation=cv.INTER_AREA)
# cv.imshow('tiger_resized', resized)

# crop 
cropped = img[50:200, 250:400]
cv.imshow('tiger_cropped',cropped)



cv.waitKey(0)
