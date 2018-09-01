#!/usr/bin/env python3
from time import sleep, time
from socket import *
import sys
import os


def send_numbers(port: int = 8000):
    address = ('localhost', port)
    max_size = 1024
    client = socket(AF_INET, SOCK_STREAM)
    client.connect(address)
    x = int(100)
    init_time = time()
    client.sendall(x.to_bytes((x.bit_length() + 7) // 8, byteorder=sys.byteorder))
    data = client.recv(max_size)
    print('Recieved', data, 'at', time())
    # print('Processing took:', time() - init_time, '\n')
    client.close()


PORT = 6781


print('Init time', time())
for i in range(10):
    pid = os.fork()
    if pid == 0:
        try:
            send_numbers(PORT)
            while 1:
                pass
        except KeyboardInterrupt:
            sys.exit()

try:
    os.waitpid(-1, 0)
except KeyboardInterrupt:
    sys.exit()
except:
    print('lol')