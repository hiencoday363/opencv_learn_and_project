import cv2 as cv

##################
noPlateCascade = cv.CascadeClassifier('./haarcascade_russian_plate_number.xml')
##################

capture = cv.VideoCapture(0)
# set width, height
capture.set(3, 360)
capture.set(4, 460)

while True:
    isTrue, frame = capture.read()

    img_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    numberPlate = noPlateCascade.detectMultiScale(img_gray, 1.1, 4)

    for (x, y, w, h) in numberPlate:
        # tinh dien tich
        area = w * h
        if area > 500:
            cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), thickness=2)

            img_roi = frame[y:y+h, x:x+w]
            cv.imshow('Roi Image', img_roi)

            # put text
            cv.putText(frame, 'number plate', (x, y - 5), cv.FONT_HERSHEY_COMPLEX, 0.7, (0, 0, 255), 2)

    cv.imshow('Result', frame)
    if cv.waitKey(1) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()
