import cv2
import imutils
import numpy as np
from imutils import contours
from imutils.perspective import four_point_transform

image = cv2.imread("1.jpg")
image = imutils.resize(image, height=700)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
edged = cv2.Canny(blurred, 50, 200, 255)
cnts = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL,
	cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
cnts = sorted(cnts, key=cv2.contourArea, reverse=True)
for c in cnts:
	# approximate the contour
	peri = cv2.arcLength(c, True)
	approx = cv2.approxPolyDP(c, 0.02 * peri, True)
 
	# if the contour has four vertices, then we have found
	# the thermostat display
	if len(approx) == 4:
		displayCnt = approx
		break
warped = four_point_transform(gray, displayCnt.reshape(4, 2))
output = four_point_transform(image, displayCnt.reshape(4, 2))
# thresh = cv2.threshold(warped, 0, 255,
# 	cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
blurred = cv2.GaussianBlur(warped, (5 , 5), 0)
edged = cv2.Canny(blurred, 50, 200, 255)
kernel = np.ones((1,15),np.uint8)
dilation = cv2.dilate(edged,kernel,iterations = 1)
# thresh = cv2.morphologyEx(edged, cv2.MORPH_OPEN, dilation)
# kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (1, 5))
# thresh = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)
cv2.imshow("output2", edged)
cv2.imshow("dilation", dilation)
# find contours in the thresholded image, then initialize the
# digit contours lists
# cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
# 	cv2.CHAIN_APPROX_SIMPLE)
# cnts = imutils.grab_contours(cnts)
# for cnt in cnts :
#         x, y, w, h = cv2.boundingRect(cnt)
#         cv2.rectangle(thresh,(x,y),(x+w,y+h),(0,0,255),2)
# cv2.drawContours(thresh,cnts,-1,(0,255,0),2)
contourmask,contours,hierarchy = cv2.findContours(dilation,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
#Draw contour on image
for cnt in contours :
	x, y, w, h = cv2.boundingRect(cnt)
	cv2.rectangle(output,(x,y),(x+w,y+h),(0,0,255),2)
	if (w*h > 4000) :
		roi = output[y:y+h, x:x+w]
		cv2.imwrite( str(w*h) + ".png" , roi)
# cv2.drawContours(output,contours,-1,(0,255,0),2)
cv2.imshow('img' , output)
cv2.waitKey(0)

