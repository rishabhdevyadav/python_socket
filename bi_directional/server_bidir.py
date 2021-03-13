#!/usr/bin/python
# coding=utf-8

import socket, time

#things to begin with
def Tcp_connect( HostIp, Port ):
    global s
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HostIp, Port))
    return
    
def Tcp_server_wait ( numofclientwait, port ):
	global s2
	s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
	s2.bind(('',port)) 
	s2.listen(numofclientwait) 

def Tcp_server_next ( ):
		global s
		s = s2.accept()[0]
   
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
  # print("End Of Items in Array")

Tcp_server_wait ( 5, 17098 )
Tcp_server_next()
while True:

	Tcp_Read_Array()
	arr = [4, 5, 6]
	Tcp_Write_Array(arr)
	# time.sleep(0.5)


Tcp_Close()