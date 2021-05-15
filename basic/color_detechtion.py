import cv2 as cv
import numpy as np


def emtpy(a):
    pass


path = '../images/house.jpg'

cv.namedWindow("TrackBars")
cv.resizeWindow('TrackBars', 640, 240)

cv.createTrackbar('Hue min', 'TrackBars', 0, 179, emtpy)
cv.createTrackbar('Hue max', 'TrackBars', 19, 179, emtpy)
cv.createTrackbar('Sat min', 'TrackBars', 110, 255, emtpy)
cv.createTrackbar('Sat max', 'TrackBars', 230, 255, emtpy)
cv.createTrackbar('Val min', 'TrackBars', 100, 255, emtpy)
cv.createTrackbar('Val max', 'TrackBars', 255, 255, emtpy)

while True:
    img = cv.imread(path)
    hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

    h_min = cv.getTrackbarPos('Hue min', 'TrackBars')
    h_max = cv.getTrackbarPos('Hue max', 'TrackBars')
    s_min = cv.getTrackbarPos('Sat min', 'TrackBars')
    s_max = cv.getTrackbarPos('Sat max', 'TrackBars')
    v_min = cv.getTrackbarPos('Val min', 'TrackBars')
    v_max = cv.getTrackbarPos('Val max', 'TrackBars')

    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    mask = cv.inRange(hsv, lower, upper)

    # cv.imshow('original',img)
    # cv.imshow('hsv',hsv)

    cv.imshow('mask', mask)

    if cv.waitKey(1) & 0xFF == ord('d'):
        break
