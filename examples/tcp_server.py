#!/usr/bin/env python3
from datetime import datetime
import socket

address = ('localhost', 6781)
max_size = 1000
print('Starting server at', datetime.now())
print('Waiting for client to call')
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(address)
server.listen(5)
client, addr = server.accept()
data = client.recv(max_size)
print('At', datetime.now(), client.getpeername(), 'said', data)
client.sendall(b'Are you talking to me?')
client.close()
server.close()