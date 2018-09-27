import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot


from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

import Adafruit_DHT
temperature_old=0;
humidity_old=0;
 
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
    button.clicked.connect(self.graph0)
        
    button1 = QPushButton('Humidity stats', self)
    button1.setToolTip('This is an example button')
    button1.move(40,120) 
    button1.clicked.connect(self.graph1)
    self.show()

  def displayValue(self):
    humidity, temperature = Adafruit_DHT.read_retry(22,4)
    if humidity is not None and temperature is not None:
#        self.label_3.setText(str(temperature) + "C")
#        self.label_4.setText(str(humidity) + "%" ) 
        print("temperature is :"+ str(temperature)+ "C")
        print("humidity is :"+ str(humidity)+ "%")


  def graph0(self):
    X = [590,540,740,130,810,300,320,230,470,620,770,250]
    Y = [32,36,39,52,61,72,77,75,68,57,48,48]

    plt.scatter(X,Y)

    plt.title('Temperature values at given time intervals')
    plt.show()


  def graph1(self):
    X = [590,540,740,130,810,300,320,230,470,620,770,250]
    Y = [32,36,39,52,61,72,77,75,68,57,48,48]

    plt.scatter(X,Y)

    plt.title('Humidity values at given time intervals')
    plt.show()
    
    
  def showtemp(self):
    humidity, temperature = Adafruit_DHT.read_retry(22,4)
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Information)

    msg.setText("You have selected the option to see temperature.The device is properly connected")
    msg.setInformativeText("This is additional information")
    msg.setWindowTitle("MessageBox demo")
    msg.setDetailedText("The temperature is : " + str(temperature) +" "+"C")
    msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

	
    retval = msg.exec_()
    print ("value of pressed message box button:" + str(retval))

  def showhumidity(self):
    humidity, temperature = Adafruit_DHT.read_retry(22,4)
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Information)

    msg.setText("You have selected the option to see humidity.The device is properly connected")
    msg.setInformativeText("This is additional information")
    msg.setWindowTitle("MessageBox demo")
    msg.setDetailedText("The humidity is : " + str(humidity) +" "+"%")
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