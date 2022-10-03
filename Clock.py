from ui_Clock import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
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
        self.show()
    def update_time(self):
        self.get_time()
        self.year.display(self.years)
        self.month.display(self.months)
        self.day.display(self.days)
        self.hour.display(self.hours)
        self.minutes.display(self.mins)
        self.second.display(self.secs)
    def get_time(self):
        self.years=int(time.strftime("%Y"))
        self.months = int(time.strftime("%M"))
        self.days = int(time.strftime("%D"))
        self.hours = int(time.strftime("%H"))
        self.mins = int(time.strftime("%M"))
        self.secs = int(time.strftime("%S"))


if __name__=="__main__":
    app=QApplication(sys.argv)
    window = Clock()
    sys.exit(app.exec_())