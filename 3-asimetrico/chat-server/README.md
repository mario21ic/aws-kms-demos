## Python puro:
1. Generar las keys y testeando:
```
./keygen.py bob
./keygen_test.py bob

./keygen.py alice
./keygen_test.py alice
```

2. Probando cifrado con el public key de Alice y descifrado con private key:
```
./keygen_test_encrypt.py alice_pub.pem HelloWorld

./keygen_test_decrypt.py bob_priv.pem HelloWorld_cipher_text.bin
./keygen_test_decrypt.py alice_priv.pem HelloWorld_cipher_text.bin
```

3. Ejecutando:
```
python Bob-server.py
python Alice-client.py
```
