#!/usr/bin/python3
import socket
recv_ip="127.0.0.1"
recv_port=4444          # ip string m or port int m ,port no range -(0-1024)
# netstat -nulp (linux)  to check wheather port no is in use or not
# creating udp socket
#[for i in dir(socket) if 'socket'in i]

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)  # ip type v4,udp
# sending data to reciever

while 4>3 :
	msg = input("pls enter msg=")
	nmsg=msg.encode('ascii')
	s.sendto(nmsg,(recv_ip,recv_port))
	print(s.recvfrom(10))
