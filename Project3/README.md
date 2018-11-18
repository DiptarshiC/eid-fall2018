#Project3 

This project has been done by Diptarshi Chakraborty and Nagarjuna.

It consists of a client and server. The server consists of a GUI application and a system
that senses the external temeprature every 5 seconds. It is stored in the local machine
as .csv files. It connects to a AWS IOT thing. The AWS IOT thing using a lambda function 
passes the data onto a SQS queue. The client then reads the data from the SQS queue
using a python script.

I looked at AWS educate for references. 

1.https://docs.aws.amazon.com/lambda/latest/dg/with-sqs-example.html

2. https://docs.aws.amazon.com/lambda/latest/dg/get-started-create-function.html 
