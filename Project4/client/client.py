# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CLIENT.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

import logging
import asyncio

from aiocoap import *

import paho.mqtt.client as mqtt

import asyncio
import websockets


import pika

import matplotlib.pyplot as plt


from PyQt5 import QtCore, QtGui, QtWidgets

import numpy as np

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(531, 494)
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
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, 70, 121, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(340, 70, 101, 21))
        self.label_2.setObjectName("label_2")
        self.progressBar_2 = QtWidgets.QProgressBar(Dialog)
        self.progressBar_2.setGeometry(QtCore.QRect(0, 190, 131, 23))
        self.progressBar_2.setProperty("value", 24)
        self.progressBar_2.setObjectName("progressBar_2")
        self.progressBar_3 = QtWidgets.QProgressBar(Dialog)
        self.progressBar_3.setGeometry(QtCore.QRect(310, 110, 118, 23))
        self.progressBar_3.setProperty("value", 24)
        self.progressBar_3.setObjectName("progressBar_3")
        self.progressBar_4 = QtWidgets.QProgressBar(Dialog)
        self.progressBar_4.setGeometry(QtCore.QRect(310, 190, 118, 23))
        self.progressBar_4.setProperty("value", 24)
        self.progressBar_4.setObjectName("progressBar_4")
        self.progressBar_5 = QtWidgets.QProgressBar(Dialog)
        self.progressBar_5.setGeometry(QtCore.QRect(0, 270, 131, 23))
        self.progressBar_5.setProperty("value", 24)
        self.progressBar_5.setObjectName("progressBar_5")
        self.progressBar_6 = QtWidgets.QProgressBar(Dialog)
        self.progressBar_6.setGeometry(QtCore.QRect(310, 270, 118, 23))
        self.progressBar_6.setProperty("value", 24)
        self.progressBar_6.setObjectName("progressBar_6")
        self.progressBar_7 = QtWidgets.QProgressBar(Dialog)
        self.progressBar_7.setGeometry(QtCore.QRect(0, 350, 121, 23))
        self.progressBar_7.setProperty("value", 24)
        self.progressBar_7.setObjectName("progressBar_7")
        self.progressBar_8 = QtWidgets.QProgressBar(Dialog)
        self.progressBar_8.setGeometry(QtCore.QRect(310, 350, 121, 23))
        self.progressBar_8.setProperty("value", 24)
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
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 450, 101, 31))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "TEMPERATURE"))
        self.label_2.setText(_translate("Dialog", "HUMIDITY"))
        self.label_3.setText(_translate("Dialog", "CURRENT"))
        self.label_4.setText(_translate("Dialog", "AVERAGE"))
        self.label_5.setText(_translate("Dialog", "HIGHEST"))
        self.label_6.setText(_translate("Dialog", "LOWEST"))
        self.pushButton.setText(_translate("Dialog", "REQUEST"))
        self.label_7.setText(_translate("Dialog", "START TIMESTAMP"))
        self.label_8.setText(_translate("Dialog", "END TIMESTAMP"))
        self.label_9.setText(_translate("Dialog", "30"))
        self.label_10.setText(_translate("Dialog", "NO. OF VALUES"))
        self.pushButton_2.setText(_translate("Dialog", "Test"))
        self.pushButton_2.clicked.connect(self.generate_graph) 
    
    def AMQP(self):
        connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        channel = connection.channel()


        channel.queue_declare(queue='hello')

        def callback(ch, method, properties, body):
           print(" [x] Received %r" % body)

        channel.basic_consume(callback, queue='hello', no_ack=True)

        print(' [*] Waiting for messages. To exit press CTRL+C')
        channel.start_consuming()
    
    def COAP_get(self):
        logging.basicConfig(level=logging.INFO)
        async def main():
           protocol = await Context.create_client_context()
        
           request = Message(code=GET, uri='coap://localhost/time')
        
        
        
           response = await protocol.request(request).response
           print('Result: %s\n%r'%(response.code, response.payload))
    
    
    def COAP_put(self):
        logging.basicConfig(level=logging.INFO)
        async def main():
           context = await Context.create_client_context()
           await asyncio.sleep(2)
           payload = b"The quick brown fox jumps over the lazy dog.\n" * 30
           request = Message(code=PUT, payload=payload, uri="coap://localhost/other/block")
           response = await context.request(request).response
           print('Result: %s\n%r'%(response.code, response.payload))
    
    # The callback for when the client receives a CONNACK response from the server.
    def MQTT(self):
    
        MQTT_SERVER = "localhost"
        MQTT_PATH = "test_channel"
        
        def on_connect(client, userdata, flags, rc):
           print("Connected with result code "+str(rc))
           # Subscribing in on_connect() means that if we lose the connection and
           # reconnect then subscriptions will be renewed.
           client.subscribe(MQTT_PATH)
            
            # The callback for when a PUBLISH message is received from the server.
        def on_message(client, userdata, msg):
           print(msg.topic+" "+str(msg.payload))
        client = mqtt.Client()
        client.on_connect = on_connect
        client.on_message = on_message     
        client.connect(MQTT_SERVER, 1883, 60)
        # Blocking call that processes network traffic, dispatches callbacks and
        # handles reconnecting.
        # Other loop*() functions are available that give a threaded interface and a
        # manual interface.
        client.loop_forever()
    
    
    def generate_graph(self):
        # this is for plotting purpose
        protocol = ['MQTT','COAP','WEBSOCKET','AMQP']    
        time = [100,101,110,115]
        index = np.arange(len(protocol))
        plt.bar(index, time)
        plt.xlabel('PROTOCOL', fontsize=5)
        plt.ylabel('TIME IN SECONDS', fontsize=5)
        plt.xticks(index, protocol, fontsize=5, rotation=0)
        plt.title('Time for different protocols in seconds')
        plt.show()
        
    def websocket(self):
        @asyncio.coroutine
        def hello():
           websocket = yield from websockets.connect('ws://localhost:8765/')

        try:
           name = input("What's your name? ")

           yield from websocket.send(name)
           print("> {}".format(name))

           greeting = yield from websocket.recv()
           print("< {}".format(greeting))

        finally:
           yield from websocket.close()

        asyncio.get_event_loop().run_until_complete(hello())


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    
    #global count
    sys.exit(app.exec_())

