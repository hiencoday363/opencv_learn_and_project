import cv2 as cv
import numpy as np

# read camera
width_cam = 460
height_cam = 400

width_img = 250
height_img = 260


def vconcat_resize_min(im_list, interpolation=cv.INTER_CUBIC):
    w_min = min(im.shape[1] for im in im_list)
    im_list_resize = [cv.resize(im, (w_min, int(im.shape[0] * w_min / im.shape[1])), interpolation=interpolation)
                      for im in im_list]
    return cv.vconcat(im_list_resize)


def hconcat_resize_min(im_list, interpolation=cv.INTER_CUBIC,size=(0,0)):
    if size==(0,0):
        h_min = min(im.shape[0] for im in im_list)
        im_list_resize = [cv.resize(im, (int(im.shape[1] * h_min / im.shape[0]), h_min), interpolation=interpolation)
                          for im in im_list]
        return cv.hconcat(im_list_resize)

    im_list_resize = [cv.resize(im, size, interpolation=interpolation) for im in im_list]
    return cv.hconcat(im_list_resize)

def concat(im_list_2d, interpolation=cv.INTER_CUBIC, size=(0,0)):
    im_list_v = [hconcat_resize_min(im_list_h, interpolation=cv.INTER_CUBIC,size=size) for im_list_h in im_list_2d]
    return vconcat_resize_min(im_list_v, interpolation=cv.INTER_CUBIC)


def preprocess(img):
    img_gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    img_blur = cv.GaussianBlur(img_gray,(5,5),1)
    img_canny = cv.Canny(img_blur,200, 200)
    # gian anh
    img_dilate = cv.dilate(img_canny,(5,5),iterations=2)
    # nguoc lai voi gian
    img_erode = cv.erode(img_dilate,(5,5),iterations=1)
    return  img_erode

def getContours(img):
    contours, hierarchies = cv.findContours(img, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
    biggest = np.array([])
    maxArea = 0

    for cnt in contours:
        area = cv.contourArea(cnt)
        if area > 5000:
            # cv.drawContours(background, cnt, -1, (255, 0, 0), 2)
            peri = cv.arcLength(cnt, True)
            approx = cv.approxPolyDP(cnt, 0.02 * peri, True)

            if area > maxArea and len(approx)==4:
                biggest = approx
                maxArea = area

    cv.drawContours(background, biggest, -1, (255, 0, 0), 10)

    return biggest

def reorder(myPoints):
    myPoints = myPoints.reshape((4,2))
    myPointNew = np.zeros((4,1,2), np.int32)
    add = myPoints.sum(1)

    myPointNew[0] = myPoints[np.argmin(add)]
    myPointNew[3] = myPoints[np.argmax(add)]
    diff = np.diff(myPoints, axis=1)
    myPointNew[1] = myPoints[np.argmin(diff)]
    myPointNew[2] = myPoints[np.argmax(diff)]

    return myPointNew

def getWarp(img, biggest):
    width = 350
    height=460
    bg = reorder(biggest)

    pts1 = np.float32(bg)
    pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])

    matrix = cv.getPerspectiveTransform(pts1, pts2)

    return cv.warpPerspective(img, matrix, (width, height))


'''
# test on image
'''
img_path = cv.imread('../images/1.jpg')
img = cv.resize(img_path, (300, 300))
background = img.copy()

img_thres = preprocess(img)
biggest = getContours(img_thres)
if len(biggest)!=0:
    img_warp = getWarp(img,biggest)
    img_warp = cv.resize(img_warp, (250, 250))
else:
    img_warp = img

cv.imshow('background ',background)
cv.imshow('img_warp ',img_warp)
cv.imshow('img_thres ',img_thres)
cv.imshow('img ',img)

cv.waitKey(0)

'''
capture = cv.VideoCapture(0)

while True:
    isTrue, frame = capture.read()
    frame = cv.resize(frame, (width_img, height_img))
    background = frame.copy()

    # concat_img = concat([[frame, frame], [frame, frame]], size=(width_img, height_img))
    img_thres = preprocess(frame)
    getContours(img_thres)


    cv.imshow('original ',background)

    if cv.waitKey(1) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()
'''
