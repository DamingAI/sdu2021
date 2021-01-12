from PyQt5.QtWidgets import QDialog
from PyQt5.QtGui import QImage,QPixmap
from PyQt5.Qt import Qt
from app.uis.loginui import Ui_Dialog
import cv2 as cv
from app.uis.loginvideo import LoginVideo

class LoginFrame(QDialog):
    def __init__(self, parent=None):
        super(LoginFrame,self).__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.th = LoginVideo()
        self.th.sign_show.connect(self.login_video)
        self.th.start()
        
    def login_video(self,h,w,c,data):
        image = QImage(data,w,h,w*c,QImage.Format_BGR888)
        pix = QPixmap.fromImage(image)
        self.ui.label.setPixmap(pix)
        self.ui.label.setScaledContents(True)
        # 智能登录业务

    def login(self):
        # 能够访问到主窗口

        #关闭当前窗口
        self.close()

        # 显示主窗口
        self.parentWidget().show()

        #当前窗口的线程也要关闭
        self.th.close()
