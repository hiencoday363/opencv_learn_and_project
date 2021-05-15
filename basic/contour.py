import cv2 as cv
import numpy as np

# custom rectangle
def draw_border(img, pt1, pt2, color, thickness, r=5, d=15):
   # r: độ dài của đường góc 
   # d: độ vuông góc

    x1,y1 = pt1
    x2,y2 = pt2
    # Top left
    cv.line(img, (x1 + r, y1), (x1 + r + d, y1), color, thickness)
    cv.line(img, (x1, y1 + r), (x1, y1 + r + d), color, thickness)
    cv.ellipse(img, (x1 + r, y1 + r), (r, r), 180, 0, 90, color, thickness)
    # Top right
    cv.line(img, (x2 - r, y1), (x2 - r - d, y1), color, thickness)
    cv.line(img, (x2, y1 + r), (x2, y1 + r + d), color, thickness)
    cv.ellipse(img, (x2 - r, y1 + r), (r, r), 270, 0, 90, color, thickness)
    # Bottom left
    cv.line(img, (x1 + r, y2), (x1 + r + d, y2), color, thickness)
    cv.line(img, (x1, y2 - r), (x1, y2 - r - d), color, thickness)
    cv.ellipse(img, (x1 + r, y2 - r), (r, r), 90, 0, 90, color, thickness)
    # Bottom right
    cv.line(img, (x2 - r, y2), (x2 - r - d, y2), color, thickness)
    cv.line(img, (x2, y2 - r), (x2, y2 - r - d), color, thickness)
    cv.ellipse(img, (x2 - r, y2 - r), (r, r), 0, 0, 90, color, thickness)


# contour: đường viền
# detection: phát hiện

img = cv.imread('../images/hinh_hoc.jpg')
img = cv.resize(img, (460, 300))
# cv.imshow('hinh hoc', img)

background = img.copy()

blank = np.zeros(img.shape, dtype='uint8')

# need convert them into gray
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('gray', gray)


# c1: blur(làm mờ) -> canny(tìm cạnh)
# blur
blur = cv.GaussianBlur(gray, (3, 3), cv.BORDER_DEFAULT)
# cv.imshow('blur', blur)

# Detect edges
canny = cv.Canny(blur, 50, 50)
# cv.imshow('Canny edge', canny)


# c2: using threshold: ngưỡng into ảnh đen trắng
# 125: ngưỡng giới hạn, 255: max value, thresh_binary: kiểu binary
ret, thresh = cv.threshold(gray, 100, 100, cv.THRESH_BINARY)
'''
điểm ảnh qua ngưỡng thì chuyển thành 255, dưới ngưỡng thì chuyển về 0
tạo thành ảnh đen trắng
'''
# cv.imshow('threshold', thresh)


# find contours
contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
# print(f'{len(contours)} contours founded !')

for cnt in contours:
    area = cv.contourArea(cnt)
    # print(area)
    if area > 1000:
        cv.drawContours(background, cnt, -1, (255, 0, 0), 2)

         # 2 dòng dưới tính chu vi
        peri = cv.arcLength(cnt, True)
        approx = cv.approxPolyDP(cnt, 0.02*peri, True)

        cor = len(approx)

        if cor==3: objtype='triangle'
        elif cor==4: objtype='rectangle'
        elif cor==5: objtype ='pentagon '
        elif cor==6: objtype ='hexagon'
        else: 
           objtype='circle'

        x, y, w, h = cv.boundingRect(approx)

      #   cv.rectangle(background, (x-5, y-5), (x+w+5, y+h+5), (0, 255, 0), 2)
        draw_border(background,(x-5, y-5),(x+w+5, y+h+5),(0, 255, 0), 2)

        cv.putText(background, objtype, (x,y-10),cv.FONT_HERSHEY_SIMPLEX,0.5,(0,0,0))


# draw Contours :
# cv.imshow('contours drawn', blank)
cv.imshow('contours', background)


cv.waitKey(0)
