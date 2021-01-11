from PyQt5.QtWidgets import QDialog

from app.uis.trafficui import Ui_Dialog

class TrafficFrame(QDialog):
    def __init__(self):
        super(TrafficFrame,self).__init__()
        #self.ui
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
    