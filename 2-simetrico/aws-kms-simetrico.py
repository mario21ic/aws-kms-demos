import boto3
from botocore.exceptions import ClientError

key_id = "arn:aws:kms:xxxxx"
kms_client = boto3.client('kms')

#text_orig = input("Enter some text to encrypt: ")
text_orig = "Hello World"

# Cifrar
try:
    cipher_text = kms_client.encrypt(KeyId=key_id, Plaintext=text_orig.encode())['CiphertextBlob']
except ClientError as err:
    print("Couldn't encrypt text. Here's why: %s", err.response['Error']['Message'])
else:
    print(f"Your ciphertext is: {cipher_text}")


# Decifrar
try:
    text = kms_client.decrypt(KeyId=key_id, CiphertextBlob=cipher_text)['Plaintext']
except ClientError as err:
    print("Couldn't encrypt text. Here's why: %s", err.response['Error']['Message'])
else:
    print(f"Your text is: {text}")
