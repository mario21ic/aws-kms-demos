#!/usr/bin/env python

import socket


HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65432  # The port used by the server
text_to_send = b"Hello, I am Alice"

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    #s.sendall(b"Hello, world")
    s.sendall(text_to_send)
    data = s.recv(1024)

print(f"Received from Server: {data!r}")

