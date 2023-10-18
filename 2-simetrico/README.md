```
export KEY_SECRET="MvJGv09gMnTnKSQbvQo1RBGeuiE72BSAqwWNQk9cluA="
python Bob-server.py
python Alice-client.py
```

Ahora intentemos con otro key:
```
export KEY_SECRET=$(python -c "from cryptography.fernet import Fernet; print(Fernet.generate_key())")
python Alice-client.py
```
