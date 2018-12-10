

#Python routine to implement MQTT server using paho


#
#
#Adapted from example
#
#Written by Diptarshi Chakraborty
#



import paho.mqtt.client as mqtt
import threading

def mqtt_server():
    client.connect("test.mosquitto.org",1883,60) #Public MQTT broker
    client.on_connect = on_connect
    client.on_message = on_message
    client.loop_forever()
    
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe(up_topic)

def on_message(client, userdata, msg):
    print("Server "+str(msg.payload))
    client.publish(down_topic, msg.payload); #echo received message back to client
    
up_topic = 'mqtt_upstream'
down_topic = 'mqtt_downstream'

client = mqtt.Client()
mqtt_server()