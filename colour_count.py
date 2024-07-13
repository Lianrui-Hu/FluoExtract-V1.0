#!/usr/bin/env python

# Install OpenCV and numpy
# $ pip install opencv-python numpy

import cv2
import numpy as np
import os

def color_count(image_name):
    rgb_image = cv2.imread(image_name)
    hsv = cv2.cvtColor(rgb_image, cv2.COLOR_BGR2HSV)
    # minimum value of Yellow pixel in HSV order -> Yellow
    Yellow_MIN = np.array([11, 43, 35], np.uint8)
    # maximum value of Yellow pixel in HSV order -> Yellow
    Yellow_MAX = np.array([77, 255, 255], np.uint8)

    # minimum value of Blue pixel in HSV order -> Blue
    Blue_MIN = np.array([78, 0, 35], np.uint8)
    # maximum value of Blue pixel in HSV order -> Blue
    Blue_MAX = np.array([124, 255, 255], np.uint8)

    Yellow_dst = cv2.inRange(hsv,lowerb=Yellow_MIN,upperb=Yellow_MAX)
    no_Yellow = cv2.countNonZero(Yellow_dst)

    Blue_dst = cv2.inRange(hsv,lowerb=Blue_MIN,upperb=Blue_MAX)
    no_Blue = cv2.countNonZero(Blue_dst)
    color_rato = no_Yellow/no_Blue
    print('The number of Yellow pixels is: ' + str(no_Yellow))
    print('The number of Blue pixels is: ' + str(no_Blue))
    print('The number of Yellow pixels is: ' + str(color_rato))

    rgb_image_show = cv2.resize(rgb_image, (615, 685))
    Yellow_dst_show = cv2.resize(Yellow_dst, (615, 685))
    Blue_dst_show = cv2.resize(Blue_dst, (615, 685))

    cv2.namedWindow("Origin")
    cv2.imshow("Origin",rgb_image_show)
    cv2.namedWindow("Yellow")
    cv2.imshow("Yellow",Yellow_dst_show)
    cv2.namedWindow("Blue")
    cv2.imshow("Blue",Blue_dst_show)
    cv2.waitKey(0)
    return


path = "Path-to-Picturefiles"
files= os.listdir(path)
for file in files:
    f = path + "/" + file
    print(file)
    color_count(f)
    
    
# vim: ft=python ts=4 sw=4 expandtab
