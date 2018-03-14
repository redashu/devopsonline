#!/usr/bin/python2

import  socket

x=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)


while 4 > 2 :
        data=raw_input("type your command  :  ")
        x.sendto(data,("192.168.10.161",8822))
        print(x.recvfrom(1000))


