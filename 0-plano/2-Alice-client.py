#!/usr/bin/env python

import socket


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(("127.0.0.1", 65432))
    s.sendall(b"Hello, I am Alice")
    data = s.recv(1024)

print(f"Received from Server: {data!r}")

