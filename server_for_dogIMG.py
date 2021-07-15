import socket
import numpy as np
import io
import PIL.Image as Image
import time
import math

#count=0;
HOST = '127.0.0.1'
PORT = 6666

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(10)
print('server start at:%s %s'%(HOST,PORT))
print('wait for connection...')

while True:
    conn, addr = server.accept()
    clientMessage = conn.recv(4096)
    file_stream=io.BytesIO()
    while clientMessage:
        file_stream.write(clientMessage)
        clientMessage=conn.recv(4096)
    image=Image.open(file_stream)
    image.save('//home//pi//Pictures//dog_received//newdog'+str(math.floor(time.time()))+'.jpg')
    print('img saved')
    image.close()
    conn.close()
    file_stream.close()