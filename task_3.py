#!/usr/bin/env python3

from socket import *
import sys
from functools import reduce
import hashlib

def factorial(x: int) -> int:
    return reduce(lambda x, y: x*y, range(1, x+1))


def to_md5(x: int, as_string: bool = False):
    if as_string:
        return hashlib.md5(bytes(str(x), 'ascii')).hexdigest()
    else:
        x = x.to_bytes((x.bit_length() + 7) // 8, byteorder=sys.byteorder)
        return hashlib.md5(x).hexdigest()


def main_server_function(port: int = 8000, num_of_workers: int = 2):
    address = ('localhost', port)
    max_size = 1024
    server = socket(AF_INET, SOCK_STREAM)
    server.bind(address)
    # Put socket into a server mode
    server.listen(5)
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
                    pass
    pass


main_server_function(6781)