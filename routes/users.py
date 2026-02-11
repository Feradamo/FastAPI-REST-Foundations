from fastapi import APIRouter, HTTPException
from auth.utils import generate_salt, hash_password
from db import USERS

# Definimos el router con un prefijo común y etiquetas para la documentación (Swagger)
router = APIRouter(prefix="/users", tags=["Users"])

# Definimos el endpoint para registrar un nuevo usuario
@router.post("/")
def create_user(data: dict):
    # Verificamos si el email ya existe en nuestra "base de datos"
    if any(u["email"] == data["email"] for u in USERS):
        raise HTTPException(400, "Email ya registrado")

    # Generamos los valores de seguridad para la contraseña
    salt = generate_salt()
    password_hash = hash_password(data["password"], salt)

    # Creamos el nuevo objeto de usuario
    user = {
        "id": len(USERS) + 1,
        "email": data["email"],
        "password_hash": password_hash,
        "salt": salt
    }

    # Guardamos el usuario en la lista
    USERS.append(user)

    # Retornamos solo los datos públicos
    return {"id": user["id"], "email": user["email"]}

@router.get("/")
def list_users():
    return [
        {"id": 1, "name": "Fer"},
    ]