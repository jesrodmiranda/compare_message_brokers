#!/usr/bin/env python

import pika
import sys

i = sys.argv[1]

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

# channel.queue_declare(queue='test_exchange', durable=True)

message = ' '.join(sys.argv[1:]) or b"A test message to MUY!"
channel.basic_publish(
    exchange='test_exchange',
    routing_key='',
    body=message,
    properties=pika.BasicProperties(
        expiration='10000',
        priority=1,
        headers={
            "x-retries": 2
        }
    ))
print(" [x] Sent %r" % message)

connection.close()
