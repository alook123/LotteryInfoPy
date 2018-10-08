# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/alook/OneDrive/project/LotteryInfoPy/untitled.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
import sys
import time
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(542, 194)
        self.dateEdit = QtWidgets.QDateEdit(Form)
        self.dateEdit.setGeometry(QtCore.QRect(110, 20, 110, 22))
        self.dateEdit.setObjectName("dateEdit")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 20, 72, 15))
        self.label.setObjectName("label")
        self.btnManualOpen = QtWidgets.QPushButton(Form)
        self.btnManualOpen.setGeometry(QtCore.QRect(270, 20, 231, 28))
        self.btnManualOpen.setObjectName("btnManualOpen")
        self.cbAutoStart = QtWidgets.QCheckBox(Form)
        self.cbAutoStart.setGeometry(QtCore.QRect(20, 70, 91, 19))
        self.cbAutoStart.setObjectName("cbAutoStart")
        self.btnAutoDir = QtWidgets.QPushButton(Form)
        self.btnAutoDir.setGeometry(QtCore.QRect(270, 70, 231, 28))
        self.btnAutoDir.setObjectName("btnAutoDir")
        self.progressBar = QtWidgets.QProgressBar(Form)
        self.progressBar.setGeometry(QtCore.QRect(30, 140, 491, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        Form.show()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "日期"))
        now_day = time.strftime("%Y-%m-%d", time.localtime())
        self.dateEdit.setDate(QtCore.QDate.fromString(now_day, 'yyyy-MM-dd'))
        self.btnManualOpen.setText(_translate("Form", "根据日期手动生成并打开"))
        self.cbAutoStart.setText(_translate("Form", "开机启动"))
        self.btnAutoDir.setText(_translate("Form", "查看自动生成文件夹"))

if __name__ == "__main__":
    app =QtWidgets.QApplication(sys.argv)
    widget =QtWidgets.QWidget(None)
    Ui_Form().setupUi(widget)
    sys.exit(app.exec_())
    pass


