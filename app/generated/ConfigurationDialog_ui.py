# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'resources/views/ConfigurationDialog.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Configuration(object):
    def setupUi(self, Configuration):
        Configuration.setObjectName("Configuration")
        Configuration.setWindowModality(QtCore.Qt.WindowModal)
        Configuration.resize(486, 255)
        font = QtGui.QFont()
        font.setPointSize(10)
        Configuration.setFont(font)
        Configuration.setModal(True)
        self.tabWidget = QtWidgets.QTabWidget(Configuration)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 451, 191))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName("tabWidget")
        self.notes = QtWidgets.QWidget()
        self.notes.setObjectName("notes")
        self.chkAppOption = QtWidgets.QCheckBox(self.notes)
        self.chkAppOption.setGeometry(QtCore.QRect(20, 20, 201, 20))
        self.chkAppOption.setObjectName("chkAppOption")
        self.tabWidget.addTab(self.notes, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.label_5 = QtWidgets.QLabel(self.tab_4)
        self.label_5.setGeometry(QtCore.QRect(10, 10, 421, 16))
        self.label_5.setObjectName("label_5")
        self.tabWidget.addTab(self.tab_4, "")
        self.btn_save_configuration = QtWidgets.QPushButton(Configuration)
        self.btn_save_configuration.setGeometry(QtCore.QRect(360, 210, 113, 32))
        self.btn_save_configuration.setObjectName("btn_save_configuration")
        self.btn_cancel_configuration = QtWidgets.QPushButton(Configuration)
        self.btn_cancel_configuration.setGeometry(QtCore.QRect(250, 210, 113, 32))
        self.btn_cancel_configuration.setObjectName("btn_cancel_configuration")

        self.retranslateUi(Configuration)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Configuration)

    def retranslateUi(self, Configuration):
        _translate = QtCore.QCoreApplication.translate
        Configuration.setWindowTitle(_translate("Configuration", "Settings"))
        self.chkAppOption.setText(_translate("Configuration", "App configuration option"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.notes), _translate("Configuration", "Notes"))
        self.label_5.setText(_translate("Configuration", "Icons by <a href=\"https://icons8.com\">Icons8</a>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("Configuration", "Credit"))
        self.btn_save_configuration.setText(_translate("Configuration", "OK"))
        self.btn_cancel_configuration.setText(_translate("Configuration", "Cancel"))
