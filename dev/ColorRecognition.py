import numpy as np
import cv2

#img = cv2.imread('img/crayorescent_202141_025597.jpg')
#image_blur = cv2.medianBlur(img,25)
# cap = cv2.VideoCapture(1, cv2.CAP_DSHOW)
#
# def empty(a):
#     pass
#
# cv2.namedWindow("HSV")
# cv2.resizeWindow("HSV", 640, 240)
# cv2.createTrackbar("Hue min", "HSV", 0, 179, empty)
# cv2.createTrackbar("Hue max", "HSV", 179, 179, empty)
# cv2.createTrackbar("Sat min", "HSV", 0, 255, empty)
# cv2.createTrackbar("Sat max", "HSV", 255, 255, empty)
# cv2.createTrackbar("Value min", "HSV", 0, 255, empty)
# cv2.createTrackbar("Value max", "HSV", 255, 255, empty)
#
# while True:
#     _, img = cap.read()
#     imghsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
#
#     hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
#     #image_blur_gray = cv2.cvtColor(image_blur, cv2.COLOR_BGR2GRAY)
#
#     #image_res ,image_thresh = cv2.threshold(image_blur_gray,156,255,cv2.THRESH_BINARY_INV)
#
#
#     h_min = cv2.getTrackbarPos("Hue min", "HSV")
#     h_max = cv2.getTrackbarPos("Hue max", "HSV")
#     s_min = cv2.getTrackbarPos("Sat min", "HSV")
#     s_max = cv2.getTrackbarPos("Sat max", "HSV")
#     v_min = cv2.getTrackbarPos("Value min", "HSV")
#     v_max = cv2.getTrackbarPos("Value max", "HSV")
#     print(h_min)
#
#     lower_red = np.array([h_min, s_min, v_min])
#     upper_red = np.array([h_max, s_max, v_max])
#
#     mask = cv2.inRange(imghsv, lower_red, upper_red)
#     res = cv2.bitwise_and(img,img,mask = mask)
#
#     cv2.imshow('res', img)
#     #cv2.imshow('res2', imghsv)
#     cv2.imshow("Mask", mask)
#     cv2.imshow("res3", res)
#     if cv2.waitKey(1)& 0xFF == ord('q'):
#         break
# cap.release()
# cv2.destroyAllWindows()


lower_blue = np.array([89, 45, 46])
upper_blue = np.array([102, 255, 154])
lower_yellow = np.array([18, 52, 116])
upper_yellow = np.array([23, 193, 243])
lower_green = np.array([49, 148, 48])
upper_green = np.array([70, 255, 156])
lower_orange = np.array([172, 177, 148])
upper_orange = np.array([179, 255, 241])
lower_red = np.array([173, 192, 71])
upper_red = np.array([179, 255, 152])
lower_pink = np.array([163, 145, 108])
upper_pink = np.array([168, 255, 217])

img = cv2.imread('img/crayorescent_202141_025597.jpg')
#imghsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)
mask_yellow = cv2.inRange(hsv, lower_yellow, upper_yellow)
mask_green = cv2.inRange(hsv, lower_green, upper_green)
mask_orange = cv2.inRange(hsv, lower_orange, upper_orange)
mask_red = cv2.inRange(hsv, lower_red, upper_red)
mask_pink = cv2.inRange(hsv, lower_pink, upper_pink)
image_res ,image_thresh_blue = cv2.threshold(mask_blue,1,255,cv2.THRESH_BINARY_INV)
image_res ,image_thresh_yellow = cv2.threshold(mask_yellow,1,255,cv2.THRESH_BINARY_INV)
image_res ,image_thresh_green = cv2.threshold(mask_green,1,255,cv2.THRESH_BINARY_INV)
image_res ,image_thresh_orange = cv2.threshold(mask_orange,1,255,cv2.THRESH_BINARY_INV)
image_res ,image_thresh_red = cv2.threshold(mask_red,1,255,cv2.THRESH_BINARY_INV)
image_res ,image_thresh_pink = cv2.threshold(mask_pink,1,255,cv2.THRESH_BINARY_INV)
img1 = cv2.bitwise_and(image_thresh_blue, image_thresh_blue, mask = image_thresh_orange)
img2 = cv2.bitwise_and(img1, img1, mask = image_thresh_red)
img3 = cv2.bitwise_and(img2, img2, mask = image_thresh_yellow)
img4 = cv2.bitwise_and(img3, img3, mask = image_thresh_green)
img5 = cv2.bitwise_and(img4, img4, mask = image_thresh_pink)
image_res ,image_thresh_all = cv2.threshold(img5,1,255,cv2.THRESH_BINARY_INV)


img = cv2.bitwise_and(img, img, mask = image_thresh_all)

Z = img.reshape((-1,3))
Z = np.float32(Z)

# define criteria, number of clusters(K) and apply kmeans()
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
k = 7

attemps = 10
ret,label,center=cv2.kmeans(Z,k,None,criteria,attemps,cv2.KMEANS_PP_CENTERS)

# Now convert back into uint8, and make original image
center = np.uint8(center)
print(center)
res = center[label.flatten()]
res2 = res.reshape((img.shape))

cv2.imshow('res2', res2)
cv2.waitKey(0)
cv2.destroyAllWindows()