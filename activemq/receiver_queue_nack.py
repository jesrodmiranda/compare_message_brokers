import time
import stomp


class MyListener(stomp.ConnectionListener):
    def on_message(self, headers, message):
        print('MyListener:\nreceived a message mq "{}"\n'.format(message))
        global read_messages
        read_messages.append({'id': headers['message-id'], 'subscription': headers['subscription']})


class MyStatsListener(stomp.StatsListener):
    def on_disconnected(self):
        super(MyStatsListener, self).on_disconnected()
        print('MyStatsListener:\n{}\n'.format(self))


read_messages = []
host = "localhost"
port = 61613

hosts = [(host, port)]
conn = stomp.Connection(host_and_ports=hosts)
conn.set_listener('my_listener', MyListener())
conn.set_listener('stats_listener', MyStatsListener())

# wait=True means that it waits until it's established a connection with the server before returning.
conn.connect(wait=True)

conn.subscribe(destination='workshop.queueA', id='*', ack='client')
# conn.nack('workshop.queueA', '*')
# conn.send(body="A Test message", destination='workshop.queueA')

for message in read_messages:
    conn.nack(id=message['id'], subscription='workshop.queueA')
    # conn.ack(message['id'], message['subscription'])

time.sleep(3000)

conn.disconnect()
