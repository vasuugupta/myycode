#!/usr/bin/python3
import socket
recv_ip="127.0.0.1"
recv_port=4444          # ip string m or port int m ,port no range -(0-1024)
# netstat -nulp (linux)  to check wheather port no is in use or not
# creating udp socket
#[for i in dir(socket) if 'socket'in i]

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)  # ip type v4,udp
# fitting ip & port with udp sockets

s.bind((recv_ip,recv_port))  #call in tuple or list
# recv data from sender
while 4>2 :
	data=s.recvfrom(100)   #length of data u wanna recvie
	ndata=data[0].decode('ascii')
	print("msg from sender",ndata)
	print("sender ip +port --socket  ",data[1])
# reply to sender
	rply =input("type ur reply==")
	s.sendto(rply.encode('ascii'),data[1])
s.close()                                                       
