def get_password(IP_address):

	from asyncore import read
	import socket
	import sys

	ServerAddr= "192.168.20.238"
	#ServerPort = 2918
	ServerPort = 8629 
	#print(IP_address)
	mes = IP_address + " NA read \n"
	#print (mes)
	clientSock= socket.socket()
	clientSock.connect( ( ServerAddr, ServerPort))
	clientSock.send(mes.encode("UTF-8"))
	clientSock.shutdown( 1)

	res=""
	while True:
		data = clientSock.recv( 2048)
		#print(data)
		if not data: break
		res+=data.decode("UTF-8")
		print (res,end="")
		clientSock.close()
		
		return res

#get_password("192.168.20.72")