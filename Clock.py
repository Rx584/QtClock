from ui_Clock import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class Clock(QMainWindow,Ui_QtClock):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()



if __name__=="__main__":
    app=QApplication(sys.argv)
    window = Clock()
    sys.exit(app.exec_())