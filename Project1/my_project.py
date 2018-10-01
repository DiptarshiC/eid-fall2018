##
#@Filenmame:myproject.py
#
#@description:A python code using QT5 libraries to make an interface
#	for reading the DHT22 temperature and humidity sensor	
#
#@author:Diptarshi Chakraborty. Sources from which I have consulted
#	www.pythonspot.com
#
#@Date:30th September 2018

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot


from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import datetime
import pylab as pl
from matplotlib.ticker import StrMethodFormatter







import Adafruit_DHT
temperature_old=0
humidity_old=0
count_temp=0;
count_humidity=0
temperature_avg=0
humidity_avg=0
temperature_tot=0
humidity_tot=0
temp_ts={}

hum_ts={}
temp_list=[]
hum_list=[]

class App(QWidget):

##
#@Function:__init__(self)
#
#@description:A function to initialize the interface
#		and to set its size
#
#@parameters:self
#	
#@return:none
#  
  
 
  def __init__(self):
    super().__init__()
    self.title = 'Temperature and Humidity Interface by Chakraborty Electronics'
    self.left = 10
    self.top = 10
    self.width = 500
    self.height = 300
    self.initUI()
##
#@Function:__init__(self)
#
#@description:A function to put buttons and GUI
#		elements in the given interface
#		that connects to the other functions
#
#@parameters:self
#	
#@return:none
#  

 
  def initUI(self):
    self.setWindowTitle(self.title)
    self.setGeometry(self.left, self.top, self.width, self.height) 

    button = QPushButton('Request Current Temperature  ', self)
    button.setToolTip('This is an example button')
    button.move(40,30) 
    button.clicked.connect(self.showtemp)

    button = QPushButton('Request Current Humidity        ', self)
    button.setToolTip('This is an example button')
    button.move(40,60) 
    button.clicked.connect(self.showhumidity)
  
    button = QPushButton('Temperature stats', self)
    button.setToolTip('This is an example button')
    button.move(40,90) 
    button.clicked.connect(self.temp_graph)
        
    button1 = QPushButton('Humidity stats', self)
    button1.setToolTip('This is an example button')
    button1.move(40,120) 
    button1.clicked.connect(self.humidity_graph)
    self.show()

##
#@Function:temp_graph(self)
#
#@description:A function to create and display the temperature
#		graph
#
#@parameters:self
#	
#@return:none
#  
  


  def temp_graph(self):
    #temp_ts = [590,540,740,130,810,300,320,230,470,620,770,250]
    #temp = [32,36,39,52,61,72,77,75,68,57,48,48]
    time0 = list(temp_ts.keys())
    values0 = list(temp_ts.values())
    plt.xticks(temp_list, time0)
    plt.plot(temp_list,values0)
    #self.set_xticklabels([ time0(x) for x in time0])
    plt.title('Temperature values at given timestamps')
    
    plt.show()

##
#@Function:humidity_graph(self)
#
#@description:A function to create and display the humidity
#		graph
#
#@parameters:self
#	
#@return:none
#  



  def humidity_graph(self):
    #hum_ts = [590,540,740,130,810,300,320,230,470,620,770,250]
    #hum = [32,36,39,52,61,72,77,75,68,57,48,48]
    time1 = list(hum_ts.keys())
    values1 = list(hum_ts.values())
    
    plt.xticks(hum_list, time1)
    plt.plot(hum_list,values1)
    #self.set_xticklabels([ time1(x) for x in time1])
    plt.title('Humidity values at given time stamps')
    plt.show()
##
#@Function:showtemp
#
#@description:A function to a window to display temperature
#		
#
#@parameters:self
#	
#@return:temperature
#  

    
  def showtemp(self):
    global temperature_old
    global count_temp
    global temperature_avg
    global temperature_tot
    global temp_ts
    global temp
    humidity, temperature = Adafruit_DHT.read_retry(22,4)
    #temperature=round(temperature,2)
    if humidity is not None and temperature is not None:
      now = datetime.datetime.now()
      count_temp=count_temp+1
      temp_list.append(count_temp)
      temperature_tot=temperature_tot+temperature
      temperature_avg=(temperature_tot)/(count_temp)
      print (now.strftime("%H:%M:%S"))
      #temp_ts.append(now.strftime("%H:%M:%S"))
      #temp.append(temperature)
      temp_ts[now.strftime("%H:%M:%S")] = temperature
      msg = QMessageBox()
      msg.setIcon(QMessageBox.Information)

      msg.setText("You have selected the option to see temperature.The sensor is properly connected")
      msg.setInformativeText("To see the temperature click on show details")
      msg.setWindowTitle("MessageBox demo")
      msg.setDetailedText("The temperature is : " + str(temperature) +" "+"C at "+now.strftime("%H:%M:%S"))
      msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
    else:
      now = datetime.datetime.now()
      print (now.strftime("%H:%M:%S"))
      msg = QMessageBox()
      msg.setIcon(QMessageBox.Information)

      msg.setText("The sensor is disconnected")
      msg.setInformativeText("Click on show details to see avg temperature")
      msg.setWindowTitle("MessageBox demo")
      msg.setDetailedText("The temperature is : " + str(temperature_avg) +" "+"C at "+now.strftime("%H:%M:%S"))
      msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel) 

	
    retval = msg.exec_()
    print ("value of pressed message box button:" + str(retval))
##
#@Function:humidity_graph
#
#@description:A function to a window to display humidity
#		
#
#@parameters:self
#	
#@return:humidity
#  

  def showhumidity(self):
    global humidity_tot
    global humidity_avg
    global count_humidity
    global hum_ts
    global hum
    humidity, temperature = Adafruit_DHT.read_retry(22,4)
    #humidity=round(humidity,2)
    if humidity is not None and temperature is not None:
      count_humidity=count_humidity+1
      hum_list.append(count_humidity)
      humidity_tot=humidity_tot+humidity
      humidity_avg=(humidity_tot)/(count_humidity)
      now = datetime.datetime.now()
      print (now.strftime("%H:%M:%S"))
      #hum_ts.append(now.strftime("%H:%M:%S"))
      #hum.append(humidity)
      hum_ts[now.strftime("%H:%M:%S")] = humidity
      msg = QMessageBox()
      msg.setIcon(QMessageBox.Information)

      msg.setText("You have selected the option to see humidity.The sensor is properly connected")
      msg.setInformativeText("To see the humidity click on show details")
      msg.setWindowTitle("MessageBox demo") 
      msg.setDetailedText("The humidity is : " + str(humidity) +" "+"% at "+now.strftime("%H:%M:%S"))
      msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
    else:
      now = datetime.datetime.now()
      print (now.strftime("%H:%M:%S"))
      msg = QMessageBox()
      msg.setIcon(QMessageBox.Information)

      msg.setText("The sensor is disconnected")
      msg.setInformativeText("Click on show details to see avg humidity")
      msg.setWindowTitle("MessageBox demo") 
      msg.setDetailedText("The humidity is : " + str(humidity_avg) +" "+"% at "+now.strftime("%H:%M:%S"))
      msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

	
    retval = msg.exec_()
    print ("value of pressed message box button:" + str(retval))

  
 
  
   
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())