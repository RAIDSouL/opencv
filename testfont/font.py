import cv2
import numpy as np
from PIL import Image
from pytesseract import image_to_string

img = cv2.imread('1.jpg')
text = image_to_string(img,lang='eng')
print(text)

