import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot


from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import datetime


import Adafruit_DHT
temperature_old=0
humidity_old=0
count_temp=0;
count_humidity=0
temperature_avg=0
humidity_avg=0
temperature_tot=0
humidity_tot=0
 
class App(QWidget):

  
  
 
  def __init__(self):
    super().__init__()
    self.title = 'Temperature and Humidity Interface by Chakraborty Electronics'
    self.left = 10
    self.top = 10
    self.width = 500
    self.height = 300
    self.initUI()
 
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

  def displayValue(self):
    humidity, temperature = Adafruit_DHT.read_retry(22,4)
    if humidity is not None and temperature is not None:
#        self.label_3.setText(str(temperature) + "C")
#        self.label_4.setText(str(humidity) + "%" ) 
        print("temperature is :"+ str(temperature)+ "C")
        print("humidity is :"+ str(humidity)+ "%")


  def temp_graph(self):
    temp_ts = [590,540,740,130,810,300,320,230,470,620,770,250]
    temp = [32,36,39,52,61,72,77,75,68,57,48,48]

    plt.scatter(temp_ts,temp)

    plt.title('Temperature values at given time intervals')
    plt.show()


  def humidity_graph(self):
    hum_ts = [590,540,740,130,810,300,320,230,470,620,770,250]
    hum = [32,36,39,52,61,72,77,75,68,57,48,48]

    plt.scatter(hum_ts,hum)

    plt.title('Humidity values at given time intervals')
    plt.show()
    
    
  def showtemp(self):
    global temperature_old
    global count_temp
    global temperature_avg
    global temperature_tot
    global temp_ts
    global temp
    humidity, temperature = Adafruit_DHT.read_retry(22,4)
    if humidity is not None and temperature is not None:
      now = datetime.datetime.now()
      count_temp=count_temp+1
      temperature_tot=temperature_tot+temperature
      temperature_avg=(temperature_tot)/(count_temp)
      print (now.strftime("%H:%M:%S"))
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

  def showhumidity(self):
    global humidity_tot
    global humidity_avg
    global count_humidity
    global hum_ts
    global hum
    humidity, temperature = Adafruit_DHT.read_retry(22,4)
    if humidity is not None and temperature is not None:
      count_humidity=count_humidity+1
      humidity_tot=humidity_tot+humidity
      humidity_avg=(humidity_tot)/(count_humidity)
      now = datetime.datetime.now()
      print (now.strftime("%H:%M:%S"))
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

  
 
  @pyqtSlot()
  def on_click(self):
    print('PyQt5 button click')
  def Taali_maaro(self):
    print('De taali') 
  def plot(self):
    ax = plt.subplot(111)

    t = np.arange(0.0, 5.0, 0.01)
    s = np.cos(2*np.pi*t)
    line, = plt.plot(t, s, lw=2)

    plt.annotate('local max', xy=(2, 1), xytext=(3, 1.5),
            arrowprops=dict(facecolor='black', shrink=0.05),
            )

    plt.ylim(-2,2)
    plt.show() 
   
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())