import base64
import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

def make_key(pswd):
    password = pswd
    password = password.encode()
    salt = b'salt_'

    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )

    key = base64.urlsafe_b64encode(kdf.derive(password))

    with open('key.key', 'wb') as f:
        f.write(key)

def encrypt(pswd):
    make_key(pswd)
    password = pswd
    encoded = password.encode()

    with open('key.key', 'rb') as f:
        key = f.read()

    fern = Fernet(key)
    encrypted = fern.encrypt(encoded)

    return encrypted

def decrypt(pswd):
    with open('key.key', 'rb') as f:
        key = f.read()

    fern = Fernet(key)
    decrypted = decrypted = fern.decrypt(pswd)

    return decrypted
