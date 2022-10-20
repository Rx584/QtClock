# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Clock.ui'
##
## Created by: Qt User Interface Compiler version 6.2.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLCDNumber, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_QtClock(object):
    def setupUi(self, QtClock):
        if not QtClock.objectName():
            QtClock.setObjectName(u"QtClock")
        QtClock.resize(540, 226)
        QtClock.setMinimumSize(QSize(540, 226))
        QtClock.setMaximumSize(QSize(540, 226))
        self.centralwidget = QWidget(QtClock)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.year = QLCDNumber(self.centralwidget)
        self.year.setObjectName(u"year")

        self.horizontalLayout.addWidget(self.year)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.month = QLCDNumber(self.centralwidget)
        self.month.setObjectName(u"month")

        self.horizontalLayout.addWidget(self.month)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.day = QLCDNumber(self.centralwidget)
        self.day.setObjectName(u"day")

        self.horizontalLayout.addWidget(self.day)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout.addWidget(self.label_3)

        self.week = QLCDNumber(self.centralwidget)
        self.week.setObjectName(u"week")

        self.horizontalLayout.addWidget(self.week)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.hour = QLCDNumber(self.centralwidget)
        self.hour.setObjectName(u"hour")

        self.horizontalLayout_2.addWidget(self.hour)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_2.addWidget(self.label_4)

        self.minutes = QLCDNumber(self.centralwidget)
        self.minutes.setObjectName(u"minutes")

        self.horizontalLayout_2.addWidget(self.minutes)

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_2.addWidget(self.label_5)

        self.second = QLCDNumber(self.centralwidget)
        self.second.setObjectName(u"second")

        self.horizontalLayout_2.addWidget(self.second)

        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_2.addWidget(self.label_6)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.start_button = QPushButton(self.centralwidget)
        self.start_button.setObjectName(u"start_button")

        self.horizontalLayout_3.addWidget(self.start_button)

        self.Freamleass = QPushButton(self.centralwidget)
        self.Freamleass.setObjectName(u"Freamleass")

        self.horizontalLayout_3.addWidget(self.Freamleass)

        self.windowontop = QPushButton(self.centralwidget)
        self.windowontop.setObjectName(u"windowontop")

        self.horizontalLayout_3.addWidget(self.windowontop)

        self.close = QPushButton(self.centralwidget)
        self.close.setObjectName(u"close")

        self.horizontalLayout_3.addWidget(self.close)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        QtClock.setCentralWidget(self.centralwidget)

        self.retranslateUi(QtClock)

        QMetaObject.connectSlotsByName(QtClock)
    # setupUi

    def retranslateUi(self, QtClock):
        QtClock.setWindowTitle(QCoreApplication.translate("QtClock", u"Clock", None))
        self.label.setText(QCoreApplication.translate("QtClock", u"\u5e74", None))
        self.label_2.setText(QCoreApplication.translate("QtClock", u"\u6708", None))
        self.label_3.setText(QCoreApplication.translate("QtClock", u"\u65e5     \u661f\u671f", None))
        self.label_4.setText(QCoreApplication.translate("QtClock", u"\u65f6", None))
        self.label_5.setText(QCoreApplication.translate("QtClock", u"\u5206", None))
        self.label_6.setText(QCoreApplication.translate("QtClock", u"\u79d2", None))
        self.start_button.setText(QCoreApplication.translate("QtClock", u"\u542f\u52a8\uff01", None))
        self.Freamleass.setText(QCoreApplication.translate("QtClock", u"\u6253\u5f00\u7a97\u53e3\u65e0\u8fb9\u6846", None))
        self.windowontop.setText(QCoreApplication.translate("QtClock", u"\u542f\u7528\u7a97\u53e3\u7f6e\u9876", None))
        self.close.setText(QCoreApplication.translate("QtClock", u"\u5173\u95ed", None))
    # retranslateUi

