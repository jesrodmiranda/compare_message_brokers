import time
import sys
import logging
import stomp
import threading
from stomp import ConnectionListener

queue_name = sys.argv[1]

logging.basicConfig(level=logging.ERROR)


class MuyTestListener(ConnectionListener):
    message_count = 0

    def on_error(self, headers, message):
        print('received an error %s' % message)

    def on_message(self, headers, message):
        self.message_count = self.message_count + 1


conn = stomp.Connection()
conn.set_listener('', MuyTestListener())
conn.connect('admin', 'admin', wait=True)


def run_subscriber():
    t1 = time.time()
    y = 1
    queue = '/queue/%s' % queue_name
    while y <= 15000:
        y += 1
        conn.subscribe(destination=queue, id=str(y), ack='auto')
        # time.sleep(0.01)
        result = time.time() - t1
        if y % 15000 == 0:
            print(str(y) + ' msgs in ' + str(result) + ' ' + str(round(y / result)) + ' msg/s ')


i = 0
while i <= 5:
    x = threading.Thread(target=run_subscriber(), args=(1,))
    x.start()
    i += 1
