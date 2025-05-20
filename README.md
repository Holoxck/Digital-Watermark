# Digital-Watermark
这是一个使用DWT和Arnold技术的数字水印系统，作用于图片和视频的隐形水印写入.
算法采取两中处理思路：
  1、整体嵌入，在目标图片或视频的RGB三个色道上分别按不同比例嵌入；
  2、将目标图片或视频拆分为4各模块，在各个模块的RGB三个色道上分别嵌入水印图片

## Repo Structure
```Digital-Watermark
**shuzi.bmp** 水印图片
**tup.bmp** 目标图片
**vediopicture.py** 运行GUI界面
**ui_mainwin1.py** GUI子界面1
**ui_childwin1** GUI子界面2
**ui_childwin3** GUI子界面3
**RGB.py** 水印嵌入提取脚本
**RGB-gui.py** 嵌入提取+gui脚本
**attack.py** 攻击脚本
**evaluation.py** 评估脚本 
**result** 用于呈现嵌入结果的文件夹
-----**resutl1.png** 嵌入前后对比+指标
-----**result2.png** 攻击后提取的水印1
-----**result3.png** 攻击后提取的水印2
-----**result4.png** 攻击后提取的水印3
-----**video1.avi** 原始视频
-----**video-LSB.avi** 经过LSN嵌入的视频
-----**video-DWT1.avi** 整体DWT嵌入视频
-----**video-DWT2.avi** 拆分为4个模块 DWT嵌入视频
`README.md` guidance for run experiments

