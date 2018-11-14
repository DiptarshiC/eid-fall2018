# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CLIENT.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!
import datetime
import sys 
import boto3
import json
import re
from PyQt5 import QtCore, QtGui, QtWidgets

temp=0
hum=0
count=0
max_temp=0
min_temp=0
max_hum=0
min_hum=0
average_temp=0
average_hum=0
avg_click=0
starttime=""
endtime=""  

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(525, 445)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(180, 410, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.lcdNumber = QtWidgets.QLCDNumber(Dialog)
        self.lcdNumber.setGeometry(QtCore.QRect(0, 40, 191, 23))
        self.lcdNumber.setObjectName("lcdNumber")
        self.lcdNumber_2 = QtWidgets.QLCDNumber(Dialog)
        self.lcdNumber_2.setGeometry(QtCore.QRect(300, 40, 201, 23))
        self.lcdNumber_2.setObjectName("lcdNumber_2")
        self.progressBar = QtWidgets.QProgressBar(Dialog)
        self.progressBar.setGeometry(QtCore.QRect(0, 110, 131, 23))
        self.progressBar.setProperty("value", 1)
        self.progressBar.setObjectName("progressBar")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, 70, 121, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(340, 70, 101, 21))
        self.label_2.setObjectName("label_2")
        self.progressBar_2 = QtWidgets.QProgressBar(Dialog)
        self.progressBar_2.setGeometry(QtCore.QRect(0, 190, 131, 23))
        self.progressBar_2.setProperty("value", 2)
        self.progressBar_2.setObjectName("progressBar_2")
        self.progressBar_3 = QtWidgets.QProgressBar(Dialog)
        self.progressBar_3.setGeometry(QtCore.QRect(310, 110, 118, 23))
        self.progressBar_3.setProperty("value", 3)
        self.progressBar_3.setObjectName("progressBar_3")
        self.progressBar_4 = QtWidgets.QProgressBar(Dialog)
        self.progressBar_4.setGeometry(QtCore.QRect(310, 190, 118, 23))
        self.progressBar_4.setProperty("value", 4)
        self.progressBar_4.setObjectName("progressBar_4")
        self.progressBar_5 = QtWidgets.QProgressBar(Dialog)
        self.progressBar_5.setGeometry(QtCore.QRect(0, 270, 131, 23))
        self.progressBar_5.setProperty("value", 5)
        self.progressBar_5.setObjectName("progressBar_5")
        self.progressBar_6 = QtWidgets.QProgressBar(Dialog)
        self.progressBar_6.setGeometry(QtCore.QRect(310, 270, 118, 23))
        self.progressBar_6.setProperty("value", 6)
        self.progressBar_6.setObjectName("progressBar_6")
        self.progressBar_7 = QtWidgets.QProgressBar(Dialog)
        self.progressBar_7.setGeometry(QtCore.QRect(0, 350, 121, 23))
        self.progressBar_7.setProperty("value", 7)
        self.progressBar_7.setObjectName("progressBar_7")
        self.progressBar_8 = QtWidgets.QProgressBar(Dialog)
        self.progressBar_8.setGeometry(QtCore.QRect(310, 350, 121, 23))
        self.progressBar_8.setProperty("value", 8)
        self.progressBar_8.setObjectName("progressBar_8")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(180, 110, 81, 21))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(180, 190, 81, 21))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(180, 270, 67, 21))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(180, 350, 67, 21))
        self.label_6.setObjectName("label_6")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(20, 410, 101, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.myfunction)
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(0, 10, 191, 21))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(300, 10, 181, 21))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(290, 410, 67, 21))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(Dialog)
        self.label_10.setGeometry(QtCore.QRect(140, 410, 131, 21))
        self.label_10.setObjectName("label_10")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
    
    
    def myfunction(self):
        global temp
        global hum
        global count
        global max_temp
        global min_temp
        global max_hum
        global min_hum
        global average_temp
        global average_hum
        global avg_click
        global starttime
        global endtime
        sqs = boto3.client('sqs', region_name = 'us-west-2',
                   aws_access_key_id='ASIAXA4WY5JYKOAXGKNN',
                   aws_secret_access_key='kzNlO3Ek7YL53CwUEVEVELJZtt96oUzPaCk7gD/d',
                   aws_session_token='FQoGZXIvYXdzEP3//////////wEaDGvIqYhUAafRztmysCKEAneom5BLSFSI8YQvDe3APAiSzfE/LC0IGfmh9EBOLG3uIoW67qh8bmV8vyT2Wt4x50MIZmWJPJQ3MqVZx9XikHGSqiKKBiNitn6a/wogPJ2iwrKPq5cUKe5to3aD0qHX+6owzEh1OUD4sIcwnwxz+KEkiss8D3mjlf+ylxMeGvoOxAisVN0GlpbA1OiOdvwFPrHnNPxdQkpPYcK6kP+hpd2tlcavnfmoLn8W8qTvudCOLBEILFdxOSu63i/82cOwIpOUL6BH56O6TVgXKyq5gFcq97uNE392A45kODrzP0ml8l/i7Xez2dAf7U1zyzasE3z47u1sEDwvWYs+PE9XSTP/KjsuKMLusd8F')                          
        url = sqs.get_queue_url(QueueName='RPI-3QUEUE.fifo')
        print(url['QueueUrl'])
        response = sqs.receive_message(QueueUrl =  url['QueueUrl'],AttributeNames= ['SentTimestamp'], MaxNumberOfMessages = 10, MessageAttributeNames=['All'], VisibilityTimeout = 0,WaitTimeSeconds = 5)

        message = response['Messages'][0]
        receipt_handle = message['ReceiptHandle']

        response1 = sqs.receive_message( QueueUrl =  url['QueueUrl'], AttributeNames= ['SentTimestamp'], MaxNumberOfMessages = 10, MessageAttributeNames=['All'],VisibilityTimeout = 0, WaitTimeSeconds = 5)

        message = response1['Messages'][0]
        receipt_handle = message['ReceiptHandle']

        response2 = sqs.receive_message(QueueUrl =  url['QueueUrl'],
        AttributeNames= ['SentTimestamp'],MaxNumberOfMessages = 10, MessageAttributeNames=['All'], VisibilityTimeout = 0, WaitTimeSeconds = 0)

        response['Messages'] = (response['Messages'] + response1['Messages'] + response2['Messages'])

        for i in range (0,30):
        
        
             now = datetime.datetime.now()
             #date = now.strftime("%Y-%m-%d")
             #datef(self)
             starttime = now.strftime("%H:%M:%S")
             #timef(self)
                  
             message = response['Messages'][i]
     	     #Spliting string and taking timestamp value
             body = response['Messages'][i]['Body']
     	     #print('\n The body content is %s' %body)
     
             x = body.split(",")
     
             str=x[0]
             num = re.findall('\d+',str)
             temp=num
             print('\nTemperature:%s' %num[0])
     
             str=x[1]
             num = re.findall('\d+',str)
             hum=num
             print('\nHumidity:%s' %num[0])
     
             str=x[2]
             num = re.findall('\d+',str)
             count=num
             print('\nCount:%s' %num[0])
     
             str=x[3]
             num = re.findall('\d+',str)
             max_temp=num
             print('\nMaximum Temperature:%s' %num[0])
     
             str=x[4]
             num = re.findall('\d+',str)
             min_temp=num
             print('\nMinimum_Temperature:%s' %num[0])
     
             str=x[5]
             num = re.findall('\d+',str)
             max_hum=num
             print('\nMaximum_Humidity:%s' %num[0])
     
             str=x[6]
             num = re.findall('\d+',str)
             min_hum=num
             print('\nMinimum_Humidity:%s' %num[0])
     
             str=x[7]
             num = re.findall('\d+',str)
             average_temp=num
             print('\nAverage_Temp:%s' %num[0])
     
             str=x[8]
             num = re.findall('\d+',str)
             average_hum=num
             print('\nAverage_Humidity:%s' %num[0])
             
             temp=float(temp[0])
             TEMP = "%2.0f" % temp
             self.progressBar.setProperty("value", TEMP)
             
             average_temp=float(average_temp[0])
             AVG_TEMP="%2.0f" % average_temp
             self.progressBar_7.setProperty("value", AVG_TEMP)
             
             max_temp=float(max_temp[0])
             MAX_TEMP="%2.0f" % max_temp
             self.progressBar_2.setProperty("value", MAX_TEMP)
             
             min_temp=float(min_temp[0])
             MIN_TEMP="%2.0f" % min_temp
             self.progressBar_5.setProperty("value", MIN_TEMP)
             
             
             hum=float(hum[0])
             hum = "%2.0f" % hum
             self.progressBar_3.setProperty("value", hum)
             
             average_hum=float(average_hum[0])
             AVG_HUM="%2.0f" % average_hum
             self.progressBar_8.setProperty("value", AVG_HUM)
             
             max_hum=float(max_hum[0])
             MAX_HUM="%2.0f" % max_hum
             self.progressBar_4.setProperty("value", MAX_HUM)
             
             min_hum=float(min_hum[0])
             MIN_HUM="%2.0f" % min_hum
             self.progressBar_6.setProperty("value", MIN_HUM)
             
             if(avg_click==30):
             	avg_click=1
             else:
                avg_click=avg_click+1
             #now = datetime.datetime.now()
             endtime=now.strftime("%H:%M:%S")
             self.lcdNumber.display(starttime)
             self.lcdNumber_2.display(endtime)
             

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "TEMPERATURE"))
        self.label_2.setText(_translate("Dialog", "HUMIDITY"))
        self.label_3.setText(_translate("Dialog", "CURRENT"))
        self.label_4.setText(_translate("Dialog", "HIGHEST"))
        self.label_5.setText(_translate("Dialog", "MINIMUM"))
        self.label_6.setText(_translate("Dialog", "AVERAGE"))
        self.pushButton.setText(_translate("Dialog", "REQUEST"))
        self.label_7.setText(_translate("Dialog", "START TIMESTAMP"))
        self.label_8.setText(_translate("Dialog", "END TIMESTAMP"))
        self.label_9.setText(_translate("Dialog", "30"))
        self.label_10.setText(_translate("Dialog", "NO. OF VALUES"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    
    #global count
    sys.exit(app.exec_())


