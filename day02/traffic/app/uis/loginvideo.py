from PyQt5.QtCore import QThread
from PyQt5.QtCore import pyqtSignal
import cv2 as cv
class LoginVideo(QThread):
    sign_show = pyqtSignal(int,int,int,bytes)
    def __init__(self):
        super(LoginVideo,self).__init__()
        
        self.dev = cv.VideoCapture("data/t.mp4",cv.CAP_DSHOW)
        self.dev.open("data/t.mp4")

    def run(self):
        while True:
            status, frame = self.dev.read()
            if not status:
                self.dev.open("data/t.mp4")
                continue

            h,w,c = frame.shape
            data = frame.tobytes()
            self.sign_show.emit(h,w,c,data)
            QThread.usleep(100000)
    def close(self):
        self.terminate()
        while self.isRunning():
            pass
        self.dev.release()        
