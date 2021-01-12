# app 程序的入口

# 包文件管理 项目根路径引入
from app.uis.trafficapp import TrafficApp
import sys

app = TrafficApp()
status = app.exec_()
sys.exit(status)
