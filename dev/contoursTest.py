import numpy as np
import cv2 as cv
im = cv.imread('img/crayorescent_2021331_174175.jpg')
imgray = cv.cvtColor(im, cv.COLOR_BGR2GRAY)
ret, thresh = cv.threshold(imgray, 127, 255, 0)
contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
im = cv.drawContours(im, contours, -1, (0,255,0), 3)
cv.imshow('res2', im)
cv.waitKey(0)
cv.destroyAllWindows()