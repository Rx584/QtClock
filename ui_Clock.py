# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\Administrator\Desktop\QtClock\Clock.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_QtClock(object):
    def setupUi(self, QtClock):
        QtClock.setObjectName("QtClock")
        QtClock.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(QtClock)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.year = QtWidgets.QLCDNumber(self.centralwidget)
        self.year.setObjectName("year")
        self.horizontalLayout.addWidget(self.year)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.month = QtWidgets.QLCDNumber(self.centralwidget)
        self.month.setObjectName("month")
        self.horizontalLayout.addWidget(self.month)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.day = QtWidgets.QLCDNumber(self.centralwidget)
        self.day.setObjectName("day")
        self.horizontalLayout.addWidget(self.day)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.second = QtWidgets.QLCDNumber(self.centralwidget)
        self.second.setObjectName("second")
        self.horizontalLayout_2.addWidget(self.second)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.minutes = QtWidgets.QLCDNumber(self.centralwidget)
        self.minutes.setObjectName("minutes")
        self.horizontalLayout_2.addWidget(self.minutes)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_2.addWidget(self.label_5)
        self.hour = QtWidgets.QLCDNumber(self.centralwidget)
        self.hour.setObjectName("hour")
        self.horizontalLayout_2.addWidget(self.hour)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_2.addWidget(self.label_6)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.start_button = QtWidgets.QPushButton(self.centralwidget)
        self.start_button.setObjectName("start_button")
        self.verticalLayout.addWidget(self.start_button)
        QtClock.setCentralWidget(self.centralwidget)

        self.retranslateUi(QtClock)
        QtCore.QMetaObject.connectSlotsByName(QtClock)

    def retranslateUi(self, QtClock):
        _translate = QtCore.QCoreApplication.translate
        QtClock.setWindowTitle(_translate("QtClock", "Clock"))
        self.label.setText(_translate("QtClock", "年"))
        self.label_2.setText(_translate("QtClock", "月"))
        self.label_3.setText(_translate("QtClock", "日"))
        self.label_4.setText(_translate("QtClock", "时"))
        self.label_5.setText(_translate("QtClock", "分"))
        self.label_6.setText(_translate("QtClock", "秒"))
        self.start_button.setText(_translate("QtClock", "启动！"))
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Clock.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_QtClock(object):
    def setupUi(self, QtClock):
        QtClock.setObjectName("QtClock")
        QtClock.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(QtClock)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.year = QtWidgets.QLCDNumber(self.centralwidget)
        self.year.setObjectName("year")
        self.horizontalLayout.addWidget(self.year)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.month = QtWidgets.QLCDNumber(self.centralwidget)
        self.month.setObjectName("month")
        self.horizontalLayout.addWidget(self.month)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.day = QtWidgets.QLCDNumber(self.centralwidget)
        self.day.setObjectName("day")
        self.horizontalLayout.addWidget(self.day)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.second = QtWidgets.QLCDNumber(self.centralwidget)
        self.second.setObjectName("second")
        self.horizontalLayout_2.addWidget(self.second)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.minutes = QtWidgets.QLCDNumber(self.centralwidget)
        self.minutes.setObjectName("minutes")
        self.horizontalLayout_2.addWidget(self.minutes)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_2.addWidget(self.label_5)
        self.hour = QtWidgets.QLCDNumber(self.centralwidget)
        self.hour.setObjectName("hour")
        self.horizontalLayout_2.addWidget(self.hour)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_2.addWidget(self.label_6)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.start_button = QtWidgets.QPushButton(self.centralwidget)
        self.start_button.setObjectName("start_button")
        self.verticalLayout.addWidget(self.start_button)
        QtClock.setCentralWidget(self.centralwidget)

        self.retranslateUi(QtClock)
        QtCore.QMetaObject.connectSlotsByName(QtClock)

    def retranslateUi(self, QtClock):
        _translate = QtCore.QCoreApplication.translate
        QtClock.setWindowTitle(_translate("QtClock", "Clock"))
        self.label.setText(_translate("QtClock", "年"))
        self.label_2.setText(_translate("QtClock", "月"))
        self.label_3.setText(_translate("QtClock", "日"))
        self.label_4.setText(_translate("QtClock", "时"))
        self.label_5.setText(_translate("QtClock", "分"))
        self.label_6.setText(_translate("QtClock", "秒"))
        self.start_button.setText(_translate("QtClock", "启动！"))
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Clock.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_QtClock(object):
    def setupUi(self, QtClock):
        QtClock.setObjectName("QtClock")
        QtClock.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(QtClock)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.year = QtWidgets.QLCDNumber(self.centralwidget)
        self.year.setObjectName("year")
        self.horizontalLayout.addWidget(self.year)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.month = QtWidgets.QLCDNumber(self.centralwidget)
        self.month.setObjectName("month")
        self.horizontalLayout.addWidget(self.month)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.day = QtWidgets.QLCDNumber(self.centralwidget)
        self.day.setObjectName("day")
        self.horizontalLayout.addWidget(self.day)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.hour = QtWidgets.QLCDNumber(self.centralwidget)
        self.hour.setObjectName("hour")
        self.horizontalLayout_2.addWidget(self.hour)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.minutes = QtWidgets.QLCDNumber(self.centralwidget)
        self.minutes.setObjectName("minutes")
        self.horizontalLayout_2.addWidget(self.minutes)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_2.addWidget(self.label_5)
        self.second = QtWidgets.QLCDNumber(self.centralwidget)
        self.second.setObjectName("second")
        self.horizontalLayout_2.addWidget(self.second)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_2.addWidget(self.label_6)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.start_button = QtWidgets.QPushButton(self.centralwidget)
        self.start_button.setObjectName("start_button")
        self.verticalLayout.addWidget(self.start_button)
        QtClock.setCentralWidget(self.centralwidget)

        self.retranslateUi(QtClock)
        QtCore.QMetaObject.connectSlotsByName(QtClock)

    def retranslateUi(self, QtClock):
        _translate = QtCore.QCoreApplication.translate
        QtClock.setWindowTitle(_translate("QtClock", "Clock"))
        self.label.setText(_translate("QtClock", "年"))
        self.label_2.setText(_translate("QtClock", "月"))
        self.label_3.setText(_translate("QtClock", "日"))
        self.label_4.setText(_translate("QtClock", "时"))
        self.label_5.setText(_translate("QtClock", "分"))
        self.label_6.setText(_translate("QtClock", "秒"))
        self.start_button.setText(_translate("QtClock", "启动！"))
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Clock.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_QtClock(object):
    def setupUi(self, QtClock):
        QtClock.setObjectName("QtClock")
        QtClock.resize(540, 226)
        self.centralwidget = QtWidgets.QWidget(QtClock)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.year = QtWidgets.QLCDNumber(self.centralwidget)
        self.year.setObjectName("year")
        self.horizontalLayout.addWidget(self.year)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.month = QtWidgets.QLCDNumber(self.centralwidget)
        self.month.setObjectName("month")
        self.horizontalLayout.addWidget(self.month)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.day = QtWidgets.QLCDNumber(self.centralwidget)
        self.day.setObjectName("day")
        self.horizontalLayout.addWidget(self.day)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.hour = QtWidgets.QLCDNumber(self.centralwidget)
        self.hour.setObjectName("hour")
        self.horizontalLayout_2.addWidget(self.hour)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.minutes = QtWidgets.QLCDNumber(self.centralwidget)
        self.minutes.setObjectName("minutes")
        self.horizontalLayout_2.addWidget(self.minutes)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_2.addWidget(self.label_5)
        self.second = QtWidgets.QLCDNumber(self.centralwidget)
        self.second.setObjectName("second")
        self.horizontalLayout_2.addWidget(self.second)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_2.addWidget(self.label_6)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.start_button = QtWidgets.QPushButton(self.centralwidget)
        self.start_button.setObjectName("start_button")
        self.verticalLayout.addWidget(self.start_button)
        QtClock.setCentralWidget(self.centralwidget)

        self.retranslateUi(QtClock)
        QtCore.QMetaObject.connectSlotsByName(QtClock)

    def retranslateUi(self, QtClock):
        _translate = QtCore.QCoreApplication.translate
        QtClock.setWindowTitle(_translate("QtClock", "Clock"))
        self.label.setText(_translate("QtClock", "年"))
        self.label_2.setText(_translate("QtClock", "月"))
        self.label_3.setText(_translate("QtClock", "日"))
        self.label_4.setText(_translate("QtClock", "时"))
        self.label_5.setText(_translate("QtClock", "分"))
        self.label_6.setText(_translate("QtClock", "秒"))
        self.start_button.setText(_translate("QtClock", "启动！"))
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Clock.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_QtClock(object):
    def setupUi(self, QtClock):
        QtClock.setObjectName("QtClock")
        QtClock.resize(540, 226)
        QtClock.setMinimumSize(QtCore.QSize(540, 226))
        QtClock.setMaximumSize(QtCore.QSize(540, 226))
        self.centralwidget = QtWidgets.QWidget(QtClock)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.year = QtWidgets.QLCDNumber(self.centralwidget)
        self.year.setObjectName("year")
        self.horizontalLayout.addWidget(self.year)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.month = QtWidgets.QLCDNumber(self.centralwidget)
        self.month.setObjectName("month")
        self.horizontalLayout.addWidget(self.month)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.day = QtWidgets.QLCDNumber(self.centralwidget)
        self.day.setObjectName("day")
        self.horizontalLayout.addWidget(self.day)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.hour = QtWidgets.QLCDNumber(self.centralwidget)
        self.hour.setObjectName("hour")
        self.horizontalLayout_2.addWidget(self.hour)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.minutes = QtWidgets.QLCDNumber(self.centralwidget)
        self.minutes.setObjectName("minutes")
        self.horizontalLayout_2.addWidget(self.minutes)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_2.addWidget(self.label_5)
        self.second = QtWidgets.QLCDNumber(self.centralwidget)
        self.second.setObjectName("second")
        self.horizontalLayout_2.addWidget(self.second)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_2.addWidget(self.label_6)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.start_button = QtWidgets.QPushButton(self.centralwidget)
        self.start_button.setObjectName("start_button")
        self.verticalLayout.addWidget(self.start_button)
        QtClock.setCentralWidget(self.centralwidget)

        self.retranslateUi(QtClock)
        QtCore.QMetaObject.connectSlotsByName(QtClock)

    def retranslateUi(self, QtClock):
        _translate = QtCore.QCoreApplication.translate
        QtClock.setWindowTitle(_translate("QtClock", "Clock"))
        self.label.setText(_translate("QtClock", "年"))
        self.label_2.setText(_translate("QtClock", "月"))
        self.label_3.setText(_translate("QtClock", "日"))
        self.label_4.setText(_translate("QtClock", "时"))
        self.label_5.setText(_translate("QtClock", "分"))
        self.label_6.setText(_translate("QtClock", "秒"))
        self.start_button.setText(_translate("QtClock", "启动！"))
