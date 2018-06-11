import time
import asyncio
import socket

host = 'localhost'
port = 9527
loop = asyncio.get_event_loop()
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.setblocking(False)
s.bind((host, port))
s.listen(10)

counter = 0


async def monitor():
    """Keep track of the requests per second using this global variable"""
    global counter
    while True:
        time.sleep(1)
        print(counter, 'reqs/sec')
        counter = 0


async def handler(conn):
    while True:
        msg = await loop.sock_recv(conn, 1024)
        if not msg:
            break
        await loop.sock_sendall(conn, msg)
    conn.close()


async def server():
    while True:
        conn, addr = await loop.sock_accept(s)
        counter += 1

        loop.create_task(handler(conn))


loop.create_task(monitor())   # add monitoring task to watch for requests per second
loop.create_task(server())    # accept socket connections and handle them
loop.run_forever()
loop.close()