import cv2
import imutils
import numpy as np
from imutils import contours
from imutils.perspective import four_point_transform

def Img_crop():
    image = cv2.imread("2.png")
    image = imutils.resize(image, height=700)
    height, width , channel= image.shape
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imshow("gray" ,gray)
    gamma = 3
    lookUpTable = np.empty((1,256), np.uint8)
    for i in range(256):
        lookUpTable[0,i] = np.clip(pow(i / 255.0, gamma) * 255.0, 0, 255)
    res = cv2.LUT(gray, lookUpTable)
    cv2.imshow("gray2",res)
    blurred = cv2.GaussianBlur(res, (5, 5), 0)
    edged = cv2.Canny(blurred, 50, 200, 255)
    cv2.imshow("edged" , edged)
    cnts = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    cnts = sorted(cnts, key=cv2.contourArea, reverse=True)
    temp_c = cnts[0]
    find_max = 0
    for c in cnts:
        x, y, w, h = cv2.boundingRect(c)
    #     if w * h > find_max :
    #         temp_c = c
    # x, y, w, h = cv2.boundingRect(temp_c)
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.02 * peri, True)
    
        # if the contour has four vertices, then we have found
        # the thermostat display
        if len(approx) == 4:
            displayCnt = approx
            break
    warped = four_point_transform(gray, displayCnt.reshape(4, 2))
    output = four_point_transform(image, displayCnt.reshape(4, 2))
    cv2.imshow("warped", warped)
    cv2.imshow("img" ,output)
    # approximate the contour
    # warped = four_point_transform(gray, displayCnt.reshape(4, 2))
    # output = four_point_transform(image, displayCnt.reshape(4, 2))
    cv2.imshow("pic", image)
    
    cv2.waitKey(0)

Img_crop()