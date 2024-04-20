import hashlib

informacion = b'Hello World'
print("informacion", informacion)


myhash = hashlib.sha1(informacion) 
print("hash sha1:", myhash.hexdigest())

myhash = hashlib.sha256(informacion) 
print("hash sha256:", myhash.hexdigest())

myhash = hashlib.sha512(informacion) 
print("hash sha512:", myhash.hexdigest())
