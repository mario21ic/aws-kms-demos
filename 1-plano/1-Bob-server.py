#!/usr/bin/env python

import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(("127.0.0.1", 65432))
    s.listen()
    print("Listening on 127.0.0.1:65432")
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            else:
                print(f"Received from Client: {data!r}")
            conn.sendall(b"Hi, I'm Bob")
