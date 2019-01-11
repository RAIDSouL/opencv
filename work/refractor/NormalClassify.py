import cv2
import sys
import imutils
import numpy as np
import subprocess
from imutils import contours
from imutils.perspective import four_point_transform

def text_from_image_file(image_name,lang):
    output_name = "OutputImg"
    return_code = subprocess.call(['tesseract',image_name,output_name,'-l',lang,'-c','preserve_interword_spaces=1 --tessdata-dir ./tessdata_best/'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    d = open(output_name+'.txt','r',encoding='utf-8')
    return d.read()

def More_Gray(gamma,image) : #make picture more clearly
    gamma1 = gamma
    lookUpTable = np.empty((1,256), np.uint8)
    for i in range(256):
        lookUpTable[0,i] = np.clip(pow(i / 255.0, gamma1) * 255.0, 0, 255)
    res = cv2.LUT(image, lookUpTable)
    return res

def Spell_checker(name):
    f = open(name , '.txt')
        str0 = "ก่อนอาหาร"
        str1 = "หลังอาหาร"
        str2 = "เช้า"
        str3 = "กลางวัน"
        str4 = "เย็น"
        line = f.readline()
    while line:
        if(line.find(str0) > 0):
            print ('หลังอาหาร')
            if(line.find(str2) >0):
                print('เช้า')
            if(line.find(str3) >0):
                print('กลางวัน')
            if(line.find(str4) >0):
                print('เย็น')
        if(line.find(str1) > 0):
            print ('หลังอาหาร')
            if(line.find(str2) >0):
                print('เช้า')
            if(line.find(str3) >0):
                print('กลางวัน')
            if(line.find(str4) >0):
                print('เย็น')
        line = f.readline()
    

def main(argv) :
    image = cv2.imread(argv[0]) 
    image = imutils.resize(image, height=500)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Gray", gray)
    gray = More_Gray(3,gray) #make picture more clear
    cv2.imshow("MGray", gray)




    fname = argv[0].split(".")[0]
    Spell_checker(fname)



main(sys.argv[1:])
cv2.waitKey(0)