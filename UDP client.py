# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 01:06:42 2013

@author: Kolan
"""

import socket

HOST = "127.0.0.1"
PORT = 5000

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((HOST, PORT))

while 1:
    print s.recv(50)