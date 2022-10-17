from ui_Clock import *
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
import sys
import time

class Clock(QMainWindow,Ui_QtClock):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.years=2020
        self.months = 1
        self.days=1
        self.hours = 12
        self.mins = 0
        self.secs=0
        self.setWindowIcon(QIcon("./icon.ico"))
        self.timer = QTimer()
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.start_button.clicked.connect(self.start_clock)
        self.Freamleass.clicked.connect(self.Windowhasnoborder)
        self.close.clicked.connect(self.closeClock)
        self.windowontop.clicked.connect(self.windowOnTop)
        self.show()
    def start_clock(self):
        self.start_button.setEnabled(False)
        self.update_time()
        self.timer.start(1000)
        self.timer.timeout.connect(self.update_time)
    def update_time(self):
        #while(True):
        self.get_time()
        self.year.display(self.years)
        self.month.display(self.months)
        self.day.display(self.days)
        self.hour.display(self.hours)
        self.minutes.display(self.mins)
        self.second.display(self.secs)
    def get_time(self):
        temp = time.strftime("%D")
        self.years=int(temp.split("/")[2])+2000
        self.months = int(temp.split("/")[0])
        self.days = int(temp.split("/")[1])
        self.hours = int(time.strftime("%H"))
        self.mins = int(time.strftime("%M"))
        self.secs = int(time.strftime("%S"))
    def Windowhasnoborder(self):
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.Freamleass.setEnabled(False)
        self.show()
    def closeClock(self):
        exit()
    def windowOnTop(self):
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.windowontop.setEnabled(False)
        self.show()
if __name__=="__main__":
    app=QApplication(sys.argv)
    window = Clock()
    sys.exit(app.exec())