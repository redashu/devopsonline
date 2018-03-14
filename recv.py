#!/usr/bin/python3

import  socket
import  time
import  os
#          first agr ipv4 address family  , UDP protocol
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

#  this is only required at my end 

s.bind(("",8822))

while True:
    client_data=s.recvfrom(100)
    out=os.popen(client_data[0])
    final_out=out.read()
    print(type(final_out))

    #s.sendto(final_out,client_data[1])
