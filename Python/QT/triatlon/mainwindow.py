# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 300)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(150, 10, 338, 151))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.people = QtWidgets.QVBoxLayout()
        self.people.setObjectName("people")
        self.name = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.name.setFont(font)
        self.name.setAlignment(QtCore.Qt.AlignCenter)
        self.name.setObjectName("name")
        self.people.addWidget(self.name)
        self.speed = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.speed.setObjectName("speed")
        self.people.addWidget(self.speed)
        self.swim = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.swim.setObjectName("swim")
        self.people.addWidget(self.swim)
        self.run = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.run.setObjectName("run")
        self.people.addWidget(self.run)
        self.res = QtWidgets.QLabel(self.gridLayoutWidget)
        self.res.setText("")
        self.res.setObjectName("res")
        self.people.addWidget(self.res)
        self.gridLayout.addLayout(self.people, 0, 1, 1, 1)
        self.people_2 = QtWidgets.QVBoxLayout()
        self.people_2.setObjectName("people_2")
        self.name_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.name_2.setFont(font)
        self.name_2.setAlignment(QtCore.Qt.AlignCenter)
        self.name_2.setObjectName("name_2")
        self.people_2.addWidget(self.name_2)
        self.speed_2 = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.speed_2.setObjectName("speed_2")
        self.people_2.addWidget(self.speed_2)
        self.swim_2 = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.swim_2.setObjectName("swim_2")
        self.people_2.addWidget(self.swim_2)
        self.run_2 = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.run_2.setObjectName("run_2")
        self.people_2.addWidget(self.run_2)
        self.res_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.res_2.setText("")
        self.res_2.setObjectName("res_2")
        self.people_2.addWidget(self.res_2)
        self.gridLayout.addLayout(self.people_2, 0, 2, 1, 1)
        self.people_3 = QtWidgets.QVBoxLayout()
        self.people_3.setObjectName("people_3")
        self.name_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.name_3.setFont(font)
        self.name_3.setAlignment(QtCore.Qt.AlignCenter)
        self.name_3.setObjectName("name_3")
        self.people_3.addWidget(self.name_3)
        self.speed_3 = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.speed_3.setObjectName("speed_3")
        self.people_3.addWidget(self.speed_3)
        self.swim_3 = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.swim_3.setObjectName("swim_3")
        self.people_3.addWidget(self.swim_3)
        self.run_3 = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.run_3.setObjectName("run_3")
        self.people_3.addWidget(self.run_3)
        self.res_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.res_3.setText("")
        self.res_3.setObjectName("res_3")
        self.people_3.addWidget(self.res_3)
        self.gridLayout.addLayout(self.people_3, 0, 3, 1, 1)
        self.people_4 = QtWidgets.QVBoxLayout()
        self.people_4.setObjectName("people_4")
        self.gridLayout.addLayout(self.people_4, 0, 0, 1, 1)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(90, 170, 341, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.winner = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.winner.setContentsMargins(0, 0, 0, 0)
        self.winner.setObjectName("winner")
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.winner.addWidget(self.pushButton)
        self.label_6 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.winner.addWidget(self.label_6)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(90, 10, 51, 21))
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(90, 80, 41, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(50, 140, 97, 21))
        self.label_5.setObjectName("label_5")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(50, 40, 97, 21))
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 110, 97, 21))
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.name.setText(_translate("MainWindow", "Андрей"))
        self.speed.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">3531</p></body></html>"))
        self.swim.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">666</p></body></html>"))
        self.run.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">33424</p></body></html>"))
        self.name_2.setText(_translate("MainWindow", "Егор"))
        self.name_3.setText(_translate("MainWindow", "Михаил"))
        self.pushButton.setText(_translate("MainWindow", "Чемпион"))
        self.label.setText(_translate("MainWindow", "Скорость"))
        self.label_4.setText(_translate("MainWindow", "Бег (км/ч)"))
        self.label_5.setText(_translate("MainWindow", "Общее время (мин)"))
        self.label_3.setText(_translate("MainWindow", "Велосипед (км/ч)"))
        self.label_2.setText(_translate("MainWindow", "Плавает (м/мин)"))
