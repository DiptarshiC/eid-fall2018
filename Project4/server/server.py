import tornado.httpserver
import tornado.websocket
import tornado.ioloop
import tornado.web
import socket
import csv
'''
This is a simple Websocket Echo server that uses the Tornado websocket handler.
Please run `pip install tornado` with python of version 2.7.9 or greater to install tornado.
This program will echo back the reverse of whatever it recieves.
Messages are output to the terminal for debuggin purposes. 
'''
temp=0
hum=0
temp_avg=0
hum_avg=0
temp_high=0
hum_high=0
temp_low=18
hum_low=19
flag=0
date=""
time=""


def hulla(self):
    global temp_high        
    with open('temp_high.csv', mode='r') as Temp_high:
        reader = csv.reader(Temp_high)
        for row in reader:
            temp_high = float(row[0])
            print(temp_high)

 
def tempf(self):
    global temp        
    with open('temp.csv', mode='r') as Temp:
        reader = csv.reader(Temp)
        for row in reader:
            temp = float(row[0])
            print(temp)
        
def humf(self):
    global hum        
    with open('hum.csv', mode='r') as Hum:
        reader = csv.reader(Hum)
        for row in reader:
            hum = float(row[0])
            print(hum)

def tempf_avg(self):
    global temp_avg        
    with open('temp_avg.csv', mode='r') as Temp_avg:
        reader = csv.reader(Temp_avg)
        for row in reader:
            temp_avg = float(row[0])
            print(temp_avg)    
        
def humf_avg(self):
    global hum_avg        
    with open('hum_avg.csv', mode='r') as Hum_avg:
        reader = csv.reader(Hum_avg)
        for row in reader:
            hum_avg = float(row[0])
            print(hum_avg)    
        

        
def tempf_low(self):
    global temp_low        
    with open('temp_low.csv', mode='r') as Temp_low:
        reader = csv.reader(Temp_low)
        for row in reader:
            temp_low = float(row[0])
            print(temp_low)
        
def humf_high(self):
    global hum_high        
    with open('hum_high.csv', mode='r') as Hum_high:
        reader = csv.reader(Hum_high)
        for row in reader:
            hum_high = float(row[0])
            print(hum_high)
             
def humf_low(self):
    global hum_low        
    with open('hum_low.csv', mode='r') as Hum_low:
        reader = csv.reader(Hum_low)
        for row in reader:
            hum_low = float(row[0])
            print(hum_low)                      

def datef(self):
    global date
    with open('date.csv', mode='r') as Datef:
        reader = csv.reader(Datef)
        for row in reader:
            date = (row[0])
            print(date)   

def timef(self):
    global time
    with open('time.csv', mode='r') as Timef:
        reader = csv.reader(Timef)
        for row in reader:
            time = (row[0])
            print(time)          



 
class WSHandler(tornado.websocket.WebSocketHandler):
    def open(self):
        print ('new connection')
      
    def on_message(self, message):
        print ('message received:  %s' % message)
        if message=="CurrentTemp":
            tempf(self)
            datef(self)
            timef(self)
            self.write_message("1 "+str(temp)+ " " + str(date)+" "+str(time))
        if message=="CurrentHum":
            humf(self)
            datef(self)
            timef(self)
            self.write_message("2 "+str(hum)+ " " + str(date)+" "+str(time))    	
        if message=="Tempavg":
            tempf_avg(self)
            datef(self)
            timef(self)
            self.write_message("3 "+str(temp_avg)+ " " + str(date)+" "+str(time))  	
        if message=="Humavg":
            humf_avg(self)
            datef(self)
            timef(self)
            self.write_message("4 "+str(hum_avg)+ " " + str(date)+" "+str(time)) 
        if message=="Temphigh":
            hulla(self)
            datef(self)
            timef(self)
            self.write_message("5 "+str(temp_high)+ " " + str(date)+" "+str(time))
        if message=="Humhigh":
            humf_high(self)
            datef(self)
            timef(self)
            self.write_message("6 "+str(hum_high)+ " " + str(date)+" "+str(time))
        if message=="Templow":
            tempf_low(self)
            datef(self)
            timef(self)
            self.write_message("7 "+str(temp_low)+ " " + str(date)+" "+str(time))
        if message=="Humlow":
            humf_low(self)
            datef(self)
            timef(self)
            self.write_message("8 "+str(hum_low)+ " " + str(date)+" "+str(time))                     
            
 
    def on_close(self):
        print ('connection closed')
 
    def check_origin(self, origin):
        return True
 
application = tornado.web.Application([
    (r'/ws', WSHandler),
])
 
 
if __name__ == "__main__":
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(9111)
    myIP = socket.gethostbyname(socket.gethostname())
    print ('*** Websocket Server Started at %s***' % myIP)
    tornado.ioloop.IOLoop.instance().start()