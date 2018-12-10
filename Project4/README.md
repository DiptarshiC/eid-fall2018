# Project 4 : Protocol comparisons.

The repo for Project 4 created by Diptarshi Chakraborty.
This project builds upon Project 3. We have to compare the time taken by websockets, mqtt(without using aws)
and COAP for a full to and fro transaction from client to the server and back to the client.
For this the first steps are to ensure all three protocols have the proper brokers initialized on the
given system.After reading messages from the sqs queue on AWS, we ininitiate a test that run that
encapsulate the entire set of 8 values into a list and send it from the client to the server.The
server then sends the message back to the client. Below are the steps to install the various brokers
for the protocols.I have cited all the resources from where I have referred for the given project. Also
I would like to thank all my buddies who have tried to help me debug my code and told me workarounds where
I got stuck.

# 1. Steps to install websockets on the given system

The broker for websockets is the tornado webserver. The steps to install it is as follows :

sudo pip3 install Tornado


Tornado is a Python web framework and asynchronous networking library, originally developed 
at FriendFeed. By using non-blocking network I/O, Tornado can scale to tens of thousands of 
open connections, making it ideal for long polling, WebSockets, and other applications that 
require a long-lived connection to each user
You shall find a good examples for code in the following links :

1.https://gist.github.com/joewashear007/8276467
2.https://lowpowerlab.com/2013/01/17/raspberrypi-websockets-with-python-tornado/

# 2. Steps to install mqtt on the given webserver

The broker for mqtt is mosquito. The steps to install it are as follows :

sudo apt-get install mosquitto mosquitto-clients

sudo apt-get install python-pip3	

sudo pip3 install paho-mqtt

There are a number of MQTT brokers available for different machines.   
For this project, we have selected one of the most popular and stable brokers, 
MQTT-Mosquitto2“Mosquitto”.Note the two “t”’s in Mosquitto.

References for the given section are as shown below :

1.https://www.switchdoc.com/2018/02/tutorial-installing-and-testing-mosquitto-mqtt-on-raspberry-pi/

2.https://randomnerdtutorials.com/how-to-install-mosquitto-broker-on-raspberry-pi/


# 3. Steps to install the broker for COAP on the given webserver

The broker for COAP is aicoap. The steps to install the broker for it are given as follows:

pip3 install --upgrade "aiocoap[all]"

This step shall help you install all the relevant support we need for the given library.
Here are some given references that shall help you navigate through the code and play with it.

1. https://aiocoap.readthedocs.io/en/latest/examples.html

2. https://aiocoap.readthedocs.io/en/latest/api.html

3. https://packages.debian.org/sid/python3-aiocoap


Constrained Application Protocol (CoAP) is a specialized Internet Application Protocol for constrained devices, as defined in RFC 7252. 
It enables those constrained devices called "nodes" to communicate with the wider Internet using similar protocols. CoAP is designed for 
use between devices on the same constrained network (e.g., low-power, lossy networks), between devices and general nodes on the Internet, 
and between devices on different constrained networks both joined by an internet. CoAP is also being used via other mechanisms, such as SMS 
on mobile communication networks.


# Method of Protocol test

The steps to test individual protocol speeds are as follows :

1. First receive data from the sqs queue using the boto3 library.

2. Create a separate queue for every dataset. (8 fields)

3. Create a megaqueue using all the queues that you have

4. Create a button related to an 'event' that sends data to the respective servers, receives it 
   back and then measures the time differences for each data set
   
5. Add all the time for a particular protocol. This is the total time.

6. Plot a graph and measure the time difference.    


# How to build project

## Server

1. run start.sh that will pusblish to the queue

2. run coap_server.py websocket_server.py mqtt_server.py either as separate instances or via a single bash command

## Client

1. go to the folder 'client' 

1. run client.py

 





