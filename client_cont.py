import socket
import os
from threading import Thread


import socket
import time

s = socket.socket()  
host = socket.gethostname()        
port = 10016



# s.connect((host, port))
# print (s.recv(1024)) 
# s.close() 


s.connect((host, port))
while True:
    s.send('0')
    a = s.recv(1024)
    print(a)
    # s.close() 