#!/usr/bin/env python3

from socket import *
import sys
import os
from functools import reduce
import hashlib

def factorial(x: int) -> int:
    if x == 0:
        return 0
    return reduce(lambda x, y: x*y, range(1, x+1))


def to_md5(x: int, as_string: bool = False):
    if as_string:
        return hashlib.md5(bytes(str(x), 'ascii')).hexdigest()
    else:
        x = x.to_bytes((x.bit_length() + 7) // 8, byteorder=sys.byteorder)
        return hashlib.md5(x).hexdigest()


def run_server(server, max_size):
    with server as s:
    # Wait for the incoming connection
        while True:
            connection, client_address = s.accept()
            with connection as c:
                while True:
                    data = c.recv(max_size)
                    if data:
                        val = int.from_bytes(data, byteorder=sys.byteorder, signed=False)
                        print(to_md5(factorial(val)))
                    else:
                        break



def main_server_function(port: int = 8000, num_of_workers: int = 2):
    address = ('localhost', port)
    max_size = 1024
    server = socket(AF_INET, SOCK_STREAM)
    server.bind(address)
    # Put socket into a server mode
    server.listen(5)
    for i in range(num_of_workers):
        pid = os.fork()
        if pid == 0:
            childpid = os.getpid()
            try:
                while True:
                    connection, client_address = server.accept()
                    data = connection.recv(max_size)
                    val = int.from_bytes(data, byteorder=sys.byteorder, signed=False)
                    responce = to_md5(factorial(val), as_string=True)
                    connection.sendall(bytes(responce, 'ascii'))
                    connection.close()
            except KeyboardInterrupt:
                sys.exit()
    try:
        # Wait child processes to complete
        os.waitpid(-1, 0)
    except KeyboardInterrupt:
        sys.exit()


main_server_function(6781, num_of_workers = 10)