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
        self.weeks = 0
        self.setWindowIcon(QIcon("./icon.ico"))
        self.timer = QTimer()
        self.topcont = False
        self.nvb = False
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
        self.week.display(self.weeks)
    def get_time(self):
        temp = time.strftime("%D")
        self.years=int(temp.split("/")[2])+2000
        self.months = int(temp.split("/")[0])
        self.days = int(temp.split("/")[1])
        self.hours = int(time.strftime("%H"))
        self.mins = int(time.strftime("%M"))
        self.secs = int(time.strftime("%S"))
        
        self.get_week()
    def get_week(self):
        week_dict = {"Monday":1,"Tuesday":2,"Wednesday":3,"Thursday":4,"Friday":5,"Saturday":6,"Sunday":7}
        self.weeks = week_dict[time.strftime("%A")]
    def Windowhasnoborder(self):
        self.nvb = True
        self.Freamleass.setEnabled(False)
        self.update_windowflag()
        self.show()
    def update_windowflag(self):
        if self.topcont:
            self.setWindowFlag(Qt.WindowStaysOnTopHint)
        if self.nvb:
            self.setWindowFlag(Qt.FramelessWindowHint)
    def closeClock(self):
        sys.exit()
    def windowOnTop(self):
        self.topcont = True
        self.windowontop.setEnabled(False)
        self.update_windowflag()
        self.show()
if __name__=="__main__":
    app=QApplication(sys.argv)
    window = Clock()
    sys.exit(app.exec())
