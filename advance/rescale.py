import cv2 as cv


def rescaleFrame(frame, scale=0.75):
	'''
	change on Image, Video and Live Video (webcam)
	'''
	width = int(frame.shape[1] * scale)
	height = int(frame.shape[0] * scale)

	dimentions = (width,height)

	return cv.resize(frame, dimentions, interpolation=cv.INTER_AREA)


def changeRes(width, height):
	# only Live Video (webcam)
	capture.set(3, width)
	capture.set(4, height)


# img = cv.imread('images/hotgirl2.jpg')
# cv.imshow('image', img)

# resize_img = rescaleFrame(img,scale=1.5)
# cv.imshow('image', resize_img)


# cv.waitKey(0)


# reading video frames
# capture = cv.VideoCapture('video/production ID_3752507.mp4') 
capture = cv.VideoCapture(0) 
# changeRes(900, 500)

while True:
	isTrue, frame = capture.read()

	# frame_resized = rescaleFrame(frame, scale=.5)

	cv.imshow('video',frame)
	# cv.imshow('video',frame_resized)

	if cv.waitKey(20) & 0xFF==ord('d'):
		break

capture.release()
cv.destroyAllWindows()


