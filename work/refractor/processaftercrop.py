import cv2
import imutils
import numpy as np
import tempfile
import subprocess
from imutils import contours
from imutils.perspective import four_point_transform

def text_from_image_file(image_name,lang):
    output_name = "OutputImg"
    os.system('tesseract {} {} -l {} -c preserve_interword_spaces=1 --tessdata-dir ./tessdata_best/'.format(image_name,output_name, lang))
    d = open(output_name+'.txt','r',encoding='utf-8')
    return d.read()

def showpic(name):
    cv2.imshow( "name" , name )

def main() :
    image = cv2.imread("3.png")
    image = imutils.resize(image, height=700)
    showpic(image)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gamma = 3
    lookUpTable = np.empty((1,256), np.uint8)
    for i in range(256):
        lookUpTable[0,i] = np.clip(pow(i / 255.0, gamma) * 255.0, 0, 255)
    res = cv2.LUT(gray, lookUpTable)
    blurred = cv2.GaussianBlur(res, (5 , 5), 0)
    edged = cv2.Canny(blurred, 50, 200, 255)
    cv2.imshow("edged" , edged)
    kernel = np.ones((2,30),np.uint8)
    dilation = cv2.dilate(edged,kernel,iterations = 1)
    # cv2.imshow("dialation" , dilation)
    # cv2.imshow("output2", edged)
    # cv2.imshow("dilation", dilation)
    contourmask,contours,hierarchy = cv2.findContours(dilation,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
    with open("test.txt","w") as f:
        for cnt in contours :
            x, y, w, h = cv2.boundingRect(cnt)
            cv2.rectangle(image,(x,y),(x+w,y+h),(0,0,255),2)
            # if w * h > 4000 :
            #     cv2.imshow("dialation" , dilation)
            if w*h > 4000 :
                str1 = "หลังอาหาร"
                str2 = "เช้า"
                str3 = "กลางวัน"
                str4 = "เย็น"
                roi = image[y:y+h, x:x+w]
                cv2.imwrite( str(w*h) + ".png" , roi)
                f.write(text_from_image_file( str(w*h) + ".png",'tha'))
    f = open('test.txt')
    line = f.readline()
    while line:
        if(line.find(str1) > 0):
            print ('หลังอาหาร')
            if(line.find(str2) >0):
                print('เช้า')
            if(line.find(str3) >0):
                print('กลางวัน')
            if(line.find(str4) >0):
                print('เย็น')
        line = f.readline()
    cv2.imshow('img' , image)
    cv2.waitKey(0)
main()