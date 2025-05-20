from PIL import Image
import tkinter as tk
from tkinter import filedialog
import cv2
import os
import shutil
import pywt
import numpy as np


def getLocalFile():
    root=tk.Tk()
    root.withdraw()
    filePath=filedialog.askopenfilename()
    return filePath

def guassi(filePath):
    f = cv2.imread(filePath)
    image_3_LF = cv2.GaussianBlur(f, (11,11), 0)  # (3,3)为高斯半径,image_3_LF为高斯滤波后的低分图像
    cv2.imwrite("D:/DWT/attack/guassi_LF_image.png", image_3_LF)
    print("guassi end!")



def shape(filePath):
    img = cv2.imread(filePath)
    rows, cols = img.shape[:2]
    M1 = cv2.getRotationMatrix2D((cols / 2, rows / 2), 0.2, 1) # 第一个参数是旋转中心，第二个参数是旋转角度，第三个参数是缩放比例
    res2 = cv2.warpAffine(img, M1, (cols, rows))
    cv2.imwrite('D:/DWT/attack/旋转.png', res2)
    print("shape end!")




if __name__ == '__main__':
    path = 'D:/DWT/attack'

    if os.path.exists(path):
        shutil.rmtree(path)
        print('shutil success!')
        os.mkdir(path)

    else:
        print('mkdir success!')
        os.mkdir(path)

    path = getLocalFile()
    guassi(path)
    shape(path)
