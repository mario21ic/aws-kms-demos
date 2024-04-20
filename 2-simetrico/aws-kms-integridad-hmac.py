import boto3

kms_client = boto3.client('kms')
key_id = 'arn:aws:kms:xxxxx'
mensaje = 'AWS Community Day'
print("Mensaje original:", mensaje)

my_hmac = kms_client.generate_mac(
        KeyId=key_id,
        Message=mensaje,
        MacAlgorithm='HMAC_SHA_256'
    )['Mac']
print('HMAC generado:', my_hmac)

es_valido = kms_client.verify_mac(
        KeyId=key_id,
        Message=mensaje,
        MacAlgorithm='HMAC_SHA_256',
        Mac=my_hmac
    )['MacValid']
print('Verificación de Integridad con HMAC es:', es_valido)
