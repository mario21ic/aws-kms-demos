import boto3
from botocore.exceptions import ClientError

kms_client = boto3.client('kms')
key_id = "arn:aws:kms:xxxxx"
text_orig = "Aws Community Day - Guatemala"

# Encrypt
try:
    cipher_text = kms_client.encrypt(KeyId=key_id, Plaintext=text_orig.encode())['CiphertextBlob']
except ClientError as err:
    print("Hubo un error: %s", err.response['Error']['Message'])
else:
    print(f"Texto cifrado: {cipher_text}")


# Decrypt
try:
    text = kms_client.decrypt(KeyId=key_id, CiphertextBlob=cipher_text)['Plaintext']
except ClientError as err:
    print("Hubo un error: %s", err.response['Error']['Message'])
else:
    print(f"Texto descifrado: {text}")
