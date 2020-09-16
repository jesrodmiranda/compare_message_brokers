import time
import sys
import logging
import stomp
from stomp import ConnectionListener

queue_name = sys.argv[1]

logging.basicConfig(level=logging.DEBUG)


class MuyTestListener(ConnectionListener):
    message_count = 0

    def on_error(self, headers, message):
        print('received an error %s' % message)

    def on_message(self, headers, message):
        print(headers)
        print(str(message))
        print(type(message))
        print("Message %d" % self.message_count)
        self.message_count = self.message_count + 1
        print('received a message ...%s...' % message)


conn = stomp.Connection()
conn.set_listener('', MuyTestListener())
conn.connect('admin', 'admin', wait=True)

i = 0
while 1:
    queue = '/queue/%s' % queue_name
    print("Queue is [%s]" % queue)
    print("subscribe: %s" % conn.subscribe)
    i += 1
    conn.subscribe(destination=queue, id='123421' + str(i), ack='auto')
    time.sleep(0.5)
