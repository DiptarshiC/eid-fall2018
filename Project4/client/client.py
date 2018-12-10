# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CLIENT.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!


#Project made by Diptarshi Chakraborty
#
#Python file for client.py
#
#The file reads from queue and makes a plot comparing the times
#for the data transaction to take place
#


import boto3
import threading
import sys
import time
import ast
import logging
import asyncio
import datetime
import re





import aiocoap
from aiocoap import *

import paho.mqtt.client as mqtt

import asyncio
import websockets

from websocket import create_connection
from matplotlib import pyplot as plt

import pika

import matplotlib.pyplot as plt


from PyQt5 import QtCore, QtGui, QtWidgets

from numpy import array

import numpy as np



temp=0
hum=0
count=0
max_temp=0
min_temp=0
max_hum=0
min_hum=0
average_temp=0
C_flag=0
average_hum=0
avg_click=0
starttime=""
endtime=""  


value_temp=[]
value_hum=[]



central_list=[]






message_list = []

client = mqtt.Client()
mqtt_end_time=[]

#the function for my User interface

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
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 450, 101, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        
        
        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(120, 450, 101, 31))
        self.pushButton_4.setObjectName("pushButton_3")
        
        
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(220, 450, 101, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
    
    #the function for translating the UI
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
        self.pushButton_3.setText(_translate("Dialog", "C to F"))
        self.pushButton_4.setText(_translate("Dialog", "F to C"))
        self.pushButton_3.clicked.connect(self.farenheit_flag)
        self.pushButton_4.clicked.connect(self.celcius_flag)
        #self.pushButton_2.clicked.connect(self.temperature_graph)
        #message_list.append(30)
        #message_list.append(40)
        #message_list.append(50)
        self.pushButton_2.clicked.connect(self.test_protocols)
        
    #function for celcius
    def celcius_flag(self):
        global C_flag
        C_flag=0
    #function for farenheit   
    def farenheit_flag(self):
        global C_flag
        C_flag=1
    
    #
    #function to request values from the queue
    #
    #plots a graph for the various values of data
    #
    #
    #
    #
    #
    #
    
    def myfunction(self):
        global value_temp
        global value_hum
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
                   aws_access_key_id='ASIAXA4WY5JYL35ZC5B7',
                   aws_secret_access_key='2XJNz9s5Z/UJdqHONOwbtIr9eMJNlvTqkCMuDy64',
                   aws_session_token='FQoGZXIvYXdzEG0aDB1bvlTIKd+JZe5DFiLkAjMINyqMbjvoxRmszxKzeAhNuQiJfxT1ndOKfjPmOYNP1mmpJL6G6YqDhvbNsVB8BnMkhfnD42ojrSBK2/MhqitbjyfI9R4pO6XfAy6Q4B93UzjfEZl33jftkikmtP9MY+HDUeTLSOMLyKAJ3cJzaXSJFGe9z1KTOa6I3e/I71f8M+IjIXneW3ZMkI0GUykom6D5AlPMfKzQ3Fp5u6AMdiFicps1DOLNJDT2J+EhPduePz54ZkxqagFWF3N5qXSwJV7ifw8KwhuivjUyHN3KSaF7HMF9iXvjtfnqnDCYvPIbrOAFuArGpbw4bpcDZyXn+ZtHIlxqLj5RhaDtX32b3gfVN6ptY4z/GneSKE9cRlZk/nKVIl4pEM5ufxBfkh798yIqAv7yYHvQfS5VLHMDSFhTGqBbkjHLwi0eZxYQ7VzZFhWsdR894AY0y9da9ME/HT2EaOnxz7YgWGP52KFpZo2TVtgZKJ3xuuAF')                          
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

        for i in range (0,1):
        
        
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
             if(C_flag==1):
                temp=(9/5)*temp + 32
             value_temp.append(int(temp))
             TEMP = "%2.0f" % temp
             self.progressBar.setProperty("value", TEMP)
             
             average_temp=float(average_temp[0])
             if(C_flag==1):
                average_temp=(9/5)*average_temp + 32
             value_temp.append(int(average_temp))
             AVG_TEMP="%2.0f" % average_temp
             self.progressBar_7.setProperty("value", AVG_TEMP)
             
             max_temp=float(max_temp[0])
             if(C_flag==1):
                max_temp=(9/5)*max_temp + 32
             value_temp.append(int(max_temp))
             MAX_TEMP="%2.0f" % max_temp
             self.progressBar_2.setProperty("value", MAX_TEMP)
             
             min_temp=float(min_temp[0])
             if(C_flag==1):
                min_temp=(9/5)*min_temp + 32
             value_temp.append(int(min_temp))
             MIN_TEMP="%2.0f" % min_temp
             self.progressBar_5.setProperty("value", MIN_TEMP)
             
             
             
             
             hum=float(hum[0])
             value_hum.append(int(hum))
             hum = "%2.0f" % hum
             self.progressBar_3.setProperty("value", hum)
             
             average_hum=float(average_hum[0])
             value_hum.append(int(average_hum))
             AVG_HUM="%2.0f" % average_hum
             self.progressBar_8.setProperty("value", AVG_HUM)
             
             max_hum=float(max_hum[0])
             value_hum.append(int(max_hum))
             MAX_HUM="%2.0f" % max_hum
             self.progressBar_4.setProperty("value", MAX_HUM)
             
             min_hum=float(min_hum[0])
             value_hum.append(int(min_hum))
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
             
             # graph of temperature and humidity values 
             #field = ['TEMP','HUMIDITY','MAX TEMP','MAX HUM', 'MIN TEMP', 'MIN HUM', 'AVG TEMP','AVG HUM']    
             #value = [100,101,110,115,115,120,115,120]
             #index = np.arange(len(field))
             #plt.bar(index, value)
             #plt.xlabel('TEMP_HUM', fontsize=5)
             #plt.ylabel('value of fields', fontsize=5)
             #plt.xticks(index, field, fontsize=5, rotation=0)
             #plt.title('Time for different fields')
             #plt.show()
             
             #global value_temp
             field = ['TEMP','AVG_TEMP','MAX_TEMP','MIN_TEMP','HUM','AVG_HUM','MAX_HUM','MIN_HUM']
             merged_list=value_temp+value_hum
             merged_list1=merged_list.copy()
             message_list.append(merged_list)
             #message_list.append(40)
             #message_list.append(50)
             merged_list=[]
             value_temp=[]
             value_hum=[]
             field1 = np.array(field)
             n=len(field1)    
             index = np.arange(n)
             #plt.plot(index, merged_list1)
             plt.plot(merged_list1)
             #plt.xlabel('TEMP_HUM', fontsize=5)
             #plt.plot(field,merged_list)
             plt.xlabel('TEMP            AVG_TEMP             MAX_TEMP             MIN_TEMP             HUM             AVG_HUM             MAX_HUM             MIN_HUM', fontsize=5)
             #plt.ylabel('value of fields', fontsize=5)
             #plt.xticks(index, field, fontsize=5, rotation=0)
             #plt.title('Time for different fields')
             plt.show()
             
             
             
             
             
             
             
             
              
    def temp_graph(self):
        global value_temp
        field = ['TEMP','AVG_TEMP','MAX_TEMP','MIN_TEMP']    
        index = np.arange(len(field))
        plt.bar(index, value_temp)
        plt.xlabel('TEMP', fontsize=5)
        plt.ylabel('value of fields', fontsize=5)
        plt.xticks(index, field, fontsize=5, rotation=0)
        plt.title('Time for different fields')
        plt.show()
        
        
    def hum_graph(self):
        global value_hum
        field = ['HUM','AVG_HUM','MAX_HUM','MIN_HUM']    
        index = np.arange(len(field))
        plt.bar(index, value_hum)
        plt.xlabel('HUM', fontsize=5)
        plt.ylabel('value of fields', fontsize=5)
        plt.xticks(index, field, fontsize=5, rotation=0)
        plt.title('Time for different fields')
        plt.show()
        
    #
    #Actual test of protocols takes place here
    #
    #measures time for exchange of each transaction
    #
    #Sends message and for each transaction records the return time
    #
    #plots time for each message exchange
    #         
    
    def test_protocols(self):
        """
        Test all three protocols
        """
        global total_time_websocket
        global total_time_mqtt
        global total_time_coap
        global message_list,mqtt_end_time
        websockets_rtt = []
        mqtt_start_time=[]
        mqtt_rtt = []
        coap_rtt = []
        mqtt_end_time = []
    
        ip = "128.138.189.119"
    
        #WEBSOCKETS
    
        ws = create_connection("ws://" + ip + ":8888/ws")
        for i in range(0,len(message_list)):
           web_t1 = time.time() #start time for message transmission
           ws.send(str(message_list[i])) #send message
           result =  ws.recv() #received message from server
           web_t2 = time.time() #end time for message reception
           websockets_rtt.append(web_t2 - web_t1) #compute round thow to empty list in pythonrip time
           print("\nWebSocket Data:\n")
           print(result)
           print('WebSocket round trip time in seconds: %s'% websockets_rtt[i])
        
        #MQTT
        up_topic = 'mqtt_upstream'
        down_topic = 'mqtt_downstream'

        threads = []
        msg_event = threading.Event()
        mqtt_thread = threading.Thread(target=mqtt_server) #client operates as mqtt server
        threads.append(mqtt_thread)
        mqtt_thread.daemon = True
        mqtt_thread.start()
        time.sleep(1) #required for MQTT to operate
        
        #Send and receive individual messages and time each transfer
        
        for i in range(0,len(message_list)):
           print(i)
           mqtt_start_time.append(time.time())
           client.publish(up_topic, str(message_list[i]))
           client.subscribe(down_topic)
           time.sleep(1)

        print(len(mqtt_end_time))
        print(len(mqtt_start_time))
     
     
     
        # Compute transfer times 
        for i in range(0,len(mqtt_end_time)):
           mqtt_rtt.append(float(mqtt_end_time[i])-float(mqtt_start_time[i+(len(mqtt_start_time)-len(mqtt_end_time))]))
        
        #COAP
        for i in range(0,len(message_list)):
           coap_t1 = time.time()
           CoAPhandler(i)
           coap_t2 = time.time()
           coap_rtt.append(coap_t2 - coap_t1)
           print('CoAP round trip time in seconds: %s'% coap_rtt[i])
        
        total_time_websockets=sum(websockets_rtt)*10+7 
        total_time_mqtt=sum(mqtt_rtt)*10
        total_time_coap=sum(coap_rtt)*10+12
        print(websockets_rtt)
        print(mqtt_rtt)
        print(coap_rtt)
        #plt.plot([total_time_websockets,  total_time_mqtt, total_time_coap])
        plt.xlabel('WEBSOCKETS                               MQTT                               COAP')
        plt.plot(websockets_rtt)
        plt.plot(mqtt_rtt)
        plt.plot(coap_rtt)  
        plt.show()

#functions specific to each protocol
#
#activates server and loop time
#
#calculates difference    
    
def mqtt_server():
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect("test.mosquitto.org",1883,60)
    client.loop_forever()
    
def on_connect(client, userdata, flags, rc): #MQTT on_connect routine
    print("Connected with result code "+str(rc))
        
        
def on_message(client, userdata, msg): #MQTT on_message routine
    global mqtt_end_time
    print("Client"+str(msg.payload))
    mqtt_end_time.append(time.time())        
        
def CoAPhandler(i): #handler for COAP transfers
    global message_list
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(coapPUT(str(message_list[i])))
    return 0    
    
async def coapPUT(data): #function to transfer data using COAP
    context = await aiocoap.Context.create_client_context()
        
    request = aiocoap.Message(code=PUT, payload=bytes(data, 'utf-8'))
        
    request.opt.uri_host = "128.138.189.119"
    request.opt.uri_path = ("other", "block")
    response = await context.request(request).response
    print('Result: %s\n%r'%(response.code, response.payload))

    
    
    
    
    
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

#
#
#main function that executes application
#
#
#


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    
    #global count
    sys.exit(app.exec_())

