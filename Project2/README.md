# Project 2 Repository

This project has been done by Diptarshi Chakraborty and Nagarjuna
It consists of a temperature and humidity sensor that display data
using a qt interface.

A server sends this data via websockets to a webpage, where a client
hosting the webpage receives the data.

Frameworks used for this project : QT designer, tornado, html, jquery
The server has been created using python 3.3

Steps to install tornado :
pip install tornado


Qt designer has already been isntalled in the previous project 

The adafruit package was used for sensing using the dht temperature and
humidity sensor

References

1. https://os.mbed.com/cookbook/Websockets-Server
2. http://www.tornadoweb.org/en/stable/
3. https://developer.rhino3d.com/guides/rhinopython/python-csv-file/