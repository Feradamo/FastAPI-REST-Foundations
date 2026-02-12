import hashlib
import secrets


def generate_salt():
    return secrets.token_hex(16)

def hash_password(password: str, salt: str):
    return hashlib.pbkdf2_hmac(
        "sha256",           # Algoritmo de hash base.
        password.encode(),  # Convierte la contraseña de texto a bytes.
        salt.encode(),      # Convierte la sal de texto a bytes.
        100_000             # Número de iteraciones. A mayor número, más lento el ataque,
                            # pero también más carga para tu servidor.
    ).hex()

def verify_password(plain_password: str, stored_password: str):
    salt, hashed = stored_password.split("$")
    return hash_password(plain_password, salt) == hashed
