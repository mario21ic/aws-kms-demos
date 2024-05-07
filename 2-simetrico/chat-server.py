#!/usr/bin/env python

import socket
import boto3

kms_client = boto3.client('kms')
key_id = 'arn:aws:kms:xxxxx'
mensaje_server = "Saludos desde AWS Peru Meetup"
print("Mensaje a enviar:", mensaje_server)

def cifrar(mensaje):
    return kms_client.encrypt(KeyId=key_id, Plaintext=mensaje.encode())['CiphertextBlob']

def descifrar(mensaje_cifrado):
    return kms_client.decrypt(KeyId=key_id, CiphertextBlob=mensaje_cifrado)['Plaintext']

HOST = "127.0.0.1"
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.bind((HOST, PORT))
    server.listen()
    print(f"Listening on {HOST}:{PORT}")
    conn, addr = server.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            else:
                print(f"Mensaje de Cliente: {data!r}")
                mensaje_client = descifrar(data)
                print(f"Mensaje de Cliente descifrado: {mensaje_client}")

            conn.sendall(cifrar(mensaje_server))
