# Importamos FastAPI y los routers (las rutas de tu API)
from fastapi import FastAPI
from routes.users import router as users_router
from routes.auth import router as auth_router
from db import engine, Base # Importamos el motor y la clase Base de tu configuración inicial

# 1. Creamos la instancia principal de la aplicación FastAPI
app = FastAPI()

# 2. Registramos los routers
# Esto permite que las rutas definidas en otros archivos sean accesibles
app.include_router(users_router)
app.include_router(auth_router)

# 3. CREACIÓN DE TABLAS
# Esta línea busca todos los modelos (tablas) que definiste y los crea en la DB
# Solo crea las tablas que no existen; si ya existen, no hace nada.
Base.metadata.create_all(bind=engine)