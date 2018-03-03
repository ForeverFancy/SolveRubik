import cv2 as cv
import numpy as np
import cv_VALK3

def discrimination(path,color,colorname):
    img=cv.imread(path)             #读取图片
    (h, w, k) = img.shape
    h = int(1 * h / 3)
    w = int(1 * w / 3)

    g1 = img[0:h, 0:w]
    g6 = img[h:2 * h, 2 * w:3 * w]
    g7 = img[2 * h:3 * h, 0:w]
    g3 = img[0:h, 2 * w:3 * w]
    g9 = img[2 * h:3 * h, 2 * w:3 * w]
    g2 = img[0:h, w:2 * w]
    g8 = img[2 * h:3 * h, w:2 * w]
    g4 = img[h:2 * h, 0:w]
    g5 = img[h:2 * h, w:2 * w]

    t=0
    listimg=[g1,g2,g3,g4,g5,g6,g7,g8,g9]
    f = open('CUBE_STATE.txt', 'a')
    for member in listimg:
        f.write(cv_VALK3.colordiscrimination(member,color,colorname))    #写入
        t+=1
        if t==3:
            f.write('\n')                                           #换行
            t=0
