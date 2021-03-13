#!/usr/bin/python
# coding=utf-8

import socket, time

def Tcp_connect( HostIp, Port ):
    global s
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HostIp, Port))
    return
   
def Tcp_Write(D):
   s.send(D + '\r')
   return 
   
def Tcp_Read( ):
	a = ' '
	b = ''
	while a != '\r':
		a = s.recv(1)
		b = b + a
	return b

def Tcp_Close( ):
   s.close()
   return 
 
def Tcp_Write_Array(myArray):
  myArrayString = ''
  for item in myArray:
    # print("item: ", item)
    myArrayString = myArrayString + str(item) + "|"
  # print(myArrayString)
  s.send((myArrayString).encode())  
  return

def Tcp_Read_Array():
  files = s.recv(1024)
  files = files.decode()
  myArray = files.split('|')

  for myItem in myArray:
    print(myItem)
  return myItem

Tcp_connect( '127.0.0.1', 17098) 

while True:

  arr = [1, 2, 3]
  Tcp_Write_Array(arr)
  Tcp_Read_Array()
  
  time.sleep(1)

Tcp_Close()