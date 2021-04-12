import numpy as np
import cv2

cap = cv2.VideoCapture(1, cv2.CAP_DSHOW)

def empty(a):
    pass

cv2.namedWindow("HSV")
cv2.resizeWindow("HSV", 640, 240)
cv2.createTrackbar("Hue min", "HSV", 0, 179, empty)
cv2.createTrackbar("Hue max", "HSV", 179, 179, empty)
cv2.createTrackbar("Sat min", "HSV", 0, 255, empty)
cv2.createTrackbar("Sat max", "HSV", 255, 255, empty)
cv2.createTrackbar("Value min", "HSV", 0, 255, empty)
cv2.createTrackbar("Value max", "HSV", 255, 255, empty)

while True:
    _, img = cap.read()
    imghsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    #image_blur_gray = cv2.cvtColor(image_blur, cv2.COLOR_BGR2GRAY)

    #image_res ,image_thresh = cv2.threshold(image_blur_gray,156,255,cv2.THRESH_BINARY_INV)


    h_min = cv2.getTrackbarPos("Hue min", "HSV")
    h_max = cv2.getTrackbarPos("Hue max", "HSV")
    s_min = cv2.getTrackbarPos("Sat min", "HSV")
    s_max = cv2.getTrackbarPos("Sat max", "HSV")
    v_min = cv2.getTrackbarPos("Value min", "HSV")
    v_max = cv2.getTrackbarPos("Value max", "HSV")
    print(h_min)

    lower_red = np.array([h_min, s_min, v_min])
    upper_red = np.array([h_max, s_max, v_max])

    mask = cv2.inRange(imghsv, lower_red, upper_red)
    res = cv2.bitwise_and(img,img,mask = mask)

    cv2.imshow('res', img)
    #cv2.imshow('res2', imghsv)
    cv2.imshow("Mask", mask)
    cv2.imshow("res3", res)
    if cv2.waitKey(1)& 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
