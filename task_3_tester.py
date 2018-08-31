#!/usr/bin/env python3
from time import sleep
from socket import *
import sys
# address = ('localhost', 6781)
# max_size = 1000
# print('Starting client at', datetime.now())
# client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# client.connect(address)
# client.sendall(b'Hey')
# data = client.recv(max_size)
# print('At', datetime.now(), 'someone replied', data)
# client.close()

def send_numbers(port: int = 8000):
    address = ('localhost', port)
    max_size = 1024
    client = socket(AF_INET, SOCK_STREAM)
    client.connect(address)
    x = 150000
    client.sendall(x.to_bytes((x.bit_length() + 7) // 8, byteorder=sys.byteorder))
    client.close()

while True:
    sleep(.5)
    send_numbers(6781)