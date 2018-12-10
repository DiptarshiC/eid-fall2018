#!/bin/bash

echo "running coap"
python3 coap_server.py & 
echo "running mqtt"
python3 mqtt_server.py &
echo "running web"
python3 websocket_server.py &

