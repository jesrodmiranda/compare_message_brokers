import time
import sys
import stomp


class MyListener(stomp.ConnectionListener):
    def on_error(self, headers, message):
        print('received an error "%s"' % message)

    def on_message(self, headers, message):
        print('received a message "%s"' % message)


host = "localhost"
port = 61613

hosts = [(host, port)]
conn = stomp.Connection(host_and_ports=hosts)
conn.set_listener('', MyListener())
conn.connect('admin', 'admin', wait=True)

conn.subscribe(destination='/queue/workshop.queueA', id='1', ack='auto')

conn.send(body=' '.join(sys.argv[1:]), destination='/queue/workshop.queueA')

time.sleep(2)
conn.disconnect()
