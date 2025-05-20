import cv2
import pywt
import numpy as np
from PIL import Image
import random
import tkinter as tk
from tkinter import filedialog
#1920*1080的图片嵌入水印
def getLocalFile():
    root=tk.Tk()
    root.withdraw()
    filePath=filedialog.askopenfilename()
    return filePath


def cl(file):
    dog = Image.open(file)
    width, height = dog.size
    dog_updown = dog.copy()
    key_updown = []
    for i in range(width):
        x = random.randint(0, height)
        key_updown.append(x)
        for j in range(height):
            pix = dog.getpixel((i, j))
            dog_updown.putpixel((i, (j + x) % height), pix)
    dog_leftright = dog_updown.copy()
    key_leftright = []
    for j in range(height):
        x = random.randint(0, width)
        key_leftright.append(x)
        for i in range(width):
            pix = dog_updown.getpixel((i, j))
            dog_leftright.putpixel(((i + x) % width, j), pix)
    dog_leftright.save("clsy.png")
    return key_leftright,key_updown

def jm(key_leftright,key_updown):
    dog=Image.open('new.png')
    width, height = dog.size
    print(width,height)
    dog_leftright = dog.copy()
    dog_updown = dog.copy()
    for j in range(height):
        x = key_leftright[j]
        key_leftright.append(x)
        for i in range(width):
            pix = dog_leftright.getpixel((i, j))
            dog_updown.putpixel(((i - x + width) % width, j), pix)
    for i in range(width):
        x = key_updown[i]
        for j in range(height):

            pix = dog_updown.getpixel((i, j))
            dog.putpixel((i, (j - x + height) % height), pix)
    dog.save('ok.png')


# arnold置换算法，key位置换次数
def arnold(img, key):
    r = img.shape[0]
    c = img.shape[1]
    p = np.zeros((r, c), np.uint8)

    a = 1
    b = 1
    for k in range(key):
        for i in range(r):
            for j in range(c):
                x = (i + b * j) % r
                y = (a * i + (a * b + 1) * j) % c
                p[x, y] = img[i, j]
    return p

# 逆arnold置换算法，key位置换次数
def deArnold(img, key):
    r = img.shape[0]
    c = img.shape[1]
    p = np.zeros((r, c), np.uint8)

    a = 1
    b = 1
    for k in range(key):
        for i in range(r):
            for j in range(c):
                x = ((a * b + 1) * i - b * j) % r
                y = (-a * i + j) % c
                p[x, y] = img[i, j]
    return p

def setwaterMark1(waterImg, Img,i,d1):
    # 载体图像三级小波变换
    c = pywt.wavedec2(Img, 'db2', level=3)
    [cl, (cH3, cV3, cD3), (cH2, cV2, cD2), (cH1, cV1, cD1)] = c
    # print(cl.shape,cH3.shape,cH2.shape)
    d = pywt.wavedec2(waterImg, 'db2', level=1)
    [ca1, (ch1, cv1, cd1)] = d
    #print(cl.shape,len(cH3),len(cH2),len(cH1),Img.shape)
    # 自定义嵌入系数
    a1 = 1.5*d1
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

    # f = open("加入水印结果.txt", 'w')
    # f.write(str(newImg))
    # f.close()
    max = np.max(newImg)//1+1
    newImg=newImg/max*255

    z =255/max
    newImg = np.array(newImg, np.uint8)
    cv2.imshow("after"+str(i), newImg)
    v = max
    cv2.waitKey(0)
    return newImg,z,v

def getwaterMark1(originalImage, Img, key,v,i,d1):
    # 载体图像三级小波变换
    c = pywt.wavedec2(Img, 'db2', level=3)
    [cl, (cH3, cV3, cD3), (cH2, cV2, cD2), (cH1, cV1, cD1)] = c
    # 原始图像三级小波变换
    d = pywt.wavedec2(originalImage, 'db2', level=3)
    [dl, (dH3, dV3, dD3), (dH2, dV2, dD2), (dH1, dV1, dD1)] = d
    # f = open("正经变换.txt", 'w')
    # f.write(str(d))
    # f.close()
    ca1 = (cl - dl) *2/3*d1
    ch1 = (cH3 - dH3) * 2*d1
    cv1 = (cV3 - dV3) * 2*d1
    cd1 = (cD3 - dD3) * 2*d1

    # 水印图像重构
    waterImg = pywt.waverec2([ca1, (ch1, cv1, cd1)], 'db2')

    # 对提取的水印图像进行逆Arnold变换
    # waterImg = deArnold(waterImg, key)

    waterImg = np.array(waterImg, np.uint8)

    # cv2.imshow("get"+str(i), waterImg)
    # cv2.imwrite(str(i)+"jeiguo.png",waterImg)
    # cv2.waitKey(0)
    return waterImg

if __name__ == '__main__':
    np.set_printoptions(threshold=np.inf)
    waterImg = cv2.imread('shuzi.bmp')
    Img = cv2.imread('dark.jpg')
    Img = cv2.resize(Img,(600,300))
    cv2.imwrite('tup.bmp',Img)
    b0, g0, r0 = cv2.split(Img)
    b1, g1, r1 = cv2.split(waterImg)
    b, a0, v0 = setwaterMark1(b1, b0,0,0.13)
    g, a1, v1 = setwaterMark1(g1, g0,1,0.3)
    r, a2, v2 = setwaterMark1(r1, r0,2,0.13)
    get= cv2.merge([b,g,r])
    cv2.imshow('1',get)
    cv2.imwrite("get.bmp",get)
    # 读取原始图像、嵌入水印图像
    originalImage = cv2.imread('tup.bmp')
    address = getLocalFile()
    waterImg = cv2.imread(address)
    b,g,r = cv2.split(waterImg)
    sa=255/v1
    print(sa,a1)
    # 水印提取
    b0, g0, r0 = cv2.split(originalImage)
    b1 = b/a0
    g1 = g/sa
    r1 = r/a2
    # b = getwaterMark1(b0, b1, 2, v0,0,1/0.13)
    g = getwaterMark1(g0, g1, 2, v1,1,1/0.3)
    # r= getwaterMark1(r0, r1, 2,v2,2,1/0.13)
    cv2.imshow("new",g)
    cv2.imwrite("ok.png",g)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
