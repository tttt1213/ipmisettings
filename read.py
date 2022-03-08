#! /usr/bin/env python
# encoding:utf-8

from asyncore import read
import socket
import sys

ServerAddr= "192.168.20.238"
ServerPort= 8629
mes = "192.168.20.72 NA read\n"

clientSock= socket.socket()
clientSock.connect( ( ServerAddr, ServerPort))
clientSock.send(mes.encode("UTF-8"))
#clientSock.send(mes)
clientSock.shutdown( 1)
res=""
while True:
    data= clientSock.recv( 2048)
    #print(data)
    if not data: break
    res+=data.decode("UTF-8")
    print (res,end="")
clientSock.close()
