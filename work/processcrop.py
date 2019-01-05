import cv2
import imutils
import numpy as np
from imutils import contours
from imutils.perspective import four_point_transform

image = cv2.imread("2.jpg")
image = imutils.resize(image, height=700)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5 , 5), 0)
edged = cv2.Canny(blurred, 50, 200, 255)
cv2.imshow("edged" , edged)
kernel = np.ones((2,30),np.uint8)
dilation = cv2.dilate(edged,kernel,iterations = 1)
cv2.imshow("dialation" , dilation)
cv2.imshow("output2", edged)
cv2.imshow("dilation", dilation)
contourmask,contours,hierarchy = cv2.findContours(dilation,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
for cnt in contours :
	x, y, w, h = cv2.boundingRect(cnt)
	cv2.rectangle(image,(x,y),(x+w,y+h),(0,0,255),2)
	#   if (w*h > 4000) :
	# 	roi = output[y:y+h, x:x+w]
	# 	cv2.imwrite( str(w*h) + ".png" , roi)
cv2.imshow('img' , image)
cv2.waitKey(0)