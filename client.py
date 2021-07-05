import socket
import os
import time

HOST = '127.0.0.1'
PORT = 8002

#client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#client.connect((HOST, PORT))

#path='//home//pi//Downloads//cat//cat'
path='//home//pi//Downloads//dog//dog'

for File in os.listdir(path):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))
    print('sending ',File)
    with open(path+'//'+File,'rb') as file:
        image_data=file.read(4096)
        while image_data:
            client.send(image_data)
            image_data=file.read(4096)
        file.close()
    client.close()
    time.sleep(1)

'''
for File in os.listdir(path):
    print('sending',File)
    with open(path+'//'+File,'rb') as file:
        image_data=file.read(4096)
        while image_data:
            total_bytes=client.send(image_data)
            image_data=file.read(2048)
            print(total_bytes)
    file.close()
    time.sleep(1.5)
'''

#client.close()

print('client close')