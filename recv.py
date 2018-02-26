#!/usr/bin/python3

import  socket
import  time
#          first agr ipv4 address family  , UDP protocol
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

#  this is only required at my end 

s.bind(("",8822))

while True:
	print(s.recvfrom(100))
	time.sleep(2)

