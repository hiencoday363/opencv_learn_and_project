import cv2 as cv
import numpy as np

# read camera

width = 460
height = 400

capture = cv.VideoCapture(0)
capture.set(3,width)
capture.set(4,height)

my_colors = [[5,107,0,19,255,255],
            [133,56,0,159,156,255],
            [57,76,0,100,255,255]]

my_color_val = [[51,153,255], # bgr
                [255,0,255],
                [0,255,0]]

my_points = [] # [x,y,id_my_color]

def myColors(frame, colors, my_color_val):
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    newPoint = []

    for id,color in enumerate(colors):
        lower = np.array(color[:3])
        upper = np.array(color[3:])

        mask = cv.inRange(hsv, lower, upper)
        x, y = getContours(mask)
        cv.circle(background,(x,y),10,my_color_val[id],cv.FILLED)

        if x!=0 and y!=0:
            newPoint.append((x, y, id))

        # cv.imshow(f'video {color[0]}', mask)

    return newPoint


def getContours(img):
    contours, hierarchies = cv.findContours(img, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
    x,y,w,h = 0,0,0,0
    for cnt in contours:
        area = cv.contourArea(cnt)
        if area > 1000:
            cv.drawContours(background, cnt, -1, (255, 0, 0), 2)

            peri = cv.arcLength(cnt, True)
            approx = cv.approxPolyDP(cnt, 0.02 * peri, True)

            x, y, w, h = cv.boundingRect(approx)
    return x+w//2,y


def drawOnCanvas(myPoint, myColorVal):
    for point in myPoint:
        cv.circle(background, (point[0], point[1]), 10, my_color_val[point[2]], cv.FILLED)

'''
## to find color, run if you dont know else dont run

cv.namedWindow("TrackBars")
cv.resizeWindow('TrackBars', 640, 240)

cv.createTrackbar('Hue min', 'TrackBars', 0, 179, lambda x: x)
cv.createTrackbar('Hue max', 'TrackBars', 0,179, lambda x: x)
cv.createTrackbar('Sat min', 'TrackBars', 0, 125, lambda x: x)
cv.createTrackbar('Sat max', 'TrackBars', 125, 255, lambda x: x)
cv.createTrackbar('Val min', 'TrackBars', 0, 125, lambda x: x)
cv.createTrackbar('Val max', 'TrackBars', 125, 255, lambda x: x)

def getTrackBars(frame):
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    
    h_min = cv.getTrackbarPos('Hue min', 'TrackBars')
    h_max = cv.getTrackbarPos('Hue max', 'TrackBars')
    s_min = cv.getTrackbarPos('Sat min', 'TrackBars')
    s_max = cv.getTrackbarPos('Sat max', 'TrackBars')
    v_min = cv.getTrackbarPos('Val min', 'TrackBars')
    v_max = cv.getTrackbarPos('Val max', 'TrackBars')

    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    
    mask = cv.inRange(hsv, lower, upper)
    cv.imshow('video', mask)
    
'''

while True:
    isTrue, frame = capture.read()
    background = frame.copy()

    newPoints = myColors(frame,my_colors, my_color_val)
    if len(newPoints)>0:
        for point in newPoints:
            my_points.append(point)
    if len(my_points)>0:
        drawOnCanvas(my_points,my_color_val)

    # cv.imshow('original ',frame)
    cv.imshow('original ',background)

    if cv.waitKey(1) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()
