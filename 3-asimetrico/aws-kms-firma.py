import boto3
import base64

kms_client = boto3.client('kms')
key_id = "arn:aws:kms:xxxx"
plaintext_message = "Aws Community Day - Guatemala"

def encrypt_message(message, key_id):
    response = kms_client.encrypt(
        KeyId=key_id,
        Plaintext=message.encode('utf-8'),
        EncryptionAlgorithm='RSAES_OAEP_SHA_256' # algoritmo a usar
    )
    return base64.b64encode(response['CiphertextBlob']).decode('utf-8')

def decrypt_message(ciphertext, key_id):
    ciphertext_blob = bytes(base64.b64decode(ciphertext))
    response = kms_client.decrypt(
        KeyId=key_id,
        CiphertextBlob=ciphertext_blob,
        EncryptionAlgorithm='RSAES_OAEP_SHA_256' # algoritmo a usar
    )
    return response['Plaintext'].decode('utf-8')


encrypted_message = encrypt_message(plaintext_message, key_id)
print(f'Mensaje cifrado: {encrypted_message}')

decrypted_message = decrypt_message(encrypted_message, key_id)
print(f'Mensaje descifrado: {decrypted_message}')

