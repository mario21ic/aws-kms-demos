#!/usr/bin/env python

import os
import socket

import boto3

kms_client = boto3.client('kms')
key_id = 'arn:aws:kms:xxxxx'
mensaje_cliente = "Hola soy un cliente"
print("Mensaje a enviar:", mensaje_cliente)

def cifrar(mensaje):
    return kms_client.encrypt(KeyId=key_id, Plaintext=mensaje.encode('utf-8'),
        EncryptionAlgorithm='RSAES_OAEP_SHA_256')['CiphertextBlob']

def descifrar(mensaje_cifrado):
    return kms_client.decrypt(KeyId=key_id, CiphertextBlob=bytes(mensaje_cifrado),
        EncryptionAlgorithm='RSAES_OAEP_SHA_256')['Plaintext']

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.connect(("127.0.0.1", 65432))
    server.sendall(cifrar(mensaje_cliente))
    data = server.recv(1024)

print(f"Mensaje del Server: {data}")
mensaje_server = descifrar(data)
print(f"Mensaje del Server descifrado: {mensaje_server}")
