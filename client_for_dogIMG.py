import socket
import os
import time

HOST = '127.0.0.1'
PORT = 6666

path='//home//pi//Pictures//CAT_DOG//'

for i in range(1,6):
    for File in os.listdir(path+str(i)+'//dog'):
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((HOST, PORT))
        print('sending ',File)
        with open(path+str(i)+'//dog//'+File,'rb') as file:
            image_data=file.read(4096)
            while image_data:
                client.send(image_data)
                image_data=file.read(4096)
            file.close()
        client.close()
        time.sleep(1)
    time.sleep(1800)