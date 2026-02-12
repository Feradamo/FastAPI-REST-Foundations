from fastapi import APIRouter, Depends, HTTPException, Response, Cookie
from sqlalchemy.orm import Session
from db import SessionLocal
from models import User
from sessions import get_user_from_session
# from sessions import create_session
from pydantic import BaseModel
from sessions import SESSIONS
from auth.jwt import create_access_token
from auth.utils import verify_password
from auth.deps import get_current_user

router = APIRouter(prefix="/auth", tags=["Auth"])

# Esquema para validar los datos que envía el usuario al loguearse
class LoginData(BaseModel):
    email: str
    password: str

# Dependencia para obtener la sesión de la base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close() # Se cierra siempre, pase lo que pase

"""
@router.post("/login")
def login(data: LoginData, response: Response, db: Session = Depends(get_db)):

    # 1. Buscamos al usuario por email
    user = db.query(User).filter(User.email == data.email).first()

    stored = user.password_hash
    salt, stored_hash = stored.split("$")

    input_hash = hash_password(data.password, salt)

    if input_hash != stored_hash:
        raise HTTPException(401, "Credenciales inválidas")
    

    # 3. Creamos la sesión en el diccionario que vimos antes
    session_id = create_session(user.id)
    
    # 4. Guardamos el ID de sesión en una Cookie en el navegador del usuario
    response.set_cookie("session_id", session_id, httponly=True)

    return {"message": "Login ok"}

    
@router.post("/logout")
def logout(response: Response, session_id: str = Cookie(None)):
    # 1. Si existe la sesión en nuestro diccionario, la eliminamos
    if session_id in SESSIONS:
        del SESSIONS[session_id]
    
    # 2. Le ordenamos al navegador que borre la cookie.
    # Al hacer 'delete_cookie', el servidor envía una instrucción para
    # que la cookie expire inmediatamente.
    response.delete_cookie("session_id")
    
    return {"message": "Sesión cerrada correctamente"}

@router.get("/me")
def me(session_id: str = Cookie(None)):   
# 1. Intentamos obtener el ID del usuario usando la cookie que nos envió
    user_id = get_user_from_session(session_id)
    
    # 2. Si no hay sesión o expiró, lanzamos error
    if not user_id:
        raise HTTPException(401, "No autorizado")
    
    # 3. Si todo está bien, le decimos quién es
    return {"user_id": user_id} 
"""


@router.post("/login")
def login(data: LoginData, db: Session = Depends(get_db)):

    user = db.query(User).filter(User.email == data.email).first()

    if not user or not verify_password(data.password, user.password_hash):
        raise HTTPException(status_code=401, detail="Credenciales inválidas")

    token = create_access_token({
        "sub": str(user.id),
        "email": user.email
    })

    return {"access_token": token, "token_type": "bearer"}