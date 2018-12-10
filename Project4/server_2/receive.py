import sys 
import boto3
import json
import re

#import matplotlib.pyplot as plt
#import numpy as np
import time
import datetime

temp=0
hum=0
count=0
max_temp=0
min_temp=0
max_hum=0
min_hum=0
average_temp=0
average_hum=0


sqs = boto3.client('sqs', region_name = 'us-west-2',
                   aws_access_key_id='ASIAXA4WY5JYAYD3YO4E',
                   aws_secret_access_key='e1lK/8dN6KKcqRuItrK8AwQSUWFRuEykn+RxSEtb',
                   aws_session_token='FQoGZXIvYXdzEP3//////////wEaDPjA37WqJX/01kIkwiKEAtGErJD2TAjUzaWoYPIemqWEC3LwdJwlexPWVBu+fkmke7gu+YBr7tytNWE03cveDz9shmemcbBN72HPl/X5k+xyH+SOomSS+2UxIHpS9T0ZwvmsLxRE+XRCZFArNtqbbZM5dVoZCYXnChDDhj4UrJ+rjf/wDw31kG2aJ25rsc5FPmKvbFpIT0kDjhT+6ChCmxszYHG/M/AVaFtBqA6Kfrzo6+NBVaNWIWcwBjXNbJvBTp+8iXYLND/Jej0GFaESCQ0sK8XJeRbcQg76CdCnqE698V72wZfizy7JVQypKgh2hpL9WSLrtajICJxBoI4sna8ZO2FdcKiDbUM9p70Nhus/3Xe/KJDwsd8F')                   
url = sqs.get_queue_url(QueueName='RPI-3QUEUE.fifo')
print(url['QueueUrl'])
response = sqs.receive_message(QueueUrl =  url['QueueUrl'],AttributeNames= ['SentTimestamp'], MaxNumberOfMessages = 10, MessageAttributeNames=['All'], VisibilityTimeout = 0,WaitTimeSeconds = 5)

message = response['Messages'][0]
receipt_handle = message['ReceiptHandle']

response1 = sqs.receive_message( QueueUrl =  url['QueueUrl'], AttributeNames= ['SentTimestamp'], MaxNumberOfMessages = 10, MessageAttributeNames=['All'],VisibilityTimeout = 0, WaitTimeSeconds = 5)

message = response1['Messages'][0]
receipt_handle = message['ReceiptHandle']

response2 = sqs.receive_message(QueueUrl =  url['QueueUrl'],
AttributeNames= ['SentTimestamp'],MaxNumberOfMessages = 10, MessageAttributeNames=['All'], VisibilityTimeout = 0, WaitTimeSeconds = 0)

response['Messages'] = (response['Messages'] + response1['Messages'] + response2['Messages'])

for i in range (0,30):
     message = response['Messages'][i]
     #Spliting string and taking timestamp value
     body = response['Messages'][i]['Body']
     #print('\n The body content is %s' %body)
     
     x = body.split(",")
     
     str=x[0]
     num = re.findall('\d+',str)
     temp=num
     print('\nTemperature:%s' %num[0])
     
     str=x[1]
     num = re.findall('\d+',str)
     hum=num
     print('\nHumidity:%s' %num[0])
     
     str=x[2]
     num = re.findall('\d+',str)
     count=num
     print('\nCount:%s' %num[0])
     
     str=x[3]
     num = re.findall('\d+',str)
     max_temp=num
     print('\nMaximum Temperature:%s' %num[0])
     
     str=x[4]
     num = re.findall('\d+',str)
     min_temp=num
     print('\nMinimum_Temperature:%s' %num[0])
     
     str=x[5]
     num = re.findall('\d+',str)
     max_hum=num
     print('\nMaximum_Humidity:%s' %num[0])
     
     str=x[6]
     num = re.findall('\d+',str)
     min_hum=num
     print('\nMinimum_Humidity:%s' %num[0])
     
     str=x[7]
     num = re.findall('\d+',str)
     average_temp=num
     print('\nAverage_Temp:%s' %num[0])
     
     str=x[8]
     num = re.findall('\d+',str)
     average_hum=num
     print('\nAverage_Humidity:%s' %num[0])
     
##sqs.delete_message(QueueUrl =  url['QueueUrl'],receipt_handle = message['ReceiptHandle'])
    
