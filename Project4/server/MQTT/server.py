import paho.mqtt.publish as publish
 
MQTT_SERVER = "128.138.189.119"
MQTT_PATH = "test_channel"
while True: 
  publish.single(MQTT_PATH, "Hello World!", hostname=MQTT_SERVER)