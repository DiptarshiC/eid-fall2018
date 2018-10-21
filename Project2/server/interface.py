# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtCore import QTimer

import Adafruit_DHT

import tornado.httpserver
import tornado.websocket
import tornado.ioloop
import tornado.web
import socket
import datetime

count=0   
temp=0
hum=0
temp_avg=0
hum_avg=0
temp_high=0
hum_high=0
temp_low=18
hum_low=19
flag=0
date=""
time=""

class WSHandler(tornado.websocket.WebSocketHandler):
    def open(self):
        print ('new connection')
      
    def on_message(self, message):
        print ('message received:  %s' % message)
        # Reverse Message and send it back
        print ('sending back message: %s' % message[::-1])
        self.write_message(message[::-1])
 
    def on_close(self):
        print ('connection closed')
 
    def check_origin(self, origin):
        return True
 
application = tornado.web.Application([(r'/ws', WSHandler),])





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
        #self.lcdNumber_9 = QtWidgets.QLCDNumber(Dialog)
        #self.lcdNumber_9.setGeometry(QtCore.QRect(80, 230, 251, 23))
        #self.lcdNumber_9.setObjectName("lcdNumber_9")
        self.lcdNumber_9 = QtWidgets.QLCDNumber(Dialog)
        self.lcdNumber_9.setGeometry(QtCore.QRect(80, 230, 81, 23))
        self.lcdNumber_9.setObjectName("lcdNumber_9")
        self.lcdNumber_10 = QtWidgets.QLCDNumber(Dialog)
        self.lcdNumber_10.setGeometry(QtCore.QRect(260, 230, 81, 23))
        self.lcdNumber_10.setObjectName("lcdNumber_10")
        self.label_11 = QtWidgets.QLabel(Dialog)
        self.label_11.setGeometry(QtCore.QRect(0, 230, 67, 21))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(Dialog)
        self.label_12.setGeometry(QtCore.QRect(170, 230, 67, 21))
        self.label_12.setObjectName("label_12")

        
        
        
        self.PushButton = QtWidgets.QPushButton(Dialog)
        self.PushButton.setGeometry(QtCore.QRect(0, 260, 101, 31))
        self.PushButton.setObjectName("PushButton")
        self.PushButton.clicked.connect(self.calc_farenheit)
        
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(110, 260, 101, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.calc_celcius)
        
        self.timer = QtCore.QTimer()
        self.timer.start(5000)
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
        self.label_11.setText(_translate("Dialog", "   Time"))
        self.label_12.setText(_translate("Dialog", "    Date"))
        self.PushButton.setText(_translate("Dialog", "Farenheit"))
        self.pushButton.setText(_translate("Dialog", "Celcius"))
    
    
    
    
    def Update_data(self):
        global count
        global temp
        global hum
        global temp_avg
        global hum_avg
        global temp_high
        global hum_high
        global temp_low
        global hum_low
        global date
        global time
        now = datetime.datetime.now()
        date = now.strftime("%m-%d")
        time = now.strftime("%H:%M")
        temp, hum = Adafruit_DHT.read_retry(22,4)
        
        temp_avg  = ((count*temp_avg)+temp)/(count+1)
        hum_avg   = ((count*hum_avg)+hum)/(count+1)
        if temp>temp_high:
            temp_high=temp
        if hum>hum_high:
            hum_high=hum
        if temp<temp_low:
            temp_low=temp
        if hum<hum_low:
            hum_low=hum   
        count=count+1
        if flag==1: 
            self.lcdNumber.display((9/5*temp+32))
        elif flag==0:
            self.lcdNumber.display(temp)
        self.lcdNumber_2.display(hum)
        if flag==1: 
            self.lcdNumber_3.display((9/5*temp_avg+32))
        elif flag==0:
            self.lcdNumber_3.display(temp_avg)
        self.lcdNumber_4.display(hum_avg)
        if flag==1: 
            self.lcdNumber_5.display((9/5*temp_high+32))
        elif flag==0:
            self.lcdNumber_5.display(temp_high)
        self.lcdNumber_6.display(hum_high)
        if flag==1: 
            self.lcdNumber_7.display((9/5*temp_low+32))
        elif flag==0:
            self.lcdNumber_7.display(temp_low)
        self.lcdNumber_8.display(hum_low)
        self.lcdNumber_9.display(time)
        self.lcdNumber_10.display(date)
        
    def calc_farenheit(self):
        global flag
        flag=1   
    
    def calc_celcius(self):
        global flag
        flag=0

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    global count
    sys.exit(app.exec_())

