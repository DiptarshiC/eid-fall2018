# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtCore import QTimer

    
count=0

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(478, 300)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(290, 260, 176, 31))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.lcdNumber = QtWidgets.QLCDNumber(Dialog)
        self.lcdNumber.setGeometry(QtCore.QRect(80, 50, 64, 23))
        self.lcdNumber.setObjectName("lcdNumber")
        self.lcdNumber_2 = QtWidgets.QLCDNumber(Dialog)
        self.lcdNumber_2.setGeometry(QtCore.QRect(270, 50, 64, 23))
        self.lcdNumber_2.setObjectName("lcdNumber_2")
        self.lcdNumber_3 = QtWidgets.QLCDNumber(Dialog)
        self.lcdNumber_3.setGeometry(QtCore.QRect(80, 100, 64, 23))
        self.lcdNumber_3.setObjectName("lcdNumber_3")
        self.lcdNumber_4 = QtWidgets.QLCDNumber(Dialog)
        self.lcdNumber_4.setGeometry(QtCore.QRect(270, 100, 64, 23))
        self.lcdNumber_4.setObjectName("lcdNumber_4")
        self.lcdNumber_5 = QtWidgets.QLCDNumber(Dialog)
        self.lcdNumber_5.setGeometry(QtCore.QRect(80, 150, 64, 23))
        self.lcdNumber_5.setObjectName("lcdNumber_5")
        self.lcdNumber_6 = QtWidgets.QLCDNumber(Dialog)
        self.lcdNumber_6.setGeometry(QtCore.QRect(270, 150, 64, 23))
        self.lcdNumber_6.setObjectName("lcdNumber_6")
        self.lcdNumber_7 = QtWidgets.QLCDNumber(Dialog)
        self.lcdNumber_7.setGeometry(QtCore.QRect(80, 200, 64, 23))
        self.lcdNumber_7.setObjectName("lcdNumber_7")
        self.lcdNumber_8 = QtWidgets.QLCDNumber(Dialog)
        self.lcdNumber_8.setGeometry(QtCore.QRect(270, 200, 64, 23))
        self.lcdNumber_8.setObjectName("lcdNumber_8")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, 50, 67, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(180, 50, 67, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(0, 100, 67, 21))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(180, 100, 67, 21))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(0, 150, 67, 21))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(180, 150, 67, 21))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(0, 200, 67, 21))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(180, 200, 67, 21))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(80, 10, 101, 21))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(Dialog)
        self.label_10.setGeometry(QtCore.QRect(260, 10, 67, 21))
        self.label_10.setObjectName("label_10")
        self.PushButton = QtWidgets.QPushButton(Dialog)
        self.PushButton.setGeometry(QtCore.QRect(0, 260, 101, 31))
        self.PushButton.setObjectName("PushButton")
        #self.PushButton.clicked.connect(self.Update_data)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(110, 260, 101, 31))
        self.pushButton.setObjectName("pushButton")
        #self.pushButton.clicked.connect(self.Update_data)
        #self.timer = QTimer(self)  
        #self.timer.setInterval(1000)
        #self.timer.timeout.connect(self.Update_data)
        self.timer = QtCore.QTimer()
        self.timer.start(1000)
        self.timer.timeout.connect(self.Update_data)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Current"))
        self.label_2.setText(_translate("Dialog", "Current"))
        self.label_3.setText(_translate("Dialog", "Average"))
        self.label_4.setText(_translate("Dialog", "Average"))
        self.label_5.setText(_translate("Dialog", "Highest"))
        self.label_6.setText(_translate("Dialog", "Highest"))
        self.label_7.setText(_translate("Dialog", "Lowest"))
        self.label_8.setText(_translate("Dialog", "Lowest"))
        self.label_9.setText(_translate("Dialog", "Temperature"))
        self.label_10.setText(_translate("Dialog", "Humidity"))
        self.PushButton.setText(_translate("Dialog", "Celcius"))
        self.pushButton.setText(_translate("Dialog", "Farenheit"))
    
    def Update_data(self):
        global count
        count=count+1
        self.lcdNumber.display(count)
        self.lcdNumber_2.display(count)
        self.lcdNumber_3.display(count)
        self.lcdNumber_4.display(count)
        self.lcdNumber_5.display(count)
        self.lcdNumber_6.display(count)
        self.lcdNumber_7.display(count)
        self.lcdNumber_8.display(count)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    global count
    sys.exit(app.exec_())

