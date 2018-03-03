import cv2 as cv
import numpy as np

def colordiscrimination(img,color,colorname):
    max=0
    y=0
    count=0
    newimg = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    for i in color:
        mask = cv.inRange(newimg, i[0], i[1])
        doingimg=cv.bitwise_and(img,img,mask=mask)
        final=cv.cvtColor(doingimg,cv.COLOR_BGR2GRAY)
        k=cv.countNonZero(final)
        if k>max:
            max=k
            y=count
        count=count+1
    return colorname[y]
