#!/usr/bin/python

import cv2
import numpy as np
import os
from PIL import Image
from pytesseract import image_to_string

img = Image.open('E:\\OPENCVGITHUB\\opencv\\testfont\\1.jpg')
text = image_to_string(img)
print(text)