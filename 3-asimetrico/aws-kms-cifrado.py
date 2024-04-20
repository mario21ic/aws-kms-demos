import boto3

kms_client = boto3.client('kms')
key_id = "arn:aws:kms:xxxxx"
mensaje = "AWS Community Day"
print("Mensaje original", mensaje)

mensaje_cifrado = kms_client.encrypt(KeyId=key_id, Plaintext=mensaje.encode('utf-8'),
        EncryptionAlgorithm='RSAES_OAEP_SHA_256')['CiphertextBlob']
print('Mensaje cifrado:', mensaje_cifrado)

mensaje_descifrado = kms_client.decrypt(KeyId=key_id, CiphertextBlob=bytes(mensaje_cifrado),
        EncryptionAlgorithm='RSAES_OAEP_SHA_256')['Plaintext']
print(f'Mensaje descifrado:', mensaje_descifrado)
