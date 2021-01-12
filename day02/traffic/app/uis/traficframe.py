from PyQt5.QtWidgets import QDialog
from PyQt5.QtGui import QImage,QPixmap
from PyQt5.Qt import Qt
from app.uis.trafficui import Ui_Dialog
import cv2 as cv
from app.uis.Video import Video

class TrafficFrame(QDialog):
    def __init__(self):
        super(TrafficFrame,self).__init__()
        # self.ui
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        # 线程
        self.th1 = Video(1,"data/t.mp4")
        self.th2 = Video(2,"data/4.mp4")

        # 3、信号指定接收者TrafficFrame
        # 4、接收者指定槽函数(数据处理函数)
        self.th1.sign_show.connect(self.show_video)
        self.th2.sign_show.connect(self.show_video)

        # 启动线程
        self.th1.start()
        self.th2.start()
    # 5 槽函数定义
    def show_video(self,h,w,c,data,th_id):
        image = QImage(data,w,h,w*c,QImage.Format_BGR888)
        pix = QPixmap.fromImage(image)
        if th_id == 1:
            self.ui.label_7.setPixmap(pix)
            self.ui.label_7.setScaledContents(True)
        if th_id ==2:
            self.ui.label_8.setPixmap(pix)
            self.ui.label_8.setScaledContents(True)






