from PyQt5.QtWidgets import QApplication

from app.uis.traficframe import TrafficFrame
from app.uis.loginframe import LoginFrame
class TrafficApp(QApplication):
    # 构造方法 （创建对象）
    def __init__(self):
        super(TrafficApp,self).__init__([])
        
        # app主窗口
        self.main_dlg = TrafficFrame()

        # app 登录窗口
        self.login_dlg = LoginFrame(self.main_dlg)

        # 登录窗口show
        self.login_dlg.show()