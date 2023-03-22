import cv2
import time

cap = cv2.VideoCapture('C:/Users/dasan/OneDrive//Escritorio/ИТМО/2-ой курс/4-ый семестр/Дизайн вещей будущего/sample.mp4')

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2. GaussianBlur(gray, (21, 21), 0)

    ret, thresh = cv2.threshold(gray, 105, 255, cv2.THRESH_BINARY_INV)

    contours, hirearchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    if len(contours) > 0:
        c = max(contours, key = cv2.contourArea)
        x, y, w, h = cv2.boundingRect(c)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        new_y = (y + (y + h)) // 2
        new_x = (x + (x + h)) // 2
        cv2.line(frame, (x, new_y), (x + h, new_y), (255, 0, 0), 2)
        cv2.line(frame, (new_x, y), (new_x, y + h), (255, 0, 0), 2)
    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    time.sleep(0.1)
cap.release()
cv2.destroyAllWindows()