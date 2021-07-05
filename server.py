import socket
import numpy as np
import cv2
import io
import PIL.Image as Image
import time
import math

#count=0;
HOST = '127.0.0.1'
PORT = 8002

start_time=math.floor(time.time())
end_time=math.floor(time.time())+10


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(10)
print('server start at:%s %s'%(HOST,PORT))
print('wait for connection...')

#server open 1000 seconds

while True:
    conn, addr = server.accept()
    #print('connected by '+str(addr))
    clientMessage = conn.recv(4096)
    #print(clientMessage)
    file_stream=io.BytesIO()
    while clientMessage:
        file_stream.write(clientMessage)
        clientMessage=conn.recv(4096)
    image=Image.open(file_stream)
    #image.save('//home//pi//Pictures//cat_received//newcat'+str(math.floor(time.time()))+'.jpg')
    image.save('//home//pi//Pictures//dog_received//newdog'+str(math.floor(time.time()))+'.jpg')
    print('img saved')
    image.close()
    conn.close()
    file_stream.close()
    end_time=math.floor(time.time())

print('server closed...')

'''
while True:
    conn, addr = server.accept()
    print('connected by '+str(addr))
    while True:
        clientMessage = conn.recv(4096)
        if(clientMessage):
            print(clientMessage)
            print('++++++++++++++++++++++++++++++++++++++++++++++++++++++')
            file_stream=io.BytesIO()
            while clientMessage:
                file_stream.write(clientMessage)
                clientMessage=conn.recv(4096)
            image=Image.open(file_stream)
            print('count=',count)
            image.save('//home//pi//Pictures//3//new'+str(++count)+'.png',format='PNG')
            print('img saved')
            image.close()
            file_stream.close()
    conn.close()
'''
