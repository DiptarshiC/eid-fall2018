var QUEUE_URL = 'https://sqs.us-west-2.amazonaws.com/482963155568/RPI-3QUEUE.fifo';
var AWS = require('aws-sdk');
var sqs = new AWS.SQS({region : 'us-west-2'});
var Temp=20;
var Hum=20;
var T_avg=0;
var H_avg=0;
var T_Max=23;
var T_Min=16;
var H_Max=20;
var H_Min=20;
var Count=20;
var T_avg0;
var H_avg0;
var T_Max0;
var T_Min0;
var H_Max0;
var H_Min0;
var Count0;
var event1;
var myobj;


exports.handler = function(event, context){
    
   // myObj=JSON.parse(event);
    Temp=event.Temperature;
    Hum=event.Humidity;
    Count=event.sequence;
    
    if(Temp>T_Max)
    {
        T_Max=Temp;
    }
    
    if(Hum>H_Max)
    {
        H_Max=Hum;
    }
    
    if(Temp<T_Min)
    {
        T_Min=Temp;
    }
    else
    T_Min=16;
    
    if(Hum<H_Min)
    {
        H_Min=Hum;
    }
    else
    H_Min=20;
    
    T_avg=(((T_avg*(Count+1))+Temp)/(Count+2));
    
    H_avg=(((H_avg*(Count+1))+Hum)/(Count+2));
    console.log(event.Temperature);
    console.log(event.Humidity);
    
    myobj={Temperature:Temp,Humidity:Hum,Counts:Count,Maximum_Temperature:T_Max,Minimum_Temperature:T_Min,Maximum_Humidity:H_Max,Minimum_Humidity:H_Min,Temperature_Avg:T_avg,Humidity_Avg:H_avg};
    
    
    
    
    
    
    
    var params = {
        MessageBody: JSON.stringify(myobj),
        QueueUrl: QUEUE_URL,
        MessageGroupId: 'STRING_VALUE',
        
           
        
    };
    sqs.sendMessage(params, function(err, data)
    {
        if(err)
        {
            console.log('error:',"Fail Send Message" + err);
            context.done('error',"ERROR Put SQS"); //Error with message
        }
        else
        {
            console.log('data:',data.MessageId);
            context.done(null,''); //SUCCESS
        }
    })
}

