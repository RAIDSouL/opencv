import cv2
import imutils
import numpy as np
import tempfile
import subprocess
from imutils import contours
from imutils.perspective import four_point_transform

def text_from_image_file(image_name,lang):
    output_name = "OutputImg"
    return_code = subprocess.call(['tesseract',image_name,output_name,'-l',lang,'-c','preserve_interword_spaces=1 --tessdata-dir ./tessdata_best/'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    d = open(output_name+'.txt','r',encoding='utf-8')
    return d.read()

def showpic(name):
    cv2.imshow( "name" , name )

def main() :
    # BLACK = [0,0,0]
    image = cv2.imread("1.jpg")
    # image = cv2.copyMakeBorder(image,10,10,10,10,cv2.BORDER_CONSTANT,value=BLACK)
    image = imutils.resize(image, height=500)
    # showpic(image)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gamma = 3
    lookUpTable = np.empty((1,256), np.uint8)
    for i in range(256):
        lookUpTable[0,i] = np.clip(pow(i / 255.0, gamma) * 255.0, 0, 255)
    res = cv2.LUT(gray, lookUpTable)
    cv2.imshow("res", res)
    blurred = cv2.GaussianBlur(res, (5 , 5), 0)
    edged = cv2.Canny(blurred, 50, 200, 255)
    # cv2.imshow("edged" , edged)
    kernel = np.ones((2,8),np.uint8)
    dilation = cv2.dilate(edged,kernel,iterations = 1)
    cv2.imshow("dialation" , dilation)
    # closing = cv2.morphologyEx(edged, cv2.MORPH_CLOSE, kernel)
    kernel2 = np.ones((5,1),np.uint8)
    erosion = cv2.erode(dilation,kernel2,iterations = 1)
    kernel3 = np.ones((7,1),np.uint8)
    dilation2 = cv2.dilate(erosion,kernel3,iterations = 1)
    cv2.imshow("dilation2", dilation2)
    cv2.imshow("erosion", erosion)
    contourmask,contours,hierarchy = cv2.findContours(dilation2,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
    contours = sorted(contours, key=cv2.contourArea, reverse=True)
# with open("test.txt","w") as f:
    for cnt in contours[1:] :
        x, y, w, h = cv2.boundingRect(cnt)
        if w > h :
            # if (h / w < 0.7 ) :
                cv2.rectangle(image,(x,y),(x+w,y+h),(0,0,255),2)
        # if w*h > 4000 :
        #     roi = image[y:y+h, x:x+w]
        #     cv2.imwrite( str(w*h) + ".png" , roi)
        #     f.write(text_from_image_file( str(w*h) + ".png",'tha'))
# f = open('test.txt')
    # str1 = "หลังอาหาร"
    # str2 = "เช้า"
    # str3 = "กลางวัน"
    # str4 = "เย็น"
    # line = f.readline()
    # while line:
    #     if(line.find(str1) > 0):
    #         print ('หลังอาหาร')
    #         if(line.find(str2) >0):
    #             print('เช้า')
    #         if(line.find(str3) >0):
    #             print('กลางวัน')
    #         if(line.find(str4) >0):
    #             print('เย็น')
    #     line = f.readline()
    cv2.imshow('img' , image)
    cv2.waitKey(0)
main()