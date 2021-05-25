# Référence - Exemple de code du K-Means tel que fourni par OpenCV :
# https://docs.opencv.org/master/d1/d5c/tutorial_py_kmeans_opencv.html
import numpy as np
import cv2
from dev.DAO import DAO

class ColorRecognition():
    def run(self, sentImg):
        dao = DAO()
        masks = dao.getAllMasks()

        lower_blue = np.array(masks[0][1])
        upper_blue = np.array(masks[0][2])
        lower_yellow = np.array(masks[1][1])
        upper_yellow = np.array(masks[1][2])
        lower_green = np.array(masks[2][1])
        upper_green = np.array(masks[2][2])
        lower_orange = np.array(masks[3][1])
        upper_orange = np.array(masks[3][2])
        lower_red = np.array(masks[4][1])
        upper_red = np.array(masks[4][2])
        lower_pink = np.array(masks[5][1])
        upper_pink = np.array(masks[5][2])

        img = sentImg

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

        criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 20, 1.0)
        k = 2

        attempts = 20
        ret,label,center=cv2.kmeans(Z,k,None,criteria,attempts,cv2.KMEANS_PP_CENTERS)

        center = np.uint8(center)
        center = center.tolist()
        center = center[1]
        return center
