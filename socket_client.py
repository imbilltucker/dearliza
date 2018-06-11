from collections import deque
import errno
import asyncio
import socket
import time

host = 'localhost'
port = 9527
loop = asyncio.get_event_loop()
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.setblocking(False)
data = b'meep'

while True:
    try:
        s.connect((host, port))
        loop.create_task(s.send(data))
        s.detach()
    except socket.error as e:
        if e.args[0] == errno.EWOULDBLOCK:
            time.sleep(1)
        else:
            print(e)
            break



