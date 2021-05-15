import cv2 as cv


'''
read video
'''
capture = cv.VideoCapture(0) # pass `0` turn on webcam device
# set width, height
capture.set(3,300)


# capture = cv.VideoCapture('../video/production ID_3752507.mp4') 

while True:
	isTrue, frame = capture.read()

	cv.imshow('video',frame)

	if cv.waitKey(1) & 0xFF==ord('d'):
		break

capture.release()
cv.destroyAllWindows()


'''
read image
'''

# img = cv.imread('images/hotgirl2.jpg')

# cv.imshow('image', img)

# cv.waitKey(0)