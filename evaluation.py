
import cv2
import math

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
image_af = cv2.imread(r'C:\Users\saber\Desktop\af.bmp')
image_fir = cv2.imread(r'C:\Users\saber\Desktop\fir.bmp')
image_sed = cv2.imread(r'C:\Users\saber\Desktop\sed.bmp')
image_thr = cv2.imread(r'C:\Users\saber\Desktop\thr.bmp')
b0, g0, r0 = cv2.split(image_af)
bf,gf,rf = cv2.split(image_fir)
bs,gs,rs = cv2.split(image_sed)
bt,gt,rt = cv2.split(image_thr)
cols1, rows1 = b0.shape
image_2 = cv2.imread(r'C:\Users\saber\Desktop\or.bmp')
b1, g1, r1 = cv2.split(image_2)
MSE0 = getMSE(g0, g1, cols1, rows1)
PSNR0 = getPSNR(g0, g1, MSE0)
NC0 = getNC(g0,g1,cols1,rows1)
MSE1 = getMSE(gf, g1, cols1, rows1)
PSNR1 = getPSNR(gf, g1, MSE1)
NC1 = getNC(gf,g1,cols1,rows1)
MSE2 = getMSE(gs, g1, cols1, rows1)
PSNR2 = getPSNR(gs, g1, MSE2)
NC2 = getNC(gs,g1,cols1,rows1)
MSE3 = getMSE(gt, g1, cols1, rows1)
PSNR3 = getPSNR(gt, g1, MSE3)
NC3 = getNC(gt,g1,cols1,rows1)
print(MSE0,MSE1,MSE2,MSE3)
print(PSNR0,PSNR1,PSNR2,PSNR3)
print(abs(NC0-1),abs(NC1-1),abs(NC2-1),abs(NC3-1))