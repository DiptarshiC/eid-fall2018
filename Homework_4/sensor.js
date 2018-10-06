/*
@Filenmame:sensor.js

@description:A javascript code for reading dht22 sensor every 10 secs
		
@author:Diptarshi Chakraborty.node version is 8.12.0.Referenced from https://github.com/momenso/node-dht-sensor	

@Date:6th October 2018
*/



var sensorLib = require("node-dht-sensor");
var temp;
var htemp=0;
var ltemp;
var hum;
var hhum=0;
var lhum;
var count=1;
var avg_temp=0;;
var avg_hum=0;
var sensor = {
    sensors: [ {
        name: "Temp",
        type: 22,
        pin: 4
    } ],      
    read: function() {
        for (var a in this.sensors) {
       	
            var b = sensorLib.read(this.sensors[a].type, this.sensors[a].pin);
            temp=((9/5)*b.temperature.toFixed(1))+32;
            hum=b.humidity.toFixed(1);
            temp=Math.round(temp*10)/10;
            hum=Math.round(hum*10)/10;
            if(count==1)
            {
            	ltemp=temp;
             	lhum=hum;
            }
            
            console.log(count +" "+this.sensors[a].name + " " +
              temp + " degF, " +
              b.humidity.toFixed(1) + "% Hum");
              
              count=count+1;
              avg_temp=avg_temp+temp;
              avg_hum=avg_hum+hum;
              if(temp>htemp)
              {
              	htemp=temp;
              }
           
              if(hum>hhum)
              {
              	hhum=hum;
              }
              if(temp<ltemp)
              {
              	ltemp=temp;
              }
           
              if(hum<lhum)
              {
              	lhum=hum;
              }
              
              if(count==11)
		{
			
			console.log("highest temperature : "+htemp+" degF");
              		console.log("highest humidity : "+hhum+"%");
              		console.log("lowest temperature : "+ltemp+" degF");
              		console.log("lowest humidity : "+lhum+"%");
              		avg_temp=Math.round(avg_temp*10)/10;
                        avg_hum=Math.round(avg_hum*10)/10;
                        avg_hum=avg_hum.toFixed(1);
              		console.log("avg temperature : "+(avg_temp)/(10)+" degF");
              		console.log("avg humidity : "+(avg_hum)/(10)+"%");
              		avg_temp=0;
              		avg_hum=0;
              		count=1;
              		
		}        
        }
        setTimeout(function() {
            sensor.read();
        }, 10000);
    }
};

sensor.read();

