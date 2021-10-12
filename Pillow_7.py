# """
# 打开图像 Image.open(路径) 
# 保存图像 图像对象.save() 
# 查看图像属性 图像对象.format 图像对象.size 图像对象.mode 
# 显示图像 plt.imshow(image对象/Numpy数组) 
# 转换色彩模式 图像对象.convert(色彩模式) 
# 颜色通道的分离与合并 图像对象.split() Image.merge(色彩模式, 图像列表) 
# 将图像转换为数组 np.array(图像对象) 
# 缩放图像 图像对象.resize((width, height)) 
# 旋转和镜像 图像对象.transpose(旋转方式) 
# 裁剪图像 图像对象.crop((x0, y0, x1, y1))
# """


#导入库
from matplotlib import image
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np


plt.rcParams['font.sans-serif']="SimHei" #字体
# #打开图像 转存图像
img=Image.open("lena.tiff")
# img.save("test.tiff")
# img.save("lena.jpg")
# img.save("lena.bmp")


# #查看图像主要属性
img1=Image.open("lena.jpg")
img2=Image.open("lena.bmp")

# print("image:",img.format)
# print("image:",img1.format)
# print("image:",img2.format)

# print("size:",img.size)
# print("mode:",img.mode)


# #显示图像——imshow()
# plt.figure(figsize=(5,5))
# plt.imshow(img)
# plt.show()

# plt.figure(figsize=(15,5))

# plt.subplot(131)
# plt.axis("off")
# plt.imshow(img)
# plt.title(img.format)

# plt.subplot(132)
# plt.axis("off")
# plt.imshow(img1)
# plt.title(img1.format)

# plt.subplot(133)
# plt.axis("off")
# plt.imshow(img2)
# plt.title(img2.format)

# plt.show()


"""
转换图像的色彩模式
取值 色彩模式
1 二值图像
L 灰度图像
P 8位彩色图像
RGB 24位彩色图像
RGBA 32位彩色图像
CMYK CMYK彩色图像
YCbCr YCbCr彩色图像
I 32位整型灰度图像
F 32位浮点灰度图像
"""

# img_gray=img.convert("F")  #图像对象.convert(色彩模式)
# print("mode=",img_gray.mode)
# plt.figure(figsize=(5,5))
# plt.imshow(img_gray)
# plt.show()


# #图像分离与合并
# img_r,img_g,img_b = img.split()
# plt.figure(figsize=(10,10))

# plt.subplot(221)
# plt.axis("off")
# plt.imshow(img_r,cmap="gray")
# plt.title("R",fontsize=20)

# plt.subplot(222)
# plt.axis("off")
# plt.imshow(img_g,cmap="gray")
# plt.title("G",fontsize=20)

# plt.subplot(223)
# plt.axis("off")
# plt.imshow(img_b,cmap="gray")
# plt.title("B",fontsize=20)

# img_rgb=Image.merge("RGB",[img_r,img_g,img_b])
# plt.subplot(224)
# plt.axis("off")
# plt.imshow(img_rgb)
# plt.title("RGB",fontsize=20)

# plt.show()


# #将灰度图像转化为数组
img_gray=img.convert("L")  #图像对象.convert(色彩模式)
# print("mode=",img_gray.mode)
# plt.figure(figsize=(5,5))
# plt.imshow(img_gray)
img_gray.save("lena_gray.bmp")

# img_gray=Image.open("lena_gray.bmp")
arr_img_gray=np.array(img_gray)
# print("\nshape:",arr_img_gray.shape)
# print(arr_img_gray)


# #将彩色图像转化为数组
# arr_img=np.array(img)
# print("shape:",arr_img.shape,"\n")
# print(arr_img)


# #图像颜色反转
# arr_img_new=255-arr_img_gray
# plt.figure(figsize=(10,5))

# plt.subplot(121)
# plt.axis("off")
# plt.imshow(arr_img_gray,cmap="gray")

# plt.subplot(122)
# plt.axis("off")
# plt.imshow(arr_img_new,cmap="gray")

# plt.show()


# #对图像进行缩放，旋转和镜像
# #缩放：图像对象.resize((width, height))
# #缩放：图像对象.resize((width, height)   resize()方法不对原图进行修改
# #图像对象.thumbnail((width, height))    thumbnail()方法是原地操作，直接对image对象本身进行缩放plt.figure(figsize=(5,5))
# img_small = img.resize((64,64))
# plt.imshow(img_small)
# plt.show
# img_small.save("lena_s.jpg")

#旋转，镜像：图像对象.transpose(旋转方式)
# Image.FLIP_LEFT_RIGHT：水平翻转
# Image.FLIP_TOP_BOTTOM：上下翻转
# Image.ROTATE_90：逆时针旋转90°
# Image.ROTATE_180：逆时针旋转180°
# Image.ROTATE_270：逆时针旋转270°
# Image.TRANSPOSE：将图像进行转置
# Image.TRANSVERSE：将图像进行转置，再水平翻转
# img_flr=img.transpose(Image.FLIP_LEFT_RIGHT)
# img_r90=img.transpose(Image.ROTATE_90)
# img_tp=img.transpose(Image.TRANSPOSE)

# plt.figure(figsize=(10,10))

# plt.subplot(221)
# plt.axis("off")
# plt.imshow(img)
# plt.title("原图",fontsize=20)

# plt.subplot(222)
# plt.axis("off")
# img_flr=img.transpose(Image.FLIP_LEFT_RIGHT)
# plt.imshow(img_flr)
# plt.title("左右翻转",fontsize=20)

# plt.subplot(223)
# plt.axis("off")
# img_r90=img.transpose(Image.ROTATE_90)
# plt.imshow(img_r90)
# plt.title("逆时针旋转90度",fontsize=20)

# plt.subplot(224)
# plt.axis("off")
# img_tp=img.transpose(Image.TRANSPOSE)
# plt.imshow(img_tp)
# plt.title("转置",fontsize=20)

# plt.show()

#裁剪图像：在图像上指定的位置裁剪出一个矩形区域
#图像对象.crop((x0, y0, x1, y1))  返回值：图像对象
plt.figure(figsize=(10,5))

plt.subplot(121)
plt.imshow(img)

plt.subplot(122)
img_region=img.crop((100,100,400,400))
plt.imshow(img_region)

plt.show()

