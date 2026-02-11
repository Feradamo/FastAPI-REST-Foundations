from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from db import USERS

router = APIRouter(prefix="/auth", tags=["Auth"])

class LoginData(BaseModel):
    email: str
    password: str


@router.post("/login")
def login(data: LoginData):
    for u in USERS:
        if u["email"] == data.email and u["password"] == data.password:
            return {"message": "Login ok", "user_id": u["id"]}