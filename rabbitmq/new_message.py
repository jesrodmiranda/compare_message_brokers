#!/usr/bin/env python

import pika
import sys

i = sys.argv[1]

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='muy_task_queue', durable=True)

message = ' '.join(sys.argv[1:]) or b"A test message to MUY!"
channel.basic_publish(
    exchange='',
    routing_key='muy_task_queue',
    body=message,
    properties=pika.BasicProperties(
        delivery_mode=2,  # make message persistent
    ))
print(" [x] Sent %r" % message)

connection.close()
