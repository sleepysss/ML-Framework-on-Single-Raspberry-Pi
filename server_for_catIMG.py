import socket
import numpy as np
import io
import PIL.Image as Image
import time
import math

HOST = '127.0.0.1'
PORT = 8000

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
    image.save('//home//pi//Pictures//cat_received//newcat'+str(math.floor(time.time()))+'.jpg')
    print('img saved')
    image.close()
    conn.close()
    file_stream.close()