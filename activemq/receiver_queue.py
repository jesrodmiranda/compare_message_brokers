import time
import sys
import stomp


class MyListener(stomp.ConnectionListener):
    def on_error(self, headers, message):
        print('received an error "%s"' % message)

    def on_message(self, headers, message):
        print('received a message "%s"' % message)


hosts = [('localhost', 61613)]
conn = stomp.Connection(host_and_ports=hosts)
conn.set_listener('', MyListener())
conn.connect('admin', 'admin', wait=True)

conn.subscribe(destination='/queue/muy_test', id='1', ack='auto')

conn.send(body=' '.join(sys.argv[1:]), destination='/queue/muy_test')

time.sleep(2)
conn.disconnect()
