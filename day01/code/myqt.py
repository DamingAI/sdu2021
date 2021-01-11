# 依赖第三方库
# import 模块名
# import 模块名  as 新名字

# from  *.py import *
# from 模块 import 模块

# ---QT DEMO----
# 桌面应用程序-->窗口---->按钮 文本 视频
from PyQt5.QtWidgets import QApplication,QWidget
# python 系统模块
import sys
# 应用程序
app = QApplication(sys.argv)
# 窗口组件
box = QWidget()
box.resize(250,250) #大小
box.move(300,300)  #位置
box.setWindowTitle("box")# 标题
box.show() #显示
#app
status = app.exec_()
sys.exit(status)
