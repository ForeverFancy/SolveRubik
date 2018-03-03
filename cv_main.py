import cv2 as cv
import time
import cv_dc
import numpy as np
import subprocess

lower_yellow=np.array([26,43,46])
upper_yellow=np.array([34,255,255])

lower_red=np.array([0,43,46])
upper_red=np.array([2,255,255])

lower_orange=np.array([3,43,46])
upper_orange=np.array([12,255,255])

lower_blue=np.array([105,43,46])
upper_blue=np.array([124,255,255])

lower_green=np.array([35,43,46])
upper_green=np.array([80,255,255])

lower_white=np.array([0,0,172])
upper_white=np.array([180,42,220])

color=[[lower_white,upper_white],[lower_red,upper_red],[lower_orange,upper_orange],[lower_yellow,upper_yellow],[lower_blue,upper_blue],[lower_green,upper_green]]
colorname=['W','R','O','Y','B','G']



num=1

while True:
    cap = cv.VideoCapture(1)
    print('%d-------------------------------' % num)
    ret,frame=cap.read()
    time.sleep(5)
    path='D:/'+str(num)+'.jpg'
    newimg = frame[220:420, 220:420]
    cv.imwrite(path,newimg)
    cv_dc.discrimination(path,color,colorname)
    cap.release()
    num+=1
    if num==7:
        break


subprocess.call("源.exe")