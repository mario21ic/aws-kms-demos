import boto3

kms_client = boto3.client('kms')
key_id = "arn:aws:kms:xxxxx"
mensaje = b"AWS Community Day"
print('Mensaje original:', mensaje)

firma = kms_client.sign(
    KeyId=key_id, Message=mensaje,
    MessageType='RAW', SigningAlgorithm='RSASSA_PKCS1_V1_5_SHA_256'
)['Signature']
print('Firma digital:', firma)

es_valido = kms_client.verify(
    KeyId=key_id, Message=mensaje,
    MessageType='RAW', Signature=firma,
    SigningAlgorithm='RSASSA_PKCS1_V1_5_SHA_256'
)['SignatureValid']
print("Verifica la firma: ", es_valido)
