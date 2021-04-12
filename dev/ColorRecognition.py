import numpy as np
import cv2


lower_blue = np.array([91, 90, 50])
upper_blue = np.array([102, 255, 128])
lower_yellow = np.array([18, 119, 116])
upper_yellow = np.array([23, 193, 225])
lower_green = np.array([49, 148, 48])
upper_green = np.array([70, 255, 156])
lower_orange = np.array([0, 177, 96])
upper_orange = np.array([179, 255, 255])
lower_red = np.array([173, 192, 71])
upper_red = np.array([179, 255, 152])
lower_pink = np.array([163, 145, 108])
upper_pink = np.array([168, 255, 217])

img = cv2.imread('img/crayorescent_202141_1441204.jpg')

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
#kernel = np.ones((3,3),np.uint8)
#opening = cv2.morphologyEx(img,cv2.MORPH_OPEN,kernel)
Z = img.reshape((-1,3))
Z = np.float32(Z)

# define criteria, number of clusters(K) and apply kmeans()
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 20, 1.0)
k = 7

attempts = 20
ret,label,center=cv2.kmeans(Z,k,None,criteria,attempts,cv2.KMEANS_PP_CENTERS)

# Now convert back into uint8, and make original image
center = np.uint8(center)
print(center)
res = center[label.flatten()]
res2 = res.reshape((img.shape))

cv2.imshow('res2', res2)
cv2.waitKey(0)
cv2.destroyAllWindows()
