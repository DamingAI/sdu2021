from PyQt5.QtWidgets import QApplication

from app.uis.traficframe import TrafficFrame
class TrafficApp(QApplication):
    # 构造方法 （创建对象）
    def __init__(self):
        super(TrafficApp,self).__init__([])
        
        # app主窗口
        self.main_dlg = TrafficFrame()
        self.main_dlg.show()