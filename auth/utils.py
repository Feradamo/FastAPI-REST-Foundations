import hashlib
import os

def generate_salt():
    return os.urandom(16).hex()

def hash_password(password: str, salt: str):
    return hashlib.pbkdf2_hmac(
        "sha256",
        password.encode(),
        salt.encode(),
        100_000
    ).hex()
