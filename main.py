from fastapi import FastAPI

# Creamos la app principal de FastAPI
app = FastAPI()

# -------------------------------
# GET /users
# Devuelve una lista fija de usuarios
# -------------------------------
@app.get("/users")
def list_users():
    return [
        {"id": 1, "name": "Fer"},
        {"id": 2, "name": "Ana"}
    ]
# -------------------------------
# GET /users/{user_id}
# user_id es un path parameter tipado como int
# -------------------------------
@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"id": user_id, "name": "User " + str(user_id)}
# -------------------------------
# POST /posts
# post es el body enviado como JSON
# -------------------------------
@app.post("/posts")
def create_post(post: dict):
    return {"message": "Post creado", "data": post}
# -------------------------------
# GET /posts/{post_id}
# -------------------------------
@app.get("/posts/{post_id}")
def get_post(post_id: int):
    return {"id": post_id, "title": f"Post {post_id}"}
