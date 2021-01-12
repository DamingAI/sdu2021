from PyQt5.QtWidgets import QDialog
from PyQt5.QtGui import QImage,QPixmap
from PyQt5.Qt import Qt
# from app.uis.trafficui import Ui_Dialog
from app.uis.hahaui import Ui_Dialog
import cv2 as cv

class TrafficFrame(QDialog):
    def __init__(self):
        super(TrafficFrame,self).__init__()
        #self.ui
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.load_img()
        
    # 加载图片并显示
    def load_img(self):
        img = cv.imread("data/1.jpg")
        # numpy图像-----》QT图像
        h,w,c = img.shape
        data = img.tobytes()
        image = QImage(data,w,h,w*c,QImage.Format_BGR888)
        # QT图像--->Pixmap
        pix = QPixmap.fromImage(image)
        # 显示
        width = self.ui.label.width()
        height = self.ui.label.height()
        scale_pix = pix.scaled(width,height,Qt.KeepAspectRatio)
        self.ui.label.setPixmap(scale_pix)

