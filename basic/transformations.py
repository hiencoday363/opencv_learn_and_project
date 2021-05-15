import cv2 as cv
import numpy as np

img = cv.imread('../images/house.jpg')
cv.imshow('house', img)

# translation
def translate(img, x, y):
	transMat = np.float32([[1,0,x],[0,1,y]])
	dimensions = (img.shape[1], img.shape[0])
	return cv.warpAffine(img, transMat, dimensions)

# -x --> left
# x --> right
# -y --> up
# y --> down

# dich chuyen img
translated = translate(img, -100, 100)
# cv.imshow('translated', translated)


def rotate(img, angle, rotPoint=None):
	width, height = img.shape[:2]


	if rotPoint == None:
		rotPoint = (height/2, width/2)


	rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1)
	dimensions = (height,width)

	return cv.warpAffine(img, rotMat, dimensions)

# rotation
# rotated = rotate(img, 90)
# cv.imshow('rotated', rotated)

# flipping: lật ảnh
flip = cv.flip(img, -1)
# cv.imshow('flipped', flip)


# Perspective Transformation: giống cắt ảnh từ 4 điểm
# thành ảnh mới với độ dài các cạnh là 4 điểm mới thứ
def perspective(img):
	rows,cols,ch = img.shape

	pts1 = np.float32([[56,65],[368,52],[28,387],[389,390]]) # 4 diem dau vao
	pts2 = np.float32([[0,0],[300,0],[0,300],[300,300]]) # 4 diem dau ra
	print(f'pst1: {pts1.shape}')
	M = cv.getPerspectiveTransform(pts1,pts2)

	return cv.warpPerspective(img,M,(300,300))

perspectived = perspective(img)
cv.imshow('perspectived', perspectived)


cv.waitKey(0)
