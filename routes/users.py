from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel

from auth.deps import get_current_user


from db import SessionLocal
from models import User
from auth.utils import generate_salt, hash_password

router = APIRouter(prefix="/users", tags=["Users"])


# -------- Pydantic schema --------
class UserCreate(BaseModel):
    email: str
    password: str


# -------- DB dependency ----------
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# -------- Create user ------------
@router.post("/")
def create_user(data: UserCreate, db: Session = Depends(get_db)):

    existing = db.query(User).filter(User.email == data.email).first()
    if existing:
        raise HTTPException(400, "Email ya registrado")

    salt = generate_salt()
    password_hash = hash_password(data.password, salt)

    user = User(
        email=data.email,
        password_hash=f"{salt}${password_hash}"
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return {"id": user.id, "email": user.email}


# -------- List users -------------
@router.get("/")
def list_users(db: Session = Depends(get_db)):
    users = db.query(User).all()
    return [{"id": u.id, "email": u.email, "password_hash": u.password_hash} for u in users]


@router.get("/me")
def me(current_user = Depends(get_current_user)):
    return {
        "id": current_user.id,
        "email": current_user.email
    }
