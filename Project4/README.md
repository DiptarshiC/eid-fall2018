# Project 4 : Protocol comparisons.

The repo for Project 4 created by Diptarshi Chakraborty.
This project builds upon Project 3. We have to compare the time taken by websockets, mqtt(without using aws)
and COAP for a full to and fro transaction from client to the server and back to the client.
For this the first steps are to ensure all three protocols have the proper brokers initialized on the
given system.After reading messages from the sqs queue on AWS, we ininitiate a test that run that
encapsulate the entire set of 8 values into a list and send it from the client to the server.The
server then sends the message back to the client. Below are the steps to install the various brokers
for the protocols. 


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













