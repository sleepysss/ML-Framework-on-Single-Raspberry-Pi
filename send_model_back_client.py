import socket
import sys

s = socket.socket()
s.connect(("localhost",9999))
f = open ("//home//pi//Documents//model.h5", "rb")
l = f.read(1024)
while (l):
    s.send(l)
    l = f.read(1024)
s.close()