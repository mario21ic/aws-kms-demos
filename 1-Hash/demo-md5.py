import hashlib

# formato bytes
informacion = b'Hello World'
print("informacion:", informacion)

myhash = hashlib.md5(informacion) 
print("hash md5:", myhash.hexdigest())

### Se agrega UN punto al final de la cadena
informacion = b'Hello World.' # <-
print("informacion:", informacion)
hash_nuevo = hashlib.md5(informacion)
print("nuevo hash md5:", hash_nuevo.hexdigest())
