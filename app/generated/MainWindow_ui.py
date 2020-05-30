# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'resources/views/MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(978, 723)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.txt_scratch_pad = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.txt_scratch_pad.setPlainText("")
        self.txt_scratch_pad.setObjectName("txt_scratch_pad")
        self.horizontalLayout.addWidget(self.txt_scratch_pad)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "OnePage"))
        self.txt_scratch_pad.setPlaceholderText(_translate("MainWindow", "Scratch Pad ..."))
