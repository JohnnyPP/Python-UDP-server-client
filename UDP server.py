# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 00:43:07 2013

@author: Kolan
"""

import socket
import time

HOST = "127.0.0.1"
PORT = 5000
DataToSend = "String data"
counter = 1

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while 1:
    s.sendto(("Number: " + str(counter) + " " + DataToSend),(HOST,PORT))
    print "Number: " + str(counter) + " " + DataToSend
    counter += 1
    time.sleep(1)