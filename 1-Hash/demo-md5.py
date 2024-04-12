import hashlib

informacion = b'Hello World'


myhash = hashlib.md5(informacion) 
print("hash md5:", myhash.hexdigest())

### Se agrega UN punto al final de la cadena
informacion = b'Hello World.' # <-
hash_nuevo = hashlib.md5(informacion)
print("nuevo hash md5:", hash_nuevo.hexdigest())