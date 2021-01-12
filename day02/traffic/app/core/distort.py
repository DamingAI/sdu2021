# 哈哈镜的原理：输入图像f(x,y),设置图像中心坐标Center(cx, cy)为缩放中心点。
# 图像上任意一点到中心点的相对坐标tx = x-cx,ty=y-cy.哈哈镜效果分为图像放大和图像缩小。

# 对于图像拉伸放大，设置图像变换的半径为radius,哈哈镜变换后的图像为p(x,y).
# x = (tx/2)*(sqrt(tx*tx + ty*ty)/radius)+cx
# y = (ty/2)*(sqrt(tx*tx + ty*ty)/radius)+cy

# 对于图像缩小，设置图像变换的半径为radius,哈哈镜变换后的图像为p(x,y).
# x = cos(atan2(ty , tx))* 12*(sqrt(tx*tx + ty*ty))+cx
# y = sin(atan2(ty , tx))* 12*(sqrt(tx*tx + ty*ty))+cy

import cv2
import math

class DistortEffect:
    def __init__(self):
        super(DistortEffect,self).__init__()


    # 图像放大函数 
    def MaxFrame(self, img_src):
        # 获取输入图像的长宽和通道
        h,w,c = img_src.shape
        # 获取中心点坐标
        center_X = w / 2
        center_Y = h / 2
        # 根据图片大小定义半径
        if(center_X > center_Y):
            radius = center_X * 1.5
        else:
            radius = center_Y * 1.5         
        # 初始变换后的坐标
        newX = 0
        newY = 0
        # 计算公式
        real_radius =int(radius / 2.0)  
        # 复制一个与原图像一样的图片 
        new_data = img_src.copy()

        for i in range(w):                # 建立循环移动像素遍历宽度方向的像素
            for j in range(h):               # 遍历高度方向的像素
                tX = i - center_X                  # 计算公式
                tY = j - center_Y
                distance = tX * tX + tY * tY
                if(distance < radius * radius):    # 变换点的距离是否太远
                    newX = int(tX/ 2.0)
                    newY = int(tY/ 2.0)

                    newX = int(newX * (math.sqrt(distance) / real_radius))
                    newX = int(newX * (math.sqrt(distance)/ real_radius))

                    newX = int(newX + center_X)
                    newY = int(newY + center_Y)

                    if newX < w and newY < h:            # 计算出的新坐标可能超出原图层，这里用if加以判断
                        new_data[j, i][0] = img_src[newY, newX][0]        # 将计算后的坐标移动到原坐标
                        new_data[j, i][1] = img_src[newY, newX][1]
                        new_data[j, i][2] = img_src[newY, newX][2]
                else:                                          # 若变换点距离太远，图像像素不变动
                    new_data[j, i][0] = img_src[j, i][0]
                    new_data[j, i][1] = img_src[j, i][1]
                    new_data[j, i][2] = img_src[j, i][2]

        return new_data


    # 图像缩小函数 
    def MinFrame(self,img_src):
        # 获取输入图像的长宽和通道
        h,w,c = img_src.shape
        # 获取中心点坐标
        center_X = w / 2
        center_Y = h / 2
        # 根据图片大小定义半径
        if(center_X > center_Y):
            radius = center_X * 1.5
        else:
            radius = center_Y * 1.5         
        # 初始变换后的坐标
        newX = 0
        newY = 0
        # 计算公式
        real_radius =int(radius / 2.0)  
        # 复制一个与原图像一样的图片 
        new_data = img_src.copy()

        for i in range(w):                # 建立循环移动像素遍历宽度方向的像素
            for j in range(h):               # 遍历高度方向的像素
                tX = i - center_X
                tY = j - center_Y
                theta = math.atan2(tY, tX)
                radius = math.sqrt((tX * tX) + (tY * tY))             #与上面一样，计算公式不一样

                newR = math.sqrt(radius) *12
                newX = int(center_X + (newR * math.cos(theta)))
                newY = int(center_Y + (newR * math.sin(theta)))

                if newX < 0 and  newX >w:
                    newX = 0

                if newY <0 and newY >h:
                    newY = 0

                if newX<w and newY<h:
                    new_data[j, i][0] = img_src[newY, newX][0]
                    new_data[j, i][1] = img_src[newY, newX][1]
                    new_data[j, i][2] = img_src[newY, newX][2]
                else:
                    new_data[j, i][0] = img_src[j, i][0]
                    new_data[j, i][1] = img_src[j, i][1]
                    new_data[j, i][2] = img_src[j, i][2]

        return new_data


    # 读取图像
    def readFile(self,filename):
        self.img_src = cv2.imread(filename)
        h,w,c = self.img_src.shape
        return h,w,c,self.img_src

# 测试
if __name__ == '__main__':
    # 输入图片
    img = cv2.imread("data/1.jpg") 
    effort = DistortEffect()
    # 输出原始图片
    cv2.imshow("original", img)

    # 拉伸放大图片（凹镜）并输出
    img2 = effort.MaxFrame(img)
    cv2.imshow("enlarge", img2) 

    # 缩小处理图片（凸镜）并输出
    img3 = effort.MinFrame(img)
    cv2.imshow("ensmall", img3)

    # 设置等待时间为零
    cv2.waitKey(0)                        

