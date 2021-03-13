import socket
import os
from threading import Thread
import thread
import threading
import time
import datetime
import numpy as np

def listener(client, address):
    print "Accepted connection from: ", address
    with clients_lock:
        clients.add(client)
    try:    
        while True:
            # data = client.recv(1024)
            # if not data:
            #     break
            # else:
            #     print repr(data)
            #     with clients_lock:
            #         for c in clients:
            #             c.sendall(data)

            data = client.recv(1024)
            if data == '0':
                timestamp = datetime.datetime.now().strftime("%I:%M:%S %p")
                # timestamp = [0,1,2,3,4,5]
                print(timestamp)
                client.send(timestamp)
                time.sleep(2)




    finally:
        with clients_lock:
            clients.remove(client)
            client.close()

clients = set()
clients_lock = threading.Lock()

host = socket.gethostname()
port = 10016

s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host,port))
s.listen(3)
th = []

while True:
    # print "Server is listening for connections..."
    # client, address = s.accept()
    # timestamp = datetime.datetime.now().strftime("%I:%M:%S %p")
    # client.send(timestamp) 
    # time.sleep(10)
    # th.append(Thread(target=listener, args = (client,address)).start())

    client, address = s.accept()
    th.append(Thread(target=listener, args = (client,address)).start())

s.close()