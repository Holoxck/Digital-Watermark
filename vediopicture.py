import sys
import time
import cv2
import pywt
import numpy as np
from PIL import Image
import os
import shutil
import pywt
import numpy as np
import math
import random
import tkinter as tk
from tkinter import filedialog
from PySide6.QtWidgets import QLabel, QHBoxLayout, QWidget, QApplication, QMainWindow, QDialog, QComboBox, QMessageBox
from PySide6.QtGui import QPixmap, QImage
from PySide6.QtCore import QDateTime, QTimer, SIGNAL, QObject
from ui_mainwin1 import Ui_mainWindow
from ui_childwin1 import Ui_dialog1
from ui_childwin3 import Ui_dialog

global filePath_zaiti
filePath_zaiti = 0
global filePath_shuiyin
filePath_shuiyin = 0
global filePath_get
filePath_get = 0
global filePath_shipin
filePath_shipin = 0


def getLocalFilezaiti():
    global filePath_zaiti
    root = tk.Tk()
    root.withdraw()
    filePath_zaiti = filedialog.askopenfilename()
    #print(filePath_zaiti)

def getLocalFileshuiyin():
    global filePath_shuiyin
    root = tk.Tk()
    root.withdraw()
    filePath_shuiyin = filedialog.askopenfilename()
    #print(filePath_shuiyin)

def getLocalFileget():
    global filePath_get
    root = tk.Tk()
    root.withdraw()
    filePath_get = filedialog.askopenfilename()
    #print(filePath_get)

def getLocalFileshipin():
    global filePath_shipin
    root = tk.Tk()
    root.withdraw()
    filePath_shipin = filedialog.askopenfilename()
    #print(filePath_get)

def childshow():
    child = ChildWindow()
    child.show()  # 显示窗口
    child.exec()  # 避免程序执行到这一行后直接退出

def childshow1():
    child1 = ChildWindow1()
    child1.show()  # 显示窗口
    child1.exec()  # 避免程序执行到这一行后直接退出

def getLocalFile():
    root=tk.Tk()
    root.withdraw()
    filePath=filedialog.askopenfilename()
    return filePath

def plus(str):
    return str.zfill(8)
# 获取水印图片的每一个像素值,i：指定要检查的像素点的逻辑X轴坐标。j：指定要检查的像素点的逻辑Y轴坐标。

#lsb图片获取像素
def getcode(watermark):
    str1 = ""
    for i in range(watermark.size[0]):
        for j in range(watermark.size[1]):
            # 获取每个像素的RGB值
            rgb = watermark.getpixel((i, j))
            str1 = str1 + plus(bin(rgb[0]).replace('0b', ''))
            str1 = str1 + plus(bin(rgb[1]).replace('0b', ''))
            str1 = str1 + plus(bin(rgb[2]).replace('0b', ''))
    #print(str1)
    return str1


# 加密  lsb图片嵌入
def encry1(img, code):
    # 计数器
    count = 0
    codelen = len(code)
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            # 获取每个像素的RGB值
            data = img.getpixel((i, j))
            if count == codelen:
                break
            r = data[0]
            g = data[1]
            b = data[2]
            r = (r - r % 2) + int(code[count])
            count += 1
            if count == codelen:
                img.putpixel((i, j), (r, g, b))
                break

            g = (g - g % 2) + int(code[count])
            count += 1
            if count == codelen:
                img.putpixel((i, j), (r, g, b))
                break

            b = (b - b % 2) + int(code[count])
            count += 1
            if count == codelen:
                img.putpixel((i, j), (r, g, b))
                break
                # 每3次循环表示一组RGB值被替换完毕，可以进行写入
            if count % 3 == 0:
                img.putpixel((i, j), (r, g, b))
    img.save('get.bmp')
    img.save('D:\\1\\get.bmp')

#lsb图片解密
def deEncry(img, length, im):
    width = im.size[0]
    height = im.size[1]
    # 计数器
    count = 0
    wt = ""

    for i in range(width):
        for j in range(height):
            # 获取像素点的值
            rgb = img.getpixel((i, j))
            # 提取R通道的附加值
            if count % 3 == 0:
                count += 1
                wt = wt + str(rgb[0] % 2)
                if count == length:
                    break

                    # 提取G通道的附加值
            if count % 3 == 1:
                count += 1
                wt = wt + str(rgb[1] % 2)
                if count == length:
                    break

                    # 提取B通道的附加值
            if count % 3 == 2:
                count += 1
                wt = wt + str(rgb[2] % 2)
                if count == length:
                    break
        if count == length:
            break
    return wt

#lsb嵌入后的图片保存
def showImage(wt,length_a,width_b):
    # str2初始化为list
    str2 = []
    # 将wt的值转变为RGB值
    for i in range(0, len(wt), 8):
        # 以每8位为一组二进制，转换为十进制
        str2.append(int(wt[i:i + 8], 2))
    # 绘制和显示水印图片
    img_out = Image.new("RGB", (length_a, width_b))
    flag = 0
    for m in range(0, length_a):
        for n in range(0, width_b):
            img_out.putpixel((m, n), (str2[flag], str2[flag + 1], str2[flag + 2]))
            flag += 3
    img_out.save("ok.png")
    #img_out.show()
    #cv2.imwrite('out.png',img_out)



def getMSE(Value1, Value2, cols, rows):
    mse = 0
    for x in range(0,cols):
        for y in range(0,rows):
            mse = mse+(int(Value1[x][y])-int(Value2[x][y]))*(int(Value1[x][y])-int(Value2[x][y]))
    MSE = (1 / (rows * cols))*mse
    #print('MES = %f',float(MSE))
    return MSE

def getPSNR(cols, rows, MSE):
    PSNR = 10*math.log((255*255/MSE),10)
    return PSNR

def getNC(Value1, Value2, cols, rows):
    nc1 = 0
    nc2 = 0
    for x in range(0,cols):
        for y in range(0,rows):
            nc1 = nc1+(int(Value1[x][y])*int(Value2[x][y]))
            nc2 = nc2+(int(Value1[x][y])*int(Value1[x][y]))
    NC = nc1/nc2
    return NC

def setwaterMark1(waterImg, Img, i, d1):
    # 载体图像三级小波变换
    c = pywt.wavedec2(Img, 'db2', level=3)
    [cl, (cH3, cV3, cD3), (cH2, cV2, cD2), (cH1, cV1, cD1)] = c
    d = pywt.wavedec2(waterImg, 'db2', level=1)
    [ca1, (ch1, cv1, cd1)] = d
    # print(cl.shape,len(cH3),len(cH2),len(cH1),Img.shape)
    # 自定义嵌入系数
    a1 = 1.5 * d1
    a2 = 0.5 * d1
    a3 = 0.5 * d1
    a4 = 0.5 * d1
    # 嵌入
    cl = cl + ca1 * a1
    cH3 = cH3 + ch1 * a2
    cV3 = cV3 + cv1 * a3
    cD3 = cD3 + cd1 * a4
    # 图像重构
    newImg = pywt.waverec2([cl, (cH3, cV3, cD3), (cH2, cV2, cD2), (cH1, cV1, cD1)], 'db2')
    v = newImg
    # f = open("加入水印结果.txt", 'w')
    # f.write(str(newImg))
    # f.close()
    max = np.max(newImg) // 1 + 1
    newImg = newImg / max * 255

    z = max
    #print(max)
    newImg = np.array(newImg, np.uint8)
    #cv2.imshow("after" + str(i), newImg)
    cv2.waitKey(0)
    return newImg, z, v


def getwaterMark1(originalImage, Img, key, v, i, d1):
    # 载体图像三级小波变换
    c = pywt.wavedec2(Img, 'db2', level=3)
    [cl, (cH3, cV3, cD3), (cH2, cV2, cD2), (cH1, cV1, cD1)] = c
    # 原始图像三级小波变换
    d = pywt.wavedec2(originalImage, 'db2', level=3)
    [dl, (dH3, dV3, dD3), (dH2, dV2, dD2), (dH1, dV1, dD1)] = d
    ca1 = (cl - dl) * 2 / 3 * d1
    ch1 = (cH3 - dH3) * 2 * d1
    cv1 = (cV3 - dV3) * 2 * d1
    cd1 = (cD3 - dD3) * 2 * d1

    # 水印图像重构
    waterImg = pywt.waverec2([ca1, (ch1, cv1, cd1)], 'db2')

    # 对提取的水印图像进行逆Arnold变换
    # waterImg = deArnold(waterImg, key)

    waterImg = np.array(waterImg, np.uint8)

    # cv2.imshow("get"+str(i), waterImg)
    # cv2.imwrite(str(i)+"jeiguo.png",waterImg)
    # cv2.waitKey(0)
    return waterImg

def quanxi_setwaterMark1(waterImg, Img,i,d1):
    # 载体图像三级小波变换
    c = pywt.wavedec2(Img, 'db2', level=3)
    [cl, (cH3, cV3, cD3), (cH2, cV2, cD2), (cH1, cV1, cD1)] = c
    d = pywt.wavedec2(waterImg, 'db2', level=1)
    [ca1, (ch1, cv1, cd1)] = d
    #print(cl.shape,len(cH3),len(cH2),len(cH1),Img.shape)
    # 自定义嵌入系数
    a1 = 1*d1
    a2 = 0.5*d1
    a3 = 0.5*d1
    a4 = 0.5*d1
    # 嵌入
    cl = cl + ca1 * a1
    cH3 = cH3 + ch1 * a2
    cV3 = cV3 + cv1 * a3
    cD3 = cD3 + cd1 * a4

    # 图像重构
    newImg = pywt.waverec2([cl, (cH3, cV3, cD3), (cH2, cV2, cD2), (cH1, cV1, cD1)], 'db2')
    v=newImg
    # f = open("加入水印结果.txt", 'w')
    # f.write(str(newImg))
    # f.close()
    max = np.max(newImg)//1+1
    newImg=newImg/max*255
    z =max
    # print(max)
    newImg = np.array(newImg, np.uint8)
    #cv2.imshow("after"+str(i), newImg)
    #cv2.waitKey(0)
    return newImg,z

def quanxi_getwaterMark1(originalImage, Img, key,i,d1):
    # 载体图像三级小波变换
    c = pywt.wavedec2(Img, 'db2', level=3)
    [cl, (cH3, cV3, cD3), (cH2, cV2, cD2), (cH1, cV1, cD1)] = c
    # 原始图像三级小波变换
    d = pywt.wavedec2(originalImage, 'db2', level=3)
    [dl, (dH3, dV3, dD3), (dH2, dV2, dD2), (dH1, dV1, dD1)] = d
    # f = open("正经变换.txt", 'w')
    # f.write(str(d))
    # f.close()
    ca1 = (cl - dl) *1*d1
    ch1 = (cH3 - dH3) * 2*d1
    cv1 = (cV3 - dV3) * 2*d1
    cd1 = (cD3 - dD3) * 2*d1

    # 水印图像重构
    waterImg = pywt.waverec2([ca1, (ch1, cv1, cd1)], 'db2')

    # 对提取的水印图像进行逆Arnold变换
    # waterImg = deArnold(waterImg, key)

    waterImg = np.array(waterImg, np.uint8)

    #cv2.imshow("get"+str(i), waterImg)
    cv2.imwrite(str(i)+"jeiguo.png",waterImg)
    #cv2.waitKey(0)
    return waterImg

def ycl(g0,g1,s):
    a0 = g0[0:300, 0:600]
    a1 = g0[780:1080, 0:600]
    a2 = g0[0:300, 1320:1920]
    a3 = g0[780:1080, 1320:1920]   #载体
    s0, d0= quanxi_setwaterMark1(g1, a0, 0, s)
    s1, d1= quanxi_setwaterMark1(g1, a1, 1, s)
    s2, d2= quanxi_setwaterMark1(g1, a2, 2, s)
    s3, d3 = quanxi_setwaterMark1(g1, a3, 4, s)   #zairu
    g0[0:300, 0:600] = s0
    g0[780:1080, 0:600] = s1
    g0[0:300, 1320:1920] = s2
    g0[780:1080, 1320:1920] = s3  #fangru
    return g0,d0,d1,d2,d3

def  mtc1(a,b,c,d):
    n=np.array([a,b,c,d])
    sum = np.max(n)

    return sum

def get_video_duration(filename):
    cap = cv2.VideoCapture(filename)
    if cap.isOpened():
        rate = cap.get(5)
        frame_num = cap.get(7)
        duration = int(frame_num / rate)
        return duration
    return -1

def cut_vedio(time_vedio, shipin, count):
    START_TIME = 0  # 设置开始时间(单位秒)
    END_TIME = time_vedio  # 设置结束时间(单位秒)
    vidcap = cv2.VideoCapture(shipin)
    fps = int(vidcap.get(cv2.CAP_PROP_FPS))  # 获取视频每秒的帧数
    print(fps)
    frameToStart = START_TIME * fps  # 开始帧 = 开始时间*帧率
    print(frameToStart)
    frametoStop = END_TIME * fps  # 结束帧 = 结束时间*帧率
    print(frametoStop)
    vidcap.set(cv2.CAP_PROP_POS_FRAMES, frameToStart)  # 设置读取的位置,从第几帧开始读取视频
    print(vidcap.get(cv2.CAP_PROP_POS_FRAMES))  # 查看当前的帧数
    success, image = vidcap.read()  # 获取第一帧

    count = 1
    while success and frametoStop >= count:
        if count != 0:
            cv2.imwrite(r"D:\before\%d.png" % int(count), image)  # 保存图片
            print('Process %dth seconds: ' % int(count), success)
        success, image = vidcap.read()  # 每次读取一帧
        count += 1
    return count
    print("end!")


def getcode(watermark):
    str1 = ""
    for i in range(watermark.size[0]):
        for j in range(watermark.size[1]):
            # 获取每个像素的RGB值
            rgb = watermark.getpixel((i, j))
            str1 = str1 + plus(bin(rgb[0]).replace('0b', ''))
            str1 = str1 + plus(bin(rgb[1]).replace('0b', ''))
            str1 = str1 + plus(bin(rgb[2]).replace('0b', ''))
    # print (str)
    return str1

def encry(img, code, k):
    # 计数器
    count = 0
    codelen = len(code)
    #print(codelen)
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            # 获取每个像素的RGB值
            data = img.getpixel((i, j))
            if count == codelen:
                break
            r = data[0]
            g = data[1]
            b = data[2]
            # print (r)
            # print(codelen)#24
            r = (r - r % 2) + int(code[count])
            count += 1
            if count == codelen:
                img.putpixel((i, j), (r, g, b))
                break

            g = (g - g % 2) + int(code[count])
            count += 1
            if count == codelen:
                img.putpixel((i, j), (r, g, b))
                break

            b = (b - b % 2) + int(code[count])
            count += 1
            if count == codelen:
                img.putpixel((i, j), (r, g, b))
                break
                # 每3次循环表示一组RGB值被替换完毕，可以进行写入
            if count % 3 == 0:
                img.putpixel((i, j), (r, g, b))
    img.save('D:/after/watermark_im%d.png' % int(k))
    print("第%d张水印嵌入完成！" %int(k))

def compose(count):
    img = cv2.imread("D:/after/watermark_im1.png")
    imgInfo = img.shape
    size = (imgInfo[1], imgInfo[0])
    print(size)
    # 1文件名 2编码器 3帧率 4size
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    videoWrite = cv2.VideoWriter("3.avi", fourcc, 23, size)  # 写入对象
    for i in range(1, count):
        fileName = "D:/after/" + "watermark_im" + str(i) + ".png"
        img = cv2.imread(fileName)
        videoWrite.write(img)  # 写入方法
    print("视频合成完成！")

class ChildWindow1(QDialog, Ui_dialog):
    def __init__(self):
        super(ChildWindow1, self).__init__()
        self.setupUi(self)
        child = QDialog()
        child_ui = Ui_dialog()
        child_ui.setupUi(child)
        # current text change function
        self.comboBox.activated[int].connect(self.Myactivated1)
        self.timer_camera = QTimer()
        self.childbind1()
        self.open_vedio()

    def Btn_Start(self):
        # 定时器开启，每隔一段时间，读取一帧
        self.timer_camera.start(50)   #数字越小越快
        self.timer_camera.timeout.connect(self.OpenFrame)

    def Btn_Stop(self):
        # self.cap.release()
        self.timer_camera.stop()

    def open_vedio(self):
        openfile_name = "3.avi"
        self.file_name = openfile_name
        self.cap = cv2.VideoCapture(self.file_name)

    def OpenFrame(self):
        ret, image = self.cap.read()
        print(ret)
        if ret:
            if len(image.shape) == 3:
                image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                vedio_img = QImage(image.data, image.shape[1], image.shape[0], QImage.Format_RGB888)
            elif len(image.shape) == 1:
                vedio_img = QImage(image.data, image.shape[1], image.shape[0], QImage.Format_Indexed8)
            else:
                vedio_img = QImage(image.data, image.shape[1], image.shape[0], QImage.Format_RGB888)

            self.showvedio.setPixmap(QPixmap(vedio_img))
            self.showvedio.setScaledContents(True)  # 自适应窗口
        else:
            self.cap.release()
            self.timer_camera.stop()
            #self.open_vedio()


    def childbind1(self):
        # self.ui.___BUTTON___.clicked.connect(___FUNCTION___)
        # 自定义信号.属性名.connect(___FUNCTION___)"""""
        self.shipin.clicked.connect(getLocalFileshipin)
        self.shuiyin.clicked.connect(getLocalFileshuiyin)
        self.play.clicked.connect(self.Btn_Start)
        self.stop.clicked.connect(self.Btn_Stop)


    def Myactivated1(self, j):
        print(j)
        if j == 1:
            self.setwater.clicked.connect(self.LSB_shipin)
            #self.view.clicked.connect()

        if j == 2:
            self.setwater.clicked.connect(self.DWT_shipin)

        if j == 3:
            self.setwater.clicked.connect(self.DWTquanxi_shipin)

        else:
            pass


    def LSB_shipin(self):
        global count     #多少帧
        global filePath_shipin    #视频原始地址
        global filePath_shuiyin   #水印原始地址

        self.timer = QTimer()
        self.timer.start(50)
        self.timer.timeout.connect(self.load_progress_bar)

        count = 0
        time_vedio = get_video_duration(filePath_shipin)

        path1 = "D:/before"
        path2 = "D:/after"

        if os.path.exists(path1):
            shutil.rmtree(path1)
            print('shutil success!')
            os.mkdir(path1)

        else:
            print('mkdir success!')
            os.mkdir(path1)

        if os.path.exists(path2):
            shutil.rmtree(path2)
            print('shutil success!')
            os.mkdir(path2)

        else:
            print('mkdir success!')
            os.mkdir(path2)

        count = cut_vedio(time_vedio, filePath_shipin, count)

        for k in range(1, count):
            im = Image.open("D:/before/%d.png" % int(k))
            watermark = Image.open(filePath_shuiyin)
            watermark = watermark.convert("RGB")
            code = getcode(watermark)
            encry(im, code, k)

        compose(count)

    def DWT_shipin(self):
        global count
        global filePath_shipin
        global filePath_shuiyin
        self.timer = QTimer()
        self.timer.start(50)
        self.timer.timeout.connect(self.load_progress_bar)
        count = 0
        time_vedio = get_video_duration(filePath_shipin)

        path1 = "D:/before"
        path2 = "D:/after"

        if os.path.exists(path1):
            shutil.rmtree(path1)
            print('shutil success!')
            os.mkdir(path1)

        else:
            print('mkdir success!')
            os.mkdir(path1)

        if os.path.exists(path2):
            shutil.rmtree(path2)
            print('shutil success!')
            os.mkdir(path2)

        else:
            print('mkdir success!')
            os.mkdir(path2)

        count = cut_vedio(time_vedio, filePath_shipin, count)

        np.set_printoptions(threshold=np.inf)


        for k in range(1, count):
            # def plus(str):
            #     return str.zfill(8)
            Img = cv2.imread("D:/before/%d.png" % int(k))
            waterImg = cv2.imread(filePath_shuiyin)
            waterImg = cv2.resize(waterImg, (482, 272))
            b0, g0, r0 = cv2.split(Img)
            b1, g1, r1 = cv2.split(waterImg)

            b, a0, v0 = setwaterMark1(b1, b0, 0, 0.1)
            g, a1, v1 = setwaterMark1(g1, g0, 1, 0.1)
            r, a2, v2 = setwaterMark1(r1, r0, 2, 0.1)
            b0[0][0] = a1 - 100
            get = cv2.merge([b, g, r])
            cv2.imwrite('D:/after/watermark_im%d.png' % int(k), get)
            print("第%d张水印嵌入完成！" % int(k))

        compose(count)

    def DWTquanxi_shipin(self):
        global count
        global filePath_shipin
        global filePath_shuiyin
        self.timer = QTimer()
        self.timer.start(50)
        self.timer.timeout.connect(self.load_progress_bar)

        count = 0
        time_vedio = get_video_duration(filePath_shipin)

        path1 = "D:/before"
        path2 = "D:/after"

        if os.path.exists(path1):
            shutil.rmtree(path1)
            print('shutil success!')
            os.mkdir(path1)

        else:
            print('mkdir success!')
            os.mkdir(path1)

        if os.path.exists(path2):
            shutil.rmtree(path2)
            print('shutil success!')
            os.mkdir(path2)

        else:
            print('mkdir success!')
            os.mkdir(path2)

        count = cut_vedio(time_vedio, filePath_shipin, count)

        np.set_printoptions(threshold=np.inf)


        for k in range(1, count):
            # def plus(str):
            #     return str.zfill(8)
            Img = cv2.imread("D:/before/%d.png" % int(k))
            waterImg = cv2.imread(filePath_shuiyin)
            waterImg = cv2.resize(waterImg, (152, 78))
            b0, g0, r0 = cv2.split(Img)
            b1, g1, r1 = cv2.split(waterImg)

            b0, db0, db1, db2, db3 = ycl(b0, b1, 0.1)
            g0, dg0, dg1, dg2, dg3 = ycl(g0, g1, 0.1)
            r0, dr0, dr1, dr2, dr3 = ycl(r0, r1, 0.1)
            b0[0][0] = dg0 - 100
            b0[0][1] = dg1 - 100
            b0[0][2] = dg2 - 100
            b0[0][3] = dg3 - 100
            get = cv2.merge([b0, g0, r0])
            cv2.imwrite('D:/after/watermark_im%d.png' % int(k), get)
            print("第%d张水印嵌入完成！" % int(k))

        compose(count)



    def load_progress_bar(self):
        self.progressBar.setValue(self.progressBar.value() + 1)

        if self.progressBar.value() >= 100:
            self.timer.stop()



class ChildWindow(QDialog, Ui_dialog1):
    def __init__(self):
        super(ChildWindow, self).__init__()
        self.setupUi(self)
        child = QDialog()
        child_ui = Ui_dialog1()
        child_ui.setupUi(child)
        # current text change function
        self.comboBox.activated[int].connect(self.Myactivated)
        self.childbind()

    def childbind(self):
        # self.ui.___BUTTON___.clicked.connect(___FUNCTION___)
        # 自定义信号.属性名.connect(___FUNCTION___)"""""
        self.zaiti.clicked.connect(getLocalFilezaiti)
        self.shuiyin.clicked.connect(getLocalFileshuiyin)
        self.get.clicked.connect(getLocalFileget)
        self.MPN.clicked.connect(self.test)

    def LSBqianru(self):
        global filePath_get
        global filePath_shuiyin
        global filePath_zaiti
        global code
        #filePath_zaiti = getLocalFilezaiti()
        im = Image.open(filePath_zaiti)
        #print(type(im))
        #filePath_shuiyin = getLocalFileshuiyin()
        watermark = Image.open(filePath_shuiyin)
        watermark = watermark.convert("RGB")
        code = getcode(watermark)
        encry1(im,code)
        img1 = QPixmap("get.bmp").scaled(self.show1.width(), self.show1.height())
        # 在label控件上显示选择的图片
        self.show1.setPixmap(img1)

    def LSBtiqu(self):
        global filePath_get
        global filePath_shuiyin
        global filePath_zaiti
        global code
        im = Image.open(filePath_zaiti)
        watermark = Image.open(filePath_shuiyin)
        img1 = Image.open(filePath_get)
        rgb_img1 = img1.convert('RGB')
        length = len(code)
        wt = deEncry(rgb_img1, length, im)
        length_a, width_b = watermark.size
        showImage(wt, length_a, width_b)
        img2 = QPixmap("ok.png").scaled(self.show2.width(), self.show2.height())
        # 在label控件上显示选择的图片
        self.show2.setPixmap(img2)

    #dwt普通
    def qianru(self):
        np.set_printoptions(threshold=np.inf)
        global filePath_get
        global filePath_shuiyin
        global filePath_zaiti
        waterImg = cv2.imread(filePath_shuiyin)
        waterImg = cv2.resize(waterImg, (482, 272))
        Img = cv2.imread(filePath_zaiti)
        Img = cv2.resize(Img, (1920, 1080))
        cv2.imwrite('tup.bmp', Img)
        b0, g0, r0 = cv2.split(Img)
        b1, g1, r1 = cv2.split(waterImg)
        b, a0, v0 = setwaterMark1(b1, b0, 0, 0.15)
        g, a1, v1 = setwaterMark1(g1, g0, 1, 0.21)
        r, a2, v2 = setwaterMark1(r1, r0, 2, 0.15)
        b[0][0]=a1-100
        get = cv2.merge([b, g, r])

        cv2.imwrite("get.bmp", get)
        cv2.imwrite('D:\\1\\get.bmp',get)
        cv2.waitKey(0)
        img1 = QPixmap("get.bmp").scaled(self.show1.width(), self.show1.height())
        # 在label控件上显示选择的图片
        self.show1.setPixmap(img1)


    def tiqu(self):
        # 读取原始图像、嵌入水印图像
        global filePath_get
        global filePath_shuiyin
        global filePath_zaiti
        waterImg = cv2.imread(filePath_get)
        originalImage = cv2.imread('tup.bmp')
        b, g, r = cv2.split(waterImg)
        sa = 255/(b[0][0]+100)
        # 水印提取
        b0, g0, r0 = cv2.split(originalImage)
        g1 = g / sa
        v1= 0
        g = getwaterMark1(g0, g1, 2, v1, 1, 1 / 0.21)
        cv2.imwrite("ok.png", g)
        cv2.waitKey(0)

        img2 = QPixmap("ok.png").scaled(self.show2.width(), self.show2.height())
        # 在label控件上显示选择的图片
        self.show2.setPixmap(img2)


    def quanxi_qianru(self):
        np.set_printoptions(threshold=np.inf)
        global filePath_get
        global filePath_shuiyin
        global filePath_zaiti
        waterImg = cv2.imread(filePath_shuiyin)
        waterImg = cv2.resize(waterImg, (152, 78))
        Img = cv2.imread(filePath_zaiti)
        b0, g0, r0 = cv2.split(Img)
        b1, g1, r1 = cv2.split(waterImg)

        b0, db0, db1, db2, db3 = ycl(b0, b1, 0.15)
        g0, dg0, dg1, dg2, dg3 = ycl(g0, g1, 0.21)
        r0, dr0, dr1, dr2, dr3 = ycl(r0, r1, 0.15)
        b0[0][0]=dg0-100
        b0[0][1]=dg1-100
        b0[0][2]=dg2-100
        b0[0][3]=dg3-100
        get = cv2.merge([b0, g0, r0])
        cv2.imwrite("get.bmp", get)
        cv2.imwrite('D:\\1\\get.bmp', get)
        img1 = QPixmap("get.bmp").scaled(self.show1.width(), self.show1.height())
        # 在label控件上显示选择的图片
        self.show1.setPixmap(img1)


    def quanxi_tiqu(self):
        # 读取原始图像、嵌入水印图像
        global filePath_get
        global filePath_shuiyin
        global filePath_zaiti
        originalImage = cv2.imread(filePath_zaiti)
        Img = cv2.imread(filePath_get)
        b, g, r = cv2.split(Img)
        dg0 = 255/(b[0][0]+100)
        dg1 = 255/(b[0][1]+100)
        dg2 = 255/(b[0][2]+100)
        dg3 = 255/(b[0][3]+100)
        # 水印提取
        b0, g0, r0 = cv2.split(originalImage)
        s0 = g[0:300, 0:600] / dg0
        s1 = g[780:1080, 0:600] / dg1
        s2 = g[0:300, 1320:1920] / dg2
        s3 = g[780:1080, 1320:1920] / dg3
        f0 = g0[0:300, 0:600]
        f1 = g0[780:1080, 0:600]
        f2 = g0[0:300, 1320:1920]
        f3 = g0[780:1080, 1320:1920]
        h0 = quanxi_getwaterMark1(f0, s0, 2, 0, 1 / 0.21)
        h1 = quanxi_getwaterMark1(f1, s1, 2, 1, 1 / 0.21)
        h2 = quanxi_getwaterMark1(f2, s2, 2, 2, 1 / 0.21)
        h3 = quanxi_getwaterMark1(f3, s3, 2, 3, 1 / 0.21)
        H0 = np.zeros((78, 152))
        H1 = np.zeros((78, 152))
        H2 = np.zeros((78, 152))
        H3 = np.zeros((78, 152))
        h = np.zeros((78, 152))
        H0 = H0 + h0
        H1 = H1 + h1
        H2 = H2 + h2
        H3 = H3 + h3
        for m in range(152):
            for n in range(78):
                h[n][m] = mtc1(H0[n][m], H1[n][m], H2[n][m], H3[n][m])

        #cv2.imshow("new", h)
        cv2.imwrite("ok.png", h)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()
        img2 = QPixmap("ok.png").scaled(self.show2.width(), self.show2.height())
        # 在label控件上显示选择的图片
        self.show2.setPixmap(img2)

#普通dwt--- 有resize
    def test(self):
        global filePath_get
        global filePath_shuiyin
        global filePath_zaiti
        image_1 = cv2.imread(filePath_zaiti)
        image_1 = cv2.resize(image_1,(1920,1080))
        b0, g0, r0 = cv2.split(image_1)
        cols1, rows1 = b0.shape
        image_2 = cv2.imread(filePath_get)
        b1, g1, r1 = cv2.split(image_2)

        MSE2 = getMSE(g0, g1, cols1, rows1)
        PSNR2 = getPSNR(g0, g1, MSE2)
        NC2 = getNC(g0, g1, cols1, rows1)

        self.MSE.setText("%f" % MSE2)
        self.PSNR.setText("%f" % PSNR2)
        self.NC.setText("%f" % NC2)

    def Myactivated(self, i):
        print(i)
        if i == 1:
            self.setwater.clicked.connect(self.LSBqianru)
            self.getwater.clicked.connect(self.LSBtiqu)

        if i == 2:
            self.setwater.clicked.connect(self.qianru)
            self.getwater.clicked.connect(self.tiqu)

        if i == 3:
            self.setwater.clicked.connect(self.quanxi_qianru)
            self.getwater.clicked.connect(self.quanxi_tiqu)

        else:
            pass

# mainWindow
class MyMainWindow(QMainWindow, Ui_mainWindow):
    def __init__(self):
        super(MyMainWindow, self).__init__()
        self.setupUi(self)
        self.bind()
        main = QMainWindow()
        main_ui = Ui_mainWindow()
        main_ui.setupUi(main)

    def bind(self):
        self.tupian.clicked.connect(childshow)
        self.shipin.clicked.connect(childshow1)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyMainWindow()  # 实例化主窗口
    window.show()  # 显示窗口
    app.exec()  #避免程序执行到这一行后直接退出