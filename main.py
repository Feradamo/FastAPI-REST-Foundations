# Importamos FastAPI y el router de usuarios con un alias
from fastapi import FastAPI
from routes.users import router as users_router

# Creamos la instancia principal de la aplicación FastAPI
app = FastAPI()

# Registramos el router de usuarios en la aplicación
app.include_router(users_router)