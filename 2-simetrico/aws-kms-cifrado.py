import boto3

kms_client = boto3.client('kms')
key_id = "arn:aws:kms:xxxxxxx"
mensaje = "AWS Community Day"
print("Texto original:", mensaje)

# Cifrar
mensaje_cifrado = kms_client.encrypt(KeyId=key_id, Plaintext=mensaje.encode())['CiphertextBlob']
print('Texto cifrado:', mensaje_cifrado)

# Descifrar
mensaje_descifrado = kms_client.decrypt(KeyId=key_id, CiphertextBlob=mensaje_cifrado)['Plaintext']
print('Texto descifrado:', mensaje_descifrado)
